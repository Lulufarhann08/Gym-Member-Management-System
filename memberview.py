import os
from mysql import connector
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
class Dbconnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
               user = os.getenv("DB_USER"),
               password = os.getenv("DB_PASSWORD"),
               database = os.getenv("DB_HOST"),
               host = os.getenv("DB_NAME")
        )
            return self.connection
        except Exception as e:
            return None
      
class GymMemberManager(Dbconnect):  
            
    def get_object(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "select * from member where id=%s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
            
    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = """insert into member(name,place,plan,mobile,fee,joining_date) values(%s,%s,%s,%s,%s,%s)"""
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Data inserted successfully...!")
        except Exception as e:
            print(e)
            
            
    def get(self):
        
            self.connect = super().get_connection()
            self.cursor = self.connection.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            
            records= self.cursor.fetchall()
            return records 

    
    def retrieve(self,id=None):
        try:
            record = self.get_object(id=id)
            if record==None:
                print("no record found...!")
            print(record)
        except Exception as e:
            print(e)
        
    def put(self, id= None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connection.commit()
                return True, "Member updated successfully....!"
            else:
                return False, "No record found...!"
        except Exception as e:
            print(e)
            
    def delete(self, id=None):
            try:
                record = self.get_object(id=id)
                if record != None:
                    query = "delete from Member where id=%s"
                    self.cursor.execute(query,(id,))
                    self.connection.commit()
                    return True, "Member deleted successfully....!"
                else:
                    return False, "No record found...!"
                        
            except Exception as e:
                print(e)
                
            
instance_connection = Dbconnect()
print(instance_connection.get_connection())           

gym_instance = GymMemberManager()
#gym_instance.post(name = "Veda",place = "Kochi", mobile = "8900045005", plan="2 months", fee = 4000 ,joining_date = datetime.today())
#gym_instance.get()
#gym_instance.retrieve(id=2)
#gym_instance.put(id=2, name = "Veda",place = "Kochi", mobile = "8900045005", plan="6 months", fee = 12000 ,joining_date = datetime.today())


instance_connection.connection.close()