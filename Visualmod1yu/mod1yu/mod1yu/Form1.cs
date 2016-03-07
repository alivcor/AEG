using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
namespace mod1yu
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Process p1 = new Process();
            p1.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            p1.StartInfo.FileName = "C:\\Users\\" + Environment.UserName + "\\Desktop\\AEG\\FE\\tfidf.bat";
            p1.Start();
            progressBar1.Increment(progressBar1.Maximum / 4);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            progressBar1.Increment(progressBar1.Maximum / 4);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            File.WriteAllText("C:\\Users\\Abhinandan\\Desktop\\AEG\\FE\\ess1.txt", richTextBox1 .Text, Encoding.ASCII);
            progressBar1.Increment(progressBar1.Maximum / 4);

            File.WriteAllText("C:\\Users\\Abhinandan\\Desktop\\AEG\\FE\\ess2.txt", richTextBox2.Text, Encoding.ASCII);
            Process p2 = new Process();
            p2.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            p2.StartInfo.FileName = "C:\\Users\\" + Environment.UserName + "\\Desktop\\AEG\\FE\\preproc.bat";
            p2.Start();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            Process p3 = new Process();
            string t="";
            string filename = @"C:\Users\Abhinandan\Desktop\AEG\FE\words.txt";
            p3.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            p3.StartInfo.FileName = "C:\\Users\\" + Environment.UserName + "\\Desktop\\AEG\\FE\\tokenizer.bat";
            p3.Start();
            MessageBox.Show("Tokenized");
            System.IO.StreamReader objReader= new System.IO.StreamReader(filename) ;
            do
            {
                t = t + objReader.ReadLine() + "\r\n";

            } while (objReader.Peek() != -1);
            richTextBox4.Text = t;

            objReader .Close();

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void richTextBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            progressBar1.Increment(progressBar1.Maximum / 4);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Process p4 = new Process();
            string t2 = "";
            string filename2 = @"C:\Users\Abhinandan\Desktop\AEG\FE\pos_tags.txt";
            p4.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            p4.StartInfo.FileName = "C:\\Users\\" + Environment.UserName + "\\Desktop\\AEG\\FE\\pos_tagm.bat";
            p4.Start();
            MessageBox.Show("posTagged...!");
            System.IO.StreamReader objReader2 = new System.IO.StreamReader(filename2);
            do
            {
                t2 = t2 + objReader2.ReadLine() + "\r\n";

            } while (objReader2.Peek() != -1);
            richTextBox3.Text = t2;

            objReader2.Close();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            Process p5 = new Process();
           
            p5.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            p5.StartInfo.FileName = "C:\\Users\\" + Environment.UserName + "\\Desktop\\AEG\\FE\\pos_count_b.bat";
            p5.Start();
            MessageBox.Show("posCount Done...!");

            string tn = "";
            string filenamen = @"C:\Users\Abhinandan\Desktop\AEG\FE\nc.txt";
            System.IO.StreamReader objReadern = new System.IO.StreamReader(filenamen);
            do
            {
                tn = tn + objReadern.ReadLine() + "\r\n";

            } while (objReadern.Peek() != -1);
            label3.Text = tn;

            objReadern.Close();



            string tv = "";
            string filenamev = @"C:\Users\Abhinandan\Desktop\AEG\FE\vc.txt";
            System.IO.StreamReader objReaderv = new System.IO.StreamReader(filenamev);
            do
            {
                tv = tv + objReaderv.ReadLine() + "\r\n";

            } while (objReaderv.Peek() != -1);
            label4.Text = tv;

            objReaderv.Close();



            string ta = "";
            string filenamea = @"C:\Users\Abhinandan\Desktop\AEG\FE\ac.txt";
            System.IO.StreamReader objReadera = new System.IO.StreamReader(filenamea);
            do
            {
                ta = ta + objReadera.ReadLine() + "\r\n";

            } while (objReadera.Peek() != -1);
            label5.Text = ta;

            objReadera.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Process p6 = new Process();

            p6.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            p6.StartInfo.FileName = "C:\\Users\\" + Environment.UserName + "\\Desktop\\AEG\\FE\\pyench_error.bat";
            p6.Start();
        }
    }
}
