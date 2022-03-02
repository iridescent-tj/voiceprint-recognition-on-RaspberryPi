%¼������
duration = 2;
fs = 16000;
nbits = 16; 
format = 'int16';	
waveFile='D:\Program Files\MATLAB704\work\Bb'; %¼��֮����ļ����õ�·��
y = wavrecord(duration*fs, fs, format);  % MATLAB��toolbox��audiovideo�����û�����������
y = double(y);			% Convert from a uint8 to double array
y = (y-mean(y))/(2^nbits/2);	% Make y zero mean and unity maximum
plot((1:length(y))/fs, y); grid on
axis([-inf inf -1 1]);
title(['Wave form of "', waveFile, '"']);
wavwrite(y, fs, nbits, waveFile);  % MATLAB��toolbox��voicebox ���û�����������
fprintf('·���ǡ]%s�^   \n\n', waveFile);