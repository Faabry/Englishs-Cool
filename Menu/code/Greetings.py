from datetime import datetime as dt


class Greeting:

    def greetings(self):
        self.date = dt.now()
        self.hour = self.date.hour

        if self.hour < 12:
            return "Bom Dia ☀️"
        
        elif self.hour < 18:
            return "Boa Tarde ⛅"
        
        else:
            return "Boa Noite 🌙"
        

    def get_hour(self):
        self.date = dt.now()
        self.hour = self.date.hour
        self.minute = self.date.minute

        if self.hour < 10:
            self.hour = f"{0}{self.hour}"

        elif self.minute < 10:
            self.minute = f"{0}{self.minute}"
        
        return f"{self.hour}:{self.minute}"


    def get_day(self):
        self.date = dt.today()
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year
        self.list_months = ["Janeiro", "Fevereiro",
                            "Março", "Abril", 
                            "Maio", "Junho", 
                            "Julho", "Agosto", 
                            "Setembro", "Outubro", 
                            "Novembro", "Dezembro"]
        
        # Received the list of months in the month index
        self.month_name = self.list_months[self.month - 1]    
        return f"{self.day} de {self.month_name} de {self.year}"