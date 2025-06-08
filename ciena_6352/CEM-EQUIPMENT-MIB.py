# SNMP MIB module (CEM-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-EQUIPMENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cemEquipmentModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 23)
)
if mibBuilder.loadTexts:
    cemEquipmentModule.setRevisions(
        ("2002-04-24 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CemEquipmentTypeIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("tALKBATSHELF1a", 1),
          ("tALKBATSHELF1b", 2),
          ("tALKBATSHELF2a", 3),
          ("tALKBATSHELF2b", 4),
          ("tALKBATSHELF3a", 5),
          ("tALKBATSHELF3b", 6),
          ("tALKBATSHELF4a", 7),
          ("tALKBATSHELF4b", 8),
          ("tALKBATSHELF5a", 9),
          ("tALKBATSHELF5b", 10),
          ("sPECIALSHELF1", 11),
          ("sPECIALSHELF2", 12),
          ("sPECIALSHELF3", 13),
          ("sPECIALSHELF4", 14),
          ("fANTRAY1", 15),
          ("fANTRAY2", 16),
          ("fANINTRAYONE1", 17),
          ("fANINTRAYONE2", 18),
          ("fANINTRAYONE3", 19),
          ("fANINTRAYTWO1", 20),
          ("fANINTRAYTWO2", 21),
          ("fANINTRAYTWO3", 22),
          ("aLARMCARD", 23),
          ("tESTCARD", 24))
    )



# MIB Managed Objects in the order of their OIDs

_CemEquipmentMIB_ObjectIdentity = ObjectIdentity
cemEquipmentMIB = _CemEquipmentMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1)
)
if mibBuilder.loadTexts:
    cemEquipmentMIB.setStatus("current")
_CemMiscellaneousEquipmentTable_Object = MibTable
cemMiscellaneousEquipmentTable = _CemMiscellaneousEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1)
)
if mibBuilder.loadTexts:
    cemMiscellaneousEquipmentTable.setStatus("current")
_CemMiscellaneousEquipmentEntry_Object = MibTableRow
cemMiscellaneousEquipmentEntry = _CemMiscellaneousEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1, 1)
)
cemMiscellaneousEquipmentEntry.setIndexNames(
    (0, "CEM-EQUIPMENT-MIB", "cemEquipmentTypeIndex"),
)
if mibBuilder.loadTexts:
    cemMiscellaneousEquipmentEntry.setStatus("current")


class _CemEquipmentTypeIndex_Type(CemEquipmentTypeIndex):
    """Custom type cemEquipmentTypeIndex based on CemEquipmentTypeIndex"""
    subtypeSpec = CemEquipmentTypeIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CemEquipmentTypeIndex_Type.__name__ = "CemEquipmentTypeIndex"
_CemEquipmentTypeIndex_Object = MibTableColumn
cemEquipmentTypeIndex = _CemEquipmentTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1, 1, 2),
    _CemEquipmentTypeIndex_Type()
)
cemEquipmentTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemEquipmentTypeIndex.setStatus("current")


class _CemMiscellaneousEquipmentDescription_Type(OctetString):
    """Custom type cemMiscellaneousEquipmentDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_CemMiscellaneousEquipmentDescription_Type.__name__ = "OctetString"
_CemMiscellaneousEquipmentDescription_Object = MibTableColumn
cemMiscellaneousEquipmentDescription = _CemMiscellaneousEquipmentDescription_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1, 1, 3),
    _CemMiscellaneousEquipmentDescription_Type()
)
cemMiscellaneousEquipmentDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemMiscellaneousEquipmentDescription.setStatus("current")


class _CemMiscellaneousEquipmentPSC_Type(OctetString):
    """Custom type cemMiscellaneousEquipmentPSC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CemMiscellaneousEquipmentPSC_Type.__name__ = "OctetString"
_CemMiscellaneousEquipmentPSC_Object = MibTableColumn
cemMiscellaneousEquipmentPSC = _CemMiscellaneousEquipmentPSC_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1, 1, 4),
    _CemMiscellaneousEquipmentPSC_Type()
)
cemMiscellaneousEquipmentPSC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemMiscellaneousEquipmentPSC.setStatus("current")


class _CemMiscellaneousEquipmentCLEI_Type(OctetString):
    """Custom type cemMiscellaneousEquipmentCLEI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CemMiscellaneousEquipmentCLEI_Type.__name__ = "OctetString"
_CemMiscellaneousEquipmentCLEI_Object = MibTableColumn
cemMiscellaneousEquipmentCLEI = _CemMiscellaneousEquipmentCLEI_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1, 1, 5),
    _CemMiscellaneousEquipmentCLEI_Type()
)
cemMiscellaneousEquipmentCLEI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemMiscellaneousEquipmentCLEI.setStatus("current")
_CemEquipmentRowStatus_Type = RowStatus
_CemEquipmentRowStatus_Object = MibTableColumn
cemEquipmentRowStatus = _CemEquipmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 1, 1, 6),
    _CemEquipmentRowStatus_Type()
)
cemEquipmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemEquipmentRowStatus.setStatus("current")
_CemEquipmentGroups_ObjectIdentity = ObjectIdentity
cemEquipmentGroups = _CemEquipmentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 5)
)
if mibBuilder.loadTexts:
    cemEquipmentGroups.setStatus("current")
_CemEquipmentConformance_ObjectIdentity = ObjectIdentity
cemEquipmentConformance = _CemEquipmentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 6)
)
if mibBuilder.loadTexts:
    cemEquipmentConformance.setStatus("current")

# Managed Objects groups

cemMiscellaneousEquipmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 5, 1)
)
cemMiscellaneousEquipmentGroup.setObjects(
      *(("CEM-EQUIPMENT-MIB", "cemEquipmentRowStatus"),
        ("CEM-EQUIPMENT-MIB", "cemMiscellaneousEquipmentCLEI"),
        ("CEM-EQUIPMENT-MIB", "cemMiscellaneousEquipmentPSC"),
        ("CEM-EQUIPMENT-MIB", "cemMiscellaneousEquipmentDescription"))
)
if mibBuilder.loadTexts:
    cemMiscellaneousEquipmentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cemEquipmentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 23, 1, 6, 1)
)
cemEquipmentCompliance.setObjects(
    ("CEM-EQUIPMENT-MIB", "cemMiscellaneousEquipmentGroup")
)
if mibBuilder.loadTexts:
    cemEquipmentCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-EQUIPMENT-MIB",
    **{"CemEquipmentTypeIndex": CemEquipmentTypeIndex,
       "cemEquipmentModule": cemEquipmentModule,
       "cemEquipmentMIB": cemEquipmentMIB,
       "cemMiscellaneousEquipmentTable": cemMiscellaneousEquipmentTable,
       "cemMiscellaneousEquipmentEntry": cemMiscellaneousEquipmentEntry,
       "cemEquipmentTypeIndex": cemEquipmentTypeIndex,
       "cemMiscellaneousEquipmentDescription": cemMiscellaneousEquipmentDescription,
       "cemMiscellaneousEquipmentPSC": cemMiscellaneousEquipmentPSC,
       "cemMiscellaneousEquipmentCLEI": cemMiscellaneousEquipmentCLEI,
       "cemEquipmentRowStatus": cemEquipmentRowStatus,
       "cemEquipmentGroups": cemEquipmentGroups,
       "cemMiscellaneousEquipmentGroup": cemMiscellaneousEquipmentGroup,
       "cemEquipmentConformance": cemEquipmentConformance,
       "cemEquipmentCompliance": cemEquipmentCompliance}
)
