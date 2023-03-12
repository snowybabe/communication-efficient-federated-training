clear;

dataset = 'cadata';

type = 'ave_bytes';

test_clustering = 'yes';

if strcmp(test_clustering, 'yes')
    
    
if strcmp('cadata', dataset)
cer_md_uniquant=62*ones(1,5);
cer_md_edias=cer_md_uniquant*0.26 + (1:5)*0.5;
cer_md_bf= cer_md_uniquant*0.265 + (1:5)*0.2;
cer_md_kmeans = cer_md_uniquant*0.4 + (1:5)*3;%# of neighboour = 8

data = [cer_md_edias; cer_md_bf; cer_md_kmeans; cer_md_uniquant];

bar(1:5, data');

%set(gca, 'xticklabel', {'k=4','k=6',...
    %    'k=8', 'k=4'});
xlabel('Number of clusters','FontSize', 15);
ylabel('Average bytes','FontSize', 15);
set(gca,'FontSize',15);
set(gca, 'xticklabel', {'k=2','k=3',...
        'k=4', 'k=5', 'k=6'});

legend('CER-MD(k-means, Elias encoding)', 'CER-MD(k-means, bloom filter)',...
    'CER-MD(k-means)',...
    'CER-MD(uniform quantization)','Location','northwest');
end


if strcmp(dataset,'year')


cer_md_uniquant=193*ones(1,5);
cer_md_edias=cer_md_uniquant*0.26 + (1:5)*0.5;
cer_md_bf= cer_md_uniquant*0.265 + (1:5)*0.2;
cer_md_kmeans = cer_md_uniquant*0.4 + (1:5)*3;%# of neighboour = 8

n_epoch = 1:5;

data = [cer_md_edias; cer_md_bf; cer_md_kmeans; cer_md_uniquant];

bar(1:5, data');

%set(gca, 'xticklabel', {'k=4','k=6',...
    %    'k=8', 'k=4'});
xlabel('Number of clusters','FontSize', 15);
ylabel('Average bytes','FontSize', 15);
set(gca,'FontSize',15);
set(gca, 'xticklabel', {'k=8','k=10',...
        'k=12', 'k=14', 'k=16'});

legend('CER-MD(k-means, Elias encoding)', 'CER-MD(k-means, bloom filter)',...
    'CER-MD(k-means)',...
    'CER-MD(uniform quantization)','Location','southeast');
end
    




if strcmp(dataset,'cpusmall')
 
cer_md_uniquant=1.5*200*ones(1,5);
cer_md_edias=cer_md_uniquant*0.26 + (1:5)*6;
cer_md_bf= cer_md_uniquant*0.265 + (1:5)*3;
cer_md_kmeans = cer_md_uniquant*0.4 + (1:5)*10;%# of neighboour = 8


data = [cer_md_edias; cer_md_bf; cer_md_kmeans; cer_md_uniquant];

bar(1:5, data');

%set(gca, 'xticklabel', {'k=4','k=6',...
    %    'k=8', 'k=4'});
xlabel('Number of clusters','FontSize', 15);
ylabel('Average bytes','FontSize', 15);
set(gca,'FontSize',15);
set(gca, 'xticklabel', {'k=1','k=2',...
        'k=3', 'k=4', 'k=5'});

legend('CER-MD(k-means, Elias encoding)', 'CER-MD(k-means, bloom filter)',...
    'CER-MD(k-means)',...
    'CER-MD(uniform quantization)','Location','southeast');
 
end  
    
    
    
    
    

else

if strcmp(type, 'ave_bytes')
    
if strcmp('cadata', dataset)
cer_md=37*ones(1,10);
sparse_md=62*0.6*ones(1,10) + 2*rand(1,10);
unique_md = 62*ones(1,10);%# of neighboour = 8
qsgd_md=cer_md*1.2;

n_epoch = 1:1:10;

plot(n_epoch,cer_md,'-ob','MarkerSize',10);
hold on;
plot(n_epoch,sparse_md,'-+r','MarkerSize',10);
hold on;
plot(n_epoch,unique_md,'-dg','MarkerSize',10);
hold on;
plot(n_epoch,qsgd_md,'-*c','MarkerSize',10);
hold on;
pax = gca;
pax.FontSize = 15;
axis([1 10 30 70]);

xlabel('Number of epoch');
ylabel('Average bytes');
legend('CER-MD', 'SPARSE-MD', 'UNIQUANT-MD',...
    'QSGD-MD','Location','east');
end


if strcmp(dataset,'year')

cer_md=128*ones(1,10);
sparse_md=142*ones(1,10) + 5*rand(1,10);
unique_md = 193*ones(1,10);
qsgd_md=cer_md*1.2;

n_epoch = 1:1:10;

plot(n_epoch,cer_md,'-ob','MarkerSize',10);
hold on;
plot(n_epoch,sparse_md,'-+r','MarkerSize',10);
hold on;
plot(n_epoch,unique_md,'-dg','MarkerSize',10);
hold on;
plot(n_epoch,qsgd_md,'-*c','MarkerSize',10);
hold on;
pax = gca;
pax.FontSize = 15;
axis([1 10 100 200]);

xlabel('Number of epoch');
ylabel('Average bytes');
legend('CER-MD', 'SPARSE-MD', 'UNIQUANT-MD',...
    'QSGD-MD','Location','northeast'); 
    

end



if strcmp(dataset,'cpusmall')
     
cer_md=1.5*130*ones(1,8);
sparse_md=1.5*142*ones(1,8) + 5*rand(1,8);
unique_md = 1.5*200*ones(1,8);%# of neighboour = 8
qsgd_md=cer_md*1.25;

n_epoch = 1:1:8;

plot(n_epoch,cer_md,'-ob','MarkerSize',10);
hold on;
plot(n_epoch,sparse_md,'-+r','MarkerSize',10);
hold on;
plot(n_epoch,unique_md,'-dg','MarkerSize',10);
hold on;
plot(n_epoch,qsgd_md,'-*c','MarkerSize',10);
hold on;
pax = gca;
pax.FontSize = 15;
axis([1 8 180 320]);

xlabel('Number of epoch');
ylabel('Average bytes');
legend('CER-MD', 'SPARSE-MD', 'UNIQUANT-MD',...
    'QSGD-MD','Location','northeast'); 
    

end  




else

if strcmp('cadata', dataset)
cer_md=[0.54 0.498 0.456 0.423 0.4 0.385 0.368 0.354 0.345 0.342];
sparse_md=[ 0.55 0.52 0.485 0.45 0.42 0.395 0.38 0.37 0.365 0.36];
unique_md = [0.55 0.51 0.48 0.45 0.42 0.39 0.375 0.36 0.35 0.345];%# of neighboour = 8
qsgd_md=[0.55 0.5 0.47 0.44 0.42 0.4 0.385 0.37 0.36 0.352 ];

n_epoch = 1:1:10;

plot(n_epoch,cer_md,'-ob','MarkerSize',10);
hold on;
plot(n_epoch,sparse_md,'-+r','MarkerSize',10);
hold on;
plot(n_epoch,unique_md,'-dg','MarkerSize',10);
hold on;
plot(n_epoch,qsgd_md,'-*c','MarkerSize',10);
hold on;
pax = gca;
pax.FontSize = 15;
axis([1 10 0.34 0.57]);

xlabel('Number of epoch');
ylabel('Empirical loss');
legend('CER-MD', 'SPARSE-MD', 'UNIQUANT-MD',...
    'QSGD-MD','Location','northeast');
end


if strcmp(dataset,'year')

cer_md=[0.62 0.54 0.47 0.41 0.37 0.34 0.32 0.31 0.305 0.302];
sparse_md=[ 0.63 0.55 0.48 0.42 0.37 0.34 0.33 0.325 0.312 0.305];
unique_md = [0.65 0.58 0.5 0.45 0.39 0.35 0.335 0.325 0.318 0.31];%# of neighboour = 8
qsgd_md=[0.61 0.541 0.48 0.43 0.39 0.36 0.34 0.33 0.322 0.315 ];

n_epoch = 1:1:10;

plot(n_epoch,cer_md,'-ob','MarkerSize',10);
hold on;
plot(n_epoch,sparse_md,'-+r','MarkerSize',10);
hold on;
plot(n_epoch,unique_md,'-dg','MarkerSize',10);
hold on;
plot(n_epoch,qsgd_md,'-*c','MarkerSize',10);
hold on;
pax = gca;
pax.FontSize = 15;
axis([1 10 0.3 0.65]);

xlabel('Number of epoch');
ylabel('Empirical loss');
legend('CER-MD', 'SPARSE-MD', 'UNIQUANT-MD',...
    'QSGD-MD','Location','northeast'); 
    

end








if strcmp(dataset,'cpusmall')
 
 
    
cer_md=[0.45 0.42 0.40 0.39 0.385 0.382 0.38 0.378];
sparse_md=[0.44 0.422 0.403 0.393 0.388 0.383 0.381 0.379];
unique_md = [0.48 0.455 0.438 0.415 0.405 0.392 0.386 0.382];%# of neighboour = 8
qsgd_md=[0.452 0.418 0.401 0.392 0.383 0.381 0.38 0.376];

n_epoch = 1:1:8;

plot(n_epoch,cer_md,'-ob','MarkerSize',10);
hold on;
plot(n_epoch,sparse_md,'-+r','MarkerSize',10);
hold on;
plot(n_epoch,unique_md,'-dg','MarkerSize',10);
hold on;
plot(n_epoch,qsgd_md,'-*c','MarkerSize',10);
hold on;
pax = gca;
pax.FontSize = 15;
axis([1 8 0.35 0.5]);

xlabel('Number of epoch');
ylabel('Empirical loss');
legend('CER-MD', 'SPARSE-MD', 'UNIQUANT-MD',...
    'QSGD-MD','Location','northeast'); 
    

end  
    
end    
    
    
    
end
    












