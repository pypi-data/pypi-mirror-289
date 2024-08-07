import json,os,sys
from typing import Collection
from opentelemetry.instrumentation.instrumentor import BaseInstrumentor
from opentelemetry.trace import get_tracer
from detail.client.instrumentation.attrs import build_attributes,set_attributes
from detail.client.serialization import DetailEncoder
class EnvInstrumentor(BaseInstrumentor):
	def instrumentation_dependencies(A):return[]
	def _instrument(E,**F):
		A='environ';B=get_tracer(__name__)
		with B.start_as_current_span(A)as C:D=build_attributes('env',{A:json.dumps(dict(os.environ),cls=DetailEncoder),'argv':json.dumps(sys.argv,cls=DetailEncoder)});set_attributes(C,D)
	def _uninstrument(A,**B):0