from . import BaseProvider
from .. import Generator
import itertools
class Provider(BaseProvider):
	"""
	This provider is a collection of functions to generate personal profiles and identities.

	"""

	def simple_profile(self):
		"""
		Generates a basic profile with personal informations
		"""

		return {"username":self.generator.user_name(),
			"name":self.generator.name(),
			"sex": self.random_element(["M","F"]),
			"address":self.generator.address(),
			"mail":self.generator.free_email(),

			#"password":self.generator.password()
			"birthdate":self.generator.date(),

		}


	def profile(self,fields=[]):
		"""
		Generates a complete profile.
		If "fields" is not empty, only the fields in the list will be returned
		"""
		d={
		"job":self.generator.job(),
		"company":self.generator.company(),
		#ssn is US only. It should be refactored to use the locale
		"ssn":self.numerify("###-##-####"),
		"residence":self.generator.address(),
		"current_location":(self.generator.latitude(),self.generator.longitude()),
		"blood_group":"".join(self.random_element(list(itertools.product(["A","B","AB","0"],["+","-"]))))
		}

		d["website"]=[self.generator.url() for i in range(1,self.random_int(2,5))]
		d= dict(d,**self.generator.simple_profile())
		#field selection
		if len(fields)>0:
			d={i:j for i,j in d.items() if i in fields}

		return d

