#!/usr/bin/perl

# GIF画像連結ライブラリを読みこむ
require "gifcat.pl";

# カウンターファイルを読み込み、加算して書きこむ
open(FILE, "+< count.txt");      # 読み書きモードでオープン
seek(FILE, 0, 0);                # ポインタを先頭に移動
$count = <FILE>;                 # カウンタ値を読み出す
$count++;                        # ひとつ加算する
seek(FILE, 0, 0);                # ポインタを先頭に戻す
print FILE "$count\n";           # 加算した値を書き戻す
close(FILE);                     # ファイルを閉じる

# 5桁の0埋め数値に変換
$count = sprintf("%05d", $count);

# GIF画像のリストを得る
for ($i = 0; $i < length($count); $i++) {
    $n = substr($count, $i, 1);  # $i桁目の値$nを取り出し、
    push(@files, "$n.gif");      # $n.gif のファイル名を配列に追加
}

# GIF画像を書き出す
print "Content-type: image/gif\n";    # イメージを書き出す
print "\n";
binmode(STDOUT);                      # 出力はバイナリモードで
print gifcat'gifcat(@files);          # GIF画像を連結して書き出す