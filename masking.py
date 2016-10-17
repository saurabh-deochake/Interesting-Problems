#masking.py

# Information masking
# EMAIL: saurabh.d04@gmail.com => s*****4@gmail.com
# Phone: +1-848-239-8471 => +*-***-***-8471
#		 no brackets should come
import re

class Masking:
	def __init__(self):
		pass

	def _mask_email(self, email):
		if ('@' not in email or email is None):
			return null
		else:
			print email[0]+"*****"+email[email.index('@')-1]+email[email.index('@'):]

	def _mask_phone(self,phone):
		if ('(' and ')' in phone):
			phone = re.sub('[\(\)]', '', phone)
			
			print re.sub('\d', '*', phone[:len(phone)-4])+phone[-4:]
		else:
			print re.sub('\d', '*', phone[:len(phone)-4])+phone[-4:]


def main():
	mask = Masking();
	# Get input
	email = raw_input("Enter the email:")
	mask._mask_email(email)
	mask._mask_phone(raw_input("\nEnter phone:"))



if __name__ == '__main__':
	main()
