import jwt
secret_key = "jgreiojguiptrhjguithrjguihjtruishgjutrjhguit"

def create_token(user_ID , firstName , lastName):
    user = {"user_ID":user_ID , "firstName":firstName , "lastName":lastName}
    token = jwt.encode(user ,secret_key,algorithm= "HS256")
    return token
    
def decode_jwt(token):
    return jwt.decode(token , secret_key , algorithms=["HS256"])