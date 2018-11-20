
% Multi variant gaussian parameters

mu_n = [0,0];
mu_p = [0,0];

sig_n = [1 0 ; 0 1];
sig_p = [2 0; 0 0.5];

rng default  % For reproducibility
nb_elem = 50000; % Number of elements for each gaussian 

N = mvnrnd(mu_n,sig_n,nb_elem);
P = mvnrnd(mu_p,sig_p,nb_elem);

figure
plot(N(:,1),N(:,2),'o')

figure 
plot (P(:,1),P(:,2),'+')

err = 0;

for i = 1:nb_elem
    if mvnpdf(N(i,:),mu_n,sig_n) < mvnpdf(N(i,:),mu_p,sig_p)
        err = err + 1;
    end
    if mvnpdf(P(i,:),mu_n,sig_n) > mvnpdf(P(i,:),mu_p,sig_p)
        err = err + 1;
    end
end

err = err/(nb_elem*2)
