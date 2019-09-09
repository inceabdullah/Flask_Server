from flask import Flask, request, redirect
import math

app = Flask(__name__)

@app.route('/deger_al', methods=['GET'])
def deger_al_():
    
    # sitem degerleri 
    
    sis_to_req = float(request.args.get("sis_to")) # c18 
    sis_tf_req = float(request.args.get("sis_tf")) # c19
    sis_mu_req = float(request.args.get("sis_mu")) # c20
    sis_n_req = float(request.args.get("sis_n")) # c21
    sis_vo_req = float(request.args.get("sis_vo")) # c22
    
    # hadde boyutlari
    
    hadde_r_req = float(request.args.get("hadde_r")) # c35
    hadde_w_req = float(request.args.get("hadde_w")) # c37
    
    # malzeme ozellikleri
    
    malz_k_req = float(request.args.get("malz_k")) # f31
    malz_n_req = float(request.args.get("malz_n")) # f32
    
    
    # sis deg
    
    sis_vr = 2*math.pi*sis_n_req*hadde_r_req/60/1000 # =2*PI()*C21*C35/60/1000 
    sis_vf = sis_to_req*sis_vo_req/sis_tf_req # =C18*C22/C19
    
    if sis_vf > sis_vr: # =IF(C24>C23, "Sağlanıyor","Sağlanmıyor") 
        sis_vo_vr = True
    else:
        sis_vo_vr  = False
        
    if sis_vr > sis_vo_req:
        sis_vr_vf = True 
    else:
        sis_vr_vf = False
       
    
    
    if sis_vo_vr == sis_vr_vf: # =IF(C25=C26, "Evet","Hayır") 
        sis_hadde = True
    else:
        sis_hadde = False
    
    # haddeleme degeri
    
    had_deg_d = sis_to_req-sis_tf_req # =C18-C19 
    had_deg_dmax = math.pow(sis_mu_req, 2)*hadde_r_req # =C20^2*C35
    
    if had_deg_d < had_deg_dmax: # =IF(C30<C31, "Evet", "Hayır")
        had_deg_hadde = True
    else:
        had_deg_hadde = False
    
    # haddeleme boyutlari
    
    had_boy_l = math.sqrt(hadde_r_req*had_deg_d) # =SQRT(C35*C30)
    
    # Guc Kuvvet Degerleri 
    
    guc_ye = math.log(sis_to_req/sis_tf_req) # =LN(C18/C19)
    guc_oo = malz_k_req*math.pow(guc_ye, malz_n_req)/(1.0+malz_n_req) # =F31*(F18^F32)/(1+F32)
    guc_f = guc_oo*hadde_w_req*had_boy_l # =F19*C37*C36
    guc_t = 0.5*guc_f*had_boy_l/math.pow(10, 6) # =0.5*F20*C36/10^6
    guc_p = 2.0*3.14*sis_n_req*guc_f*had_boy_l/60/1000 # =2*3.14*C21*F20*C36/60/1000
    
    # Birimler
    
    bir_f_mn = guc_f/math.pow(10, 6) # =F20/10^6
    bir_f_ton = guc_f/9.81/1000 # =F20/9.81/1000
    bir_p_kw = guc_p/1000 # =F22/1000
    bir_p_hp = guc_p/745.7 # =F22/745.7
    
    
    red_url = "redirect?sis_vr=%f&sis_vf=%f&sis_vo_vr=%s&sis_vr_vf=%s&sis_hadde=%s&had_deg_d=%f&had_deg_dmax=%f&had_deg_hadde=%s&had_boy_l=%f&guc_ye=%f&guc_oo=%f&guc_f=%f&guc_t=%f&guc_p=%f&bir_f_mn=%f&bir_f_ton=%f&bir_p_kw=%f&bir_p_hp=%f&" %  (sis_vr, sis_vf, sis_vo_vr , sis_vr_vf, sis_hadde, had_deg_d, had_deg_dmax, had_deg_hadde, had_boy_l, guc_ye, guc_oo, guc_f, guc_t, guc_p, bir_f_mn, bir_f_ton, bir_p_kw, bir_p_hp) 

    return redirect(red_url, code=302)
"""

like redirect?sis_vr=1.308997&sis_vf=1.420455&sis_vo_vr=True&sis_vr_vf=True&sis_hadde=True&had_deg_d=3.000000&had_deg_dmax=3.600000&had_deg_hadde=True&had_boy_l=27.386128&guc_ye=0.127833&guc_oo=175.643260&guc_f=1443056.636303&guc_t=19.759867&guc_p=206819.939032&bir_f_mn=1.443057&bir_f_ton=147.100575&bir_p_kw=206.819939&bir_p_hp=277.350059&

http://apps.ozguruygulama.com/hadde-hesabi/redirect?sis_vr=1.308997&sis_vf=1.420455&sis_vo_vr=True&sis_vr_vf=True&sis_hadde=True&had_deg_d=3.000000&had_deg_dmax=3.600000&had_deg_hadde=True&had_boy_l=27.386128&guc_ye=0.127833&guc_oo=175.643260&guc_f=1443056.636303&guc_t=19.759867&guc_p=206819.939032&bir_f_mn=1.443057&bir_f_ton=147.100575&bir_p_kw=206.819939&bir_p_hp=277.350059&

"""

@app.route('/input')
def input_():
    html_raw = """
    
    <html><body>
    
    <form action="deger_al">
    sis_to<input name="sis_to"><br />
    sis_tf<input name="sis_tf"><br />
    sis_mu<input name="sis_mu"><br />
    sis_n<input name="sis_n"><br />
    sis_vo<input name="sis_vo"><br />
    hadde_r<input name="hadde_r"><br />
    hadde_w<input name="hadde_w"><br />
    malz_k<input name="malz_k"><br />
    malz_n<input name="malz_n"><br />
    
    
<input type="submit">    </form>
    
    
    </body></html>
    
    """ # sis_to,sis_tf,sis_mu,sis_n,sis_vo,hadde_r,hadde_w,malz_k,malz_n
    return html_raw


@app.route('/redirect')
def redirect_():
    
    return ''



if __name__ == '__main__':
    app.run()


"""
              sis_vr 
                sis_vf
                sis_vo_vr # t, f
                sis_vr_vf # t, f
                sis_hadde # t, f
                had_deg_d
                had_deg_dmax
                had_deg_hadde # t, f
                had_boy_l
                guc_ye
                guc_oo
                guc_f
                guc_t
                guc_p
                bir_f_mn
                bir_f_ton
                bir_p_kw
                bir_p_hp
"""