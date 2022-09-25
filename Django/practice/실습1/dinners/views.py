from django.shortcuts import render
import random

# Create your views here.

def todayDinner(request):
    menus = ['치킨', '초밥', '삼겹살', '간장게장', '파스타']
    menu_idx = random.choice(range(len(menus)))
    menu_imgs = [
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA4MjZfMTA2%2FMDAxNjYxNDc5NDA4NDA5.XVtQ6bOImyC5aZ1xndwT3eCNBKj-U5S0wRbDaKpts0Eg.tw8IXoohJ5h5FOAuCFWKWtxiQNxalSw_rxpWYSMIpCkg.JPEG.nosang2020%2FIMG_0012.jpg&type=sc960_832',
        'https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000370/img/basic/a0000370_main.jpg?20201002142956&q=80&rw=750&rh=536',
        'https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA5MDZfMTUg%2FMDAxNjYyNDQzNzYxMzU3.K2IrXnNzHo0pYBxISSxKFb9K4bkFbyatbf1VrL5Wppwg.WtqjKPIJIAmgTAoq6xA5Igi7GJ_qt2Trt900DPLcp_Ag.PNG.religion2686%2F13.png&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA5MDNfODcg%2FMDAxNjYyMjA3Mjg5MTM4.vJaEW0JIAa9NQ8NmsVbWoR2edZXb_7fYoEt_tWWOFnEg.-mPmgIQXRU3B93B8SLI_y-OfhITVMirUgLRX3gOS06Ag.JPEG.kong4bean%2F1662206454445.jpg&type=sc960_832',
    ]
    menu = menus[menu_idx]
    menu_img = menu_imgs[menu_idx]
    context = {
        'menu' : menu,
        'menu_img' : menu_img,
    }
    return render(request, 'today-dinner.html', context)