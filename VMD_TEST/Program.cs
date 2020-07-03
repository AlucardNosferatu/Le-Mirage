using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Scallion.DomainModels;
using Scallion.DomainModels.Components;

namespace VMD_TEST
{
    class Program
    {
        static void Main(string[] args)
        {
            Motion m = new Motion();
            m.Load("Test.vmd");
            foreach(KeyFrame KF in m.Bones[0].KeyFrames)
            {
                BoneKeyFrame TempKF = (BoneKeyFrame)KF;
                Console.WriteLine(TempKF.KeyFrameIndex);
                Console.WriteLine(TempKF.Quaternion.W + "  " + TempKF.Quaternion.X + "  " + TempKF.Quaternion.Y + "  " + TempKF.Quaternion.Z);
                Console.WriteLine(TempKF.Position.X + "  " + TempKF.Position.Y + "  " + TempKF.Position.Z);
                Console.ReadKey();
            }
            //m.Save("C:\\Users\\Scrooge\\Desktop\\Output.vmd");
            Console.ReadKey();
        }
    }
}
