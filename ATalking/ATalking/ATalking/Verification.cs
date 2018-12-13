using System;
using System.Collections.Generic;
using System.Text;
using AfricasTalkingCS;

namespace ATalking
{
    class Verification
    {
        static public void Main()
        {

     
            string username = "BobMburu";
            string apiKey = "MyAppAPIKey";

            
            

            AfricasTalkingGateway gateway = new AfricasTalkingGateway(username, apiKey);

            // Any gateway errors will be captured by our custom Exception class below,
            // so wrap the call in a try-catch block   
            try
            {

                // Thats it, hit send and we'll take care of the rest
                User user = new User();
                string recepient = user.PhoneNumber;
                string message = user.Password;

                dynamic results = gateway.SendMessage(recepient, message);

                foreach (dynamic result in results)
                {
                    Console.Write((string)result["number"] + ",");
                    Console.Write((string)result["status"] + ","); 
                    Console.Write((string)result["statusCode"] + ",");
                    Console.Write((string)result["messageId"] + ",");
                    Console.WriteLine((string)result["cost"]);
                }
            }
            catch (AfricasTalkingGatewayException e)
            {

                Console.WriteLine("Encountered an error: " + e.Message);

            }
        }
    }
}
