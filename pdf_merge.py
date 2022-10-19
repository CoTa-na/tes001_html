# 1: ライブラリ設定
import tkinter
import PyPDF2
import glob
import os
 
# 2: フォルダ内のPDFファイルを取得
path = os.getcwd()
filelist = sorted(glob.glob('*.pdf'))
print(filelist)
 
# 3: PDF結合オブジェクトの生成
merger = PyPDF2.PdfFileMerger(strict=False)
 
# 4: PDFを1ファイルずつ結合
for file in filelist:
    merger.append(file)
 
# 4.2: 最初のPDFのファイル名を”name”に格納
name = os.path.splitext(os.path.basename(filelist[0]))[0] 
print("生成するPDFファイル名：" + name + "_merge.pdf") 
print("PDF結合処理中・・・・・しばらくお待ちください。") 

# 5: オブジェクトを書き出し
# merger.write(os.path.join(path, filelist[0].stem + '_merge.pdf'))　ファイル名没コード
# merger.write(filelist[0] + '_merge.pdf')　ファイル名没コード　"***.pdf_merger.pdf" となってしまう。
merger.write(name + '_merge.pdf')
merger.close()

print("完了")

# 6: .exeファイルとした際に完了メッセージを表示させた方が良いので実装
tkinter.messagebox.showinfo(
        title="完了メッセージ", 
        message="お待たせしました。",
        detail="PDF結合処理が完了しました。")