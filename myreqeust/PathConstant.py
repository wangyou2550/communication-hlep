class PathConstant:
    # DNS = "http://localhost:30504/"
    DNS = "http://39.105.200.100:30999/"
    HEAD_IMAGE_URL="http://39.105.200.100:30997/images/软件首页.png"
    # chapter
    GET_CHAPTER_LIST=DNS+"communication/chapter/list"
    GET_PAST_PAPER_LIST=DNS+"communication/chapter/pastpaper/list"
    GET_CHAPTER_BY_ID=DNS+"communication/chapter/{id}"
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
    QUERY_STEP=DNS+"communication/step/query"
    QUERY_STEP_PAGE=DNS+"communication/step/page"
    # 上传图片
    UPLOAD_IMAGE=DNS+"common/minio/upload"
    #新增知识点图片
    ADD_IMAGE=DNS+"communication/image"

    ADD_RELATION_STEP=DNS+"communication/relationStep"

    ADD_STEP_FEEDBACK_FAVORITE=DNS+"communication/stepFeedbackFavorite/insertAndUpdate"
    QUERY_PROBLEM_PAGE = DNS + "communication/step/page"


    '''
    问题相关api
    '''
    # QUERY_QUESTION_LIST=DNS+"communication/question/list?chapter="
    QUERY_QUESTION_LIST=DNS+"communication/question/list"
    ADD_QUESTION=DNS+"communication/question"
    QUERY_HINT=DNS+"communication/question/hint/"
    ADD_REL_SECTION=DNS+"communication/quetionRelSection"
    ADD_REL_STEP=DNS+"communication/relationQuestion"
    ADD_REL_QUESTION=DNS+"communication/quesRelQues"
    QUERY_SOLUTION=DNS+"communication/question/solution/"
    ADD_SOLUTION=DNS+"communication/question/solution"

    ADD_PROBLEM_FEEDBACK_FAVORITE=DNS+"communication/problemFeedbackFavorite"
    GET_PROBLEM_FEEDBACK_FAVORITE=DNS+"communication/problemFeedbackFavorite/"
    QUERY_PROBLEM_PAGE = DNS + "communication/problemFeedbackFavorite/page"

    '''
    登录有关的
    '''
    # 获取验证码
    GET_CAPTCHAIMAGE=DNS+"captchaImage"
    LOGIN=DNS+"login"
    GET_INFO=DNS+"getInfo"
    REGISTER=DNS+"regist"

