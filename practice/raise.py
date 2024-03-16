class error(Exception):
    def __init__(self, error_message):
        self.message = error_message
        
def main():
    raise error("A custom error at main()")
    
try:
    main()
except error as e:
    print(e)