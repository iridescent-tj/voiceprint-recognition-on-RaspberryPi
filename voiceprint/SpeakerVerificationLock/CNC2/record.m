%录音程序
duration = 2;
fs = 16000;
nbits = 16; 
format = 'int16';	
waveFile='D:\Program Files\MATLAB704\work\Bb'; %录好之后的文件放置的路径
y = wavrecord(duration*fs, fs, format);  % MATLAB中toolbox的audiovideo，如果没有需额外下载
y = double(y);			% Convert from a uint8 to double array
y = (y-mean(y))/(2^nbits/2);	% Make y zero mean and unity maximum
plot((1:length(y))/fs, y); grid on
axis([-inf inf -1 1]);
title(['Wave form of "', waveFile, '"']);
wavwrite(y, fs, nbits, waveFile);  % MATLAB中toolbox的voicebox 如果没有需额外下载
fprintf('路径是%s   \n\n', waveFile);