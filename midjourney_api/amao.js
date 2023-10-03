let elements = document.querySelectorAll(".messageContent-2t3eCI");
elements = [...elements].map(content => content.innerText);
let images = [...document.querySelectorAll(".originalLink-Azwuo9")];

let downloadList = images.map((img, index) => {
  let src = img.href;
  let url = elements[index].match(/https:\/\/s.mj.run\/\S+/)[0]; // 提取超链接
  let folderName = elements[index].match(/a photo of a (\S+)/)[1]; // 提取文件夹名部分

  return folderName + ' ' + url + " " + src; // 组合文件名和源URL
}).join('\n');
let textarea = document.createElement('textarea');
textarea.value = downloadList;
document.body.appendChild(textarea);
textarea.select();
document.execCommand('copy');
document.body.removeChild(textarea);
alert('Text copied to clipboard');
