import numpy as np
import asgl
import time
from sklearn.datasets import make_regression

# Import test data #
x, y = make_regression(n_samples=200, n_features=30, random_state=42)
group_index = np.random.randint(1, 6, 30)

def equal_array(array0, array1, tol=1e-6):
    n0 = array0.shape[0]
    n1 = array1.shape[0]
    if n0 != n1:
        f'Shapes do not match. Received: {n0} and {n1}'
    else:
        dif = array0 - array1
        if np.abs(np.mean(dif)) > tol:
            f'Arrays are not equal. Mean difference is {np.mean(dif)}'


if __name__ == '__main__':
    start_time = time.time()
    # UNPENALIZED TEST
    tvt_class = asgl.TVT(model='lm', penalization=None, error_type='MSE', random_state=2, train_pct=0.7,
                         validate_pct=0.1)
    cv1 = tvt_class.train_validate_test(x, y, group_index)
    cv2 = tvt_class.train_validate_test(x, y, group_index)
    equal_array(cv1.get('optimal_betas'), cv2.get('optimal_betas'))

    # LASSO penalization
    tvt_class = asgl.TVT(model='qr', penalization='lasso', lambda1=[0.01, 0.1, 1, 10], parallel=True, tau=0.5,
                         error_type='QRE', random_state=1, train_pct=0.3, validate_pct=0.6)
    tvt_class.train_validate_test(x, y, group_index)

    # Group LASSO
    tvt_class = asgl.TVT(model='lm', penalization='gl', lambda1=[0.01, 0.1, 1, 10], parallel=True,
                         error_type='MAE', random_state=2, train_pct=0.1, validate_pct=0.1)
    tvt_class.train_validate_test(x, y, group_index)

    # Sparse Group LASSO
    tvt_class = asgl.TVT(model='qr', penalization='sgl', lambda1=[0.01, 0.1, 1, 10], parallel=True, tau=0.02,
                         error_type='QRE', random_state=3, alpha=[0.1, 0.5, 0.9], train_pct=0.7, validate_pct=0.1)
    tvt_class.train_validate_test(x, y, group_index)

    print(f'Entering adaptive formulations.  Execution time: {time.time() - start_time}')

    # Adaptive sparse group lasso
    tvt_class = asgl.TVT(model='qr', penalization='asgl', lambda1=[0.01, 0.1, 1, 10], tau=0.5,
                         alpha=[0.1, 0.5, 0.9], parallel=True, num_cores=3, weight_technique='pca_1',
                         lasso_power_weight=[0.8, 1, 1.2], gl_power_weight=[0.8, 1, 1.2], variability_pct=0.7,
                         error_type='QRE', random_state=99, train_size=100, validate_size=50)
    tvt_class.train_validate_test(x, y, group_index)

    tvt_class = asgl.TVT(model='qr', penalization='asgl', lambda1=[0.01, 0.1, 1, 10], tau=0.5,
                         alpha=[0.1, 0.5, 0.9], parallel=True, num_cores=3, weight_technique='pls_1',
                         lasso_power_weight=[0.8, 1, 1.2], gl_power_weight=[0.8, 1, 1.2], variability_pct=0.7,
                         error_type='QRE', random_state=99, train_size=50, validate_size=50)
    tvt_class.train_validate_test(x, y, group_index)

    tvt_class = asgl.TVT(model='qr', penalization='asgl', lambda1=[0.01, 0.1, 1, 10], tau=0.5,
                         alpha=[0.1, 0.5, 0.9], parallel=True, num_cores=3, weight_technique='sparse_pca',
                         lasso_power_weight=[0.8, 1, 1.2], gl_power_weight=[0.8, 1, 1.2], variability_pct=0.7,
                         error_type='QRE', random_state=99, spca_alpha=1e-1, spca_ridge_alpha=1e-5,
                         train_size=120, validate_size=70)
    tvt_class.train_validate_test(x, y, group_index)

    print(f'Finished with no error. Execution time: {time.time() - start_time}')
