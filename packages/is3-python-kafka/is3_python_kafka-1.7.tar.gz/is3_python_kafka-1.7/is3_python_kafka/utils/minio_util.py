from is3_python_kafka.domain.data_dto import DataEntity
from is3_python_kafka.minio.MinioComponent import MinioComponent

'''文件上传，返回的文件带有过期时间'''
"""
    Args:
        dataDto(DataEntity):实现方法数据体
        bucketName (str): 桶名称.
        filePath (str): 目标文件路径."""


def upload_file_with_expire(dataDto: DataEntity, bucketName, filePath):
    minioClient = MinioComponent(dataDto.minioEndpoint, dataDto.minioAccessKey, dataDto.minioSecretKey)
    return minioClient.upload_file_with_expire(bucketName, filePath)


'''文件上传'''
"""
    Args:
        dataDto(DataEntity):实现方法数据体
        bucketName (str): 桶名称.
        filePath (str): 目标文件路径."""


def upload_file(dataDto: DataEntity, bucketName, filePath):
    minioClient = MinioComponent(dataDto.minioEndpoint, dataDto.minioAccessKey, dataDto.minioSecretKey)
    return minioClient.upload_file(bucketName, filePath)
