using System;
using System.Collections.Generic;
using System.Text;

namespace ATalking
{
    public class User
    {
        public string UserName { get; set; }
        public string PhoneNumber { get; set; }
        public string Password { get; set; }
        public User() { }
        public User(string Username, string PhoneNumber, string Password)
        {
            this.UserName = UserName;
            this.PhoneNumber = PhoneNumber;
            this.Password = Password;

        }
        public bool CheckInformation()
        {
            if (!this.UserName.Equals("") && !this.PhoneNumber.Equals("") && this.Password.Equals(""))
                return true;
            else
                return false;
        }
    }
}
