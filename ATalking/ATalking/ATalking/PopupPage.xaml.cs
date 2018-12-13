using AfricasTalkingCS;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace ATalking
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class PopupPage : ContentView
	{
        AfricasTalkingGateway gateway = new AfricasTalkingGateway("BobMburu", "MyAppAPIKey");
        int msgId = 0;
        public PopupPage()
		{
			InitializeComponent ();
             
        }
        private void On_Clicked(object sender, EventArgs e)
        {
            CheckMessage();
        }

        private void CheckMessage()
        {
            try
            {
                var res = gateway.FetchMessages(msgId);
                Console.WriteLine(res);
            }
            catch (AfricasTalkingGatewayException e)
            {
                Console.WriteLine("We had an Error: " + e.Message);
            }
        }
    }
}