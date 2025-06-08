# SNMP MIB module (CISCO-MGX82XX-MODULE-RSRC-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MGX82XX-MODULE-RSRC-PART-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:02 2025
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

(cardGeneric,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardGeneric")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoMgx82xxModuleRsrcPartMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 73)
)
if mibBuilder.loadTexts:
    ciscoMgx82xxModuleRsrcPartMIB.setRevisions(
        ("2003-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CardResourcePartition_ObjectIdentity = ObjectIdentity
cardResourcePartition = _CardResourcePartition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9)
)


class _CardLcnPartitionType_Type(Integer32):
    """Custom type cardLcnPartitionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPartition", 1),
          ("controllerBased", 2),
          ("portControllerBased", 3))
    )


_CardLcnPartitionType_Type.__name__ = "Integer32"
_CardLcnPartitionType_Object = MibScalar
cardLcnPartitionType = _CardLcnPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 1),
    _CardLcnPartitionType_Type()
)
cardLcnPartitionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardLcnPartitionType.setStatus("current")
_CardResPartGrpTable_Object = MibTable
cardResPartGrpTable = _CardResPartGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2)
)
if mibBuilder.loadTexts:
    cardResPartGrpTable.setStatus("current")
_CardResPartGrpEntry_Object = MibTableRow
cardResPartGrpEntry = _CardResPartGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1)
)
cardResPartGrpEntry.setIndexNames(
    (0, "CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"),
)
if mibBuilder.loadTexts:
    cardResPartGrpEntry.setStatus("current")


class _CardResPartCtrlrNum_Type(Integer32):
    """Custom type cardResPartCtrlrNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("par", 1),
          ("pnni", 2),
          ("tag", 3))
    )


_CardResPartCtrlrNum_Type.__name__ = "Integer32"
_CardResPartCtrlrNum_Object = MibTableColumn
cardResPartCtrlrNum = _CardResPartCtrlrNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 1),
    _CardResPartCtrlrNum_Type()
)
cardResPartCtrlrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardResPartCtrlrNum.setStatus("current")


class _CardResPartRowStatus_Type(Integer32):
    """Custom type cardResPartRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_CardResPartRowStatus_Type.__name__ = "Integer32"
_CardResPartRowStatus_Object = MibTableColumn
cardResPartRowStatus = _CardResPartRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 2),
    _CardResPartRowStatus_Type()
)
cardResPartRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardResPartRowStatus.setStatus("current")


class _CardResPartNumOfLcnAvail_Type(Integer32):
    """Custom type cardResPartNumOfLcnAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CardResPartNumOfLcnAvail_Type.__name__ = "Integer32"
_CardResPartNumOfLcnAvail_Object = MibTableColumn
cardResPartNumOfLcnAvail = _CardResPartNumOfLcnAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 9, 2, 1, 3),
    _CardResPartNumOfLcnAvail_Type()
)
cardResPartNumOfLcnAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardResPartNumOfLcnAvail.setStatus("current")
_CmmRsrcPartMIBConformance_ObjectIdentity = ObjectIdentity
cmmRsrcPartMIBConformance = _CmmRsrcPartMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 73, 2)
)
_CmmRsrcPartMIBCompliances_ObjectIdentity = ObjectIdentity
cmmRsrcPartMIBCompliances = _CmmRsrcPartMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1)
)
_CmmRsrcPartMIBGroups_ObjectIdentity = ObjectIdentity
cmmRsrcPartMIBGroups = _CmmRsrcPartMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2)
)

# Managed Objects groups

cmmRsrcPartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 2, 1)
)
cmmRsrcPartGroup.setObjects(
      *(("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardLcnPartitionType"),
        ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartCtrlrNum"),
        ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartRowStatus"),
        ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cardResPartNumOfLcnAvail"))
)
if mibBuilder.loadTexts:
    cmmRsrcPartGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmmRsrcPartCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 73, 2, 1, 1)
)
cmmRsrcPartCompliance.setObjects(
    ("CISCO-MGX82XX-MODULE-RSRC-PART-MIB", "cmmRsrcPartGroup")
)
if mibBuilder.loadTexts:
    cmmRsrcPartCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-MODULE-RSRC-PART-MIB",
    **{"cardResourcePartition": cardResourcePartition,
       "cardLcnPartitionType": cardLcnPartitionType,
       "cardResPartGrpTable": cardResPartGrpTable,
       "cardResPartGrpEntry": cardResPartGrpEntry,
       "cardResPartCtrlrNum": cardResPartCtrlrNum,
       "cardResPartRowStatus": cardResPartRowStatus,
       "cardResPartNumOfLcnAvail": cardResPartNumOfLcnAvail,
       "ciscoMgx82xxModuleRsrcPartMIB": ciscoMgx82xxModuleRsrcPartMIB,
       "cmmRsrcPartMIBConformance": cmmRsrcPartMIBConformance,
       "cmmRsrcPartMIBCompliances": cmmRsrcPartMIBCompliances,
       "cmmRsrcPartCompliance": cmmRsrcPartCompliance,
       "cmmRsrcPartMIBGroups": cmmRsrcPartMIBGroups,
       "cmmRsrcPartGroup": cmmRsrcPartGroup}
)
