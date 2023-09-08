class PathConstant:
    DNS = "http://localhost:8080/"
    # chapter
    GET_CHAPTER_LIST=DNS+"communication/chapter/list"
    GET_CHAPTER_SIMPLE_LIST=DNS+"communication/chapter/simple/list"
    # section
    GET_SECTION_CHILD=DNS+"communication/section/child/"
    # 新增节点
    ADD_SECTION=DNS+"communication/section"
    GET_SECTION=DNS+"communication/section"
    GET_SECTION_BY_CHAPTERID=DNS+"communication/section/chapter"
    # 删除节点
    DELETE_SECTION=DNS+"communication/section"


    # 步骤
    ADD_STEP=DNS+"communication/step"
    GET_STEP=DNS+"communication/step"
    # 上传图片
    UPLOAD_IMAGE=DNS+"common/minio/upload"
    #新增知识点图片
    ADD_IMAGE=DNS+"communication/image"

    ADD_RELATION_STEP=DNS+"communication/relationStep"