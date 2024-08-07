_A='__call__'
import gc,json
from typing import Any
import flask
from flask import Response,request
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.utils import unwrap
from opentelemetry.trace import get_tracer
from wrapt import wrap_function_wrapper
from detail.client import sentry
from detail.client.context import set_wsgi_span_id
from detail.client.instrumentation import NS
from detail.client.instrumentation.attrs import build_attributes,format_otel_span_id,set_attributes
from detail.client.logs import get_detail_logger
from detail.client.serialization import DetailEncoder
logger=get_detail_logger(__name__)
def before_request():
	C='http.route';A=trace.get_current_span();B={'request.body':request.get_data(as_text=True),'request.headers':json.dumps(request.headers.to_wsgi_list(),cls=DetailEncoder)}
	if C in A.attributes:B['request.path']=A.attributes[C]
	D=build_attributes('http',B);set_attributes(A,D)
def after_request(response):A=response;B=trace.get_current_span();C=build_attributes('http',{'status_code':A.status_code,'response.headers':json.dumps(A.headers.to_wsgi_list(),cls=DetailEncoder),'response.body':A.data});set_attributes(B,C);gc.collect();sentry.flush();return A
def call_wrapper(wrapped,instance,args,kwargs):
	A='wsgi'
	with get_tracer(A).start_as_current_span(A)as B:B.set_attribute(f"{NS}.library",A);set_wsgi_span_id(format_otel_span_id(B.get_span_context().span_id));return wrapped(*args,**kwargs)
def sentry_flask_setup_wrapper(wrapped,instance,args,kwargs):unwrap(flask.Flask,_A);A=wrapped(*args,**kwargs);wrap_function_wrapper(flask.Flask,_A,call_wrapper);logger.info('rewrapped flask around sentry');return A
class DetailFlaskInstrumentor(FlaskInstrumentor):
	def _instrument(D,**A):
		super()._instrument(**A)
		class B(flask.Flask):
			def __init__(A,*B,**C):super().__init__(*B,**C);A.before_request(before_request);A.after_request(after_request)
		flask.Flask=B;wrap_function_wrapper(flask.Flask,_A,call_wrapper)
		try:from sentry_sdk.integrations.flask import FlaskIntegration as C
		except ImportError:pass
		else:logger.info('sentry detected; monkeypatching FlaskIntegration.setup_once');wrap_function_wrapper(C,'setup_once',sentry_flask_setup_wrapper)