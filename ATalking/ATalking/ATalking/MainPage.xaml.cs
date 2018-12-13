using AfricasTalkingCS;
using Rg.Plugins.Popup.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace ATalking
{
    public partial class MainPage : ContentPage
    {
       
        AfricasTalkingGateway gateway = new AfricasTalkingGateway("BobMburu", "MyAppAPIKey");
        public MainPage()
        {
            InitializeComponent();
             
            User user = new User();
        }
        private async void  Btn_Submit_Clicked(object sender, EventArgs e)
        {
            User user = new User(Username_lbl.Text, Phone_lbl.Text, Password_lbl.Text);
            if (user.CheckInformation())
            {
                RunCheck();
                PopupNavigation.Instance.PushAsync(new PopupPage());
               
            }
            else
            {
                await DisplayAlert("Oops", "Some Details Are Missing, please try again", "Ok");
            }
        }

        private void RunCheck()
        {
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
