// WARNING: This file was autogenerated by MBRS generator.
// Do not update it because if you run generator again you changes will be deleted

package ftn.backendservice.domain.mappers;

import org.mapstruct.*;
import org.mapstruct.factory.Mappers;

import java.util.List;

import ftn.backendservice.domain.dtos.TransactionDto;
import ftn.backendservice.domain.entities.*;


@Mapper(unmappedTargetPolicy = ReportingPolicy.IGNORE,
        nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)
public interface TransactionMapper {

    TransactionMapper INSTANCE = Mappers.getMapper(TransactionMapper.class);

    TransactionDto toDTO(Transaction transaction);

    List<TransactionDto> toDTO(List<Transaction> transaction);

}