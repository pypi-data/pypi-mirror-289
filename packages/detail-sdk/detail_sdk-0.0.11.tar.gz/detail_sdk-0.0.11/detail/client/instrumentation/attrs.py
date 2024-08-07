import json,os
from typing import Any,Dict
from opentelemetry.trace.span import format_span_id
from detail.client.context import get_thread_index,get_wsgi_span_id
from detail.client.instrumentation import NS
from detail.client.serialization import DetailEncoder
def format_otel_span_id(int_span_id):return f"0x{format_span_id(int_span_id)}"
def build_attributes(library,library_attrs):
	A=library;B={f"{NS}.library":A,f"{NS}.context.thread_index":get_thread_index(),f"{NS}.context.pid":os.getpid(),f"{NS}.context.ppid":os.getppid(),f"{NS}.context.wsgi_span_id":get_wsgi_span_id()or''}
	for(C,D)in library_attrs.items():B[f"{NS}.{A}.{C}"]=D
	return B
def build_pure_attributes(library,qualname,args,kwargs,result,empty_args=False):C=empty_args;B=kwargs;A=args;A,B=(tuple(),{})if C else(A,B);return build_attributes(library,{'qualname':qualname,'args':json.dumps(A,cls=DetailEncoder),'kwargs':json.dumps(B,cls=DetailEncoder),'emptied':C,'return':json.dumps(result,cls=DetailEncoder)})
def set_attributes(span,attrs):
	for(A,B)in attrs.items():span.set_attribute(A,B)