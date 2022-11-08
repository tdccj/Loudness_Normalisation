# coding = utf-8
# 这是一个帮助响度标准化（正常化、归一化）的程序
# @tdccj
import ffmpy3

ff = ffmpy3.FFmpeg(
    inputs={'【高清无水印】希望之花名场面素材 - 1.【高清无水印】希望之花名场面素材(Av795640030,P1).flv': None},
    outputs={'output.avi': None}
)
ff.run()
