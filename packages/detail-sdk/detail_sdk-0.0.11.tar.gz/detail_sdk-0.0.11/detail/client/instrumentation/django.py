from __future__ import annotations
import gc,json
from io import BytesIO
from typing import TYPE_CHECKING,Any
from urllib.parse import urlparse
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.trace import Span
from detail.client.instrumentation.attrs import build_attributes,set_attributes
from detail.client.serialization import DetailEncoder
if TYPE_CHECKING:from django.http import HttpRequest,HttpResponse
class DetailDjangoInstrumentor(DjangoInstrumentor):
	def _instrument(B,**A):A['request_hook']=B.request_hook;A['response_hook']=B.response_hook;super()._instrument(**A)
	@staticmethod
	def request_hook(span,request):
		E='http.url';B=request;A=span;C=B._stream.read();B._stream=BytesIO(C);D={'request.body':C,'request.headers':json.dumps(list(B.headers.items()),cls=DetailEncoder)}
		if E in A.attributes:D['target']=urlparse(A.attributes[E]).path
		F=build_attributes('http',D);set_attributes(A,F)
	@staticmethod
	def response_hook(span,request,response):
		E='http.route';B=span;A=response;C={'status_code':A.status_code,'response.body':A.content};D=list(A.headers.items());D.extend([('Set-Cookie',A.output(header=''))for A in A.cookies.values()]);C['response.headers']=json.dumps(D,cls=DetailEncoder)
		if E in B.attributes:C['request.path']=B.attributes[E]
		F=build_attributes('http',C);set_attributes(B,F);gc.collect()