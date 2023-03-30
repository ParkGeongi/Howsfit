import os


def get_densepose(model_fname):
    print("\nGet Densepose image\n")
    terminnal_command = "python apply_net.py show " \
                        "configs/densepose_rcnn_R_50_FPN_s1x.yaml " \
                        "https://dl.fbaipublicfiles.com/densepose" \
                        "/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl " \
                        f"../data/test/image/{model_fname} " \
                        f"dp_segm -v --opts MODEL.DEVICE cpu"
    os.system(terminnal_command)


if __name__ == '__main__':
    model_fname = "image_picker_4D0EBEDB-D6ED-4395-BC7E-41D540041548-10365-0000002AC1923233.jpg"
    get_densepose(model_fname)
