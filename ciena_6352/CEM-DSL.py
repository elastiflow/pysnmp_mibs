# SNMP MIB module (CEM-DSL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-DSL.mib
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cnDslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 5)
)
if mibBuilder.loadTexts:
    cnDslMIB.setRevisions(
        ("2000-10-24 11:34",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnDslObjects_ObjectIdentity = ObjectIdentity
cnDslObjects = _CnDslObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1)
)
_CnDslInterfaceIdTable_Object = MibTable
cnDslInterfaceIdTable = _CnDslInterfaceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2)
)
if mibBuilder.loadTexts:
    cnDslInterfaceIdTable.setStatus("current")
_CnDslInterfaceIdEntry_Object = MibTableRow
cnDslInterfaceIdEntry = _CnDslInterfaceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2, 1)
)
cnDslInterfaceIdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnDslInterfaceIdEntry.setStatus("current")


class _CnDslInterfaceIdString1_Type(DisplayString):
    """Custom type cnDslInterfaceIdString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CnDslInterfaceIdString1_Type.__name__ = "DisplayString"
_CnDslInterfaceIdString1_Object = MibTableColumn
cnDslInterfaceIdString1 = _CnDslInterfaceIdString1_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2, 1, 1),
    _CnDslInterfaceIdString1_Type()
)
cnDslInterfaceIdString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslInterfaceIdString1.setStatus("current")


class _CnDslInterfaceIdString2_Type(DisplayString):
    """Custom type cnDslInterfaceIdString2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CnDslInterfaceIdString2_Type.__name__ = "DisplayString"
_CnDslInterfaceIdString2_Object = MibTableColumn
cnDslInterfaceIdString2 = _CnDslInterfaceIdString2_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2, 1, 2),
    _CnDslInterfaceIdString2_Type()
)
cnDslInterfaceIdString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslInterfaceIdString2.setStatus("current")


class _CnDslInterfaceIdString3_Type(DisplayString):
    """Custom type cnDslInterfaceIdString3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CnDslInterfaceIdString3_Type.__name__ = "DisplayString"
_CnDslInterfaceIdString3_Object = MibTableColumn
cnDslInterfaceIdString3 = _CnDslInterfaceIdString3_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2, 1, 3),
    _CnDslInterfaceIdString3_Type()
)
cnDslInterfaceIdString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslInterfaceIdString3.setStatus("current")


class _CnDslInterfaceIdString4_Type(DisplayString):
    """Custom type cnDslInterfaceIdString4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CnDslInterfaceIdString4_Type.__name__ = "DisplayString"
_CnDslInterfaceIdString4_Object = MibTableColumn
cnDslInterfaceIdString4 = _CnDslInterfaceIdString4_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2, 1, 4),
    _CnDslInterfaceIdString4_Type()
)
cnDslInterfaceIdString4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslInterfaceIdString4.setStatus("current")


class _CnDslInterfaceIdString5_Type(DisplayString):
    """Custom type cnDslInterfaceIdString5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CnDslInterfaceIdString5_Type.__name__ = "DisplayString"
_CnDslInterfaceIdString5_Object = MibTableColumn
cnDslInterfaceIdString5 = _CnDslInterfaceIdString5_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 2, 1, 5),
    _CnDslInterfaceIdString5_Type()
)
cnDslInterfaceIdString5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslInterfaceIdString5.setStatus("current")
_CnDslInterfaceConfTable_Object = MibTable
cnDslInterfaceConfTable = _CnDslInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3)
)
if mibBuilder.loadTexts:
    cnDslInterfaceConfTable.setStatus("current")
_CnDslInterfaceConfEntry_Object = MibTableRow
cnDslInterfaceConfEntry = _CnDslInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1)
)
cnDslInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnDslInterfaceConfEntry.setStatus("current")


class _CnDslEnableAlarms_Type(Integer32):
    """Custom type cnDslEnableAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CnDslEnableAlarms_Type.__name__ = "Integer32"
_CnDslEnableAlarms_Object = MibTableColumn
cnDslEnableAlarms = _CnDslEnableAlarms_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 1),
    _CnDslEnableAlarms_Type()
)
cnDslEnableAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslEnableAlarms.setStatus("current")


class _CnDslEnableBitSwapping_Type(Integer32):
    """Custom type cnDslEnableBitSwapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CnDslEnableBitSwapping_Type.__name__ = "Integer32"
_CnDslEnableBitSwapping_Object = MibTableColumn
cnDslEnableBitSwapping = _CnDslEnableBitSwapping_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 2),
    _CnDslEnableBitSwapping_Type()
)
cnDslEnableBitSwapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslEnableBitSwapping.setStatus("current")
_CnDslFastChanIfIndex_Type = Integer32
_CnDslFastChanIfIndex_Object = MibTableColumn
cnDslFastChanIfIndex = _CnDslFastChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 3),
    _CnDslFastChanIfIndex_Type()
)
cnDslFastChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDslFastChanIfIndex.setStatus("current")
_CnDslInterleavedChanIfIndex_Type = Integer32
_CnDslInterleavedChanIfIndex_Object = MibTableColumn
cnDslInterleavedChanIfIndex = _CnDslInterleavedChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 4),
    _CnDslInterleavedChanIfIndex_Type()
)
cnDslInterleavedChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDslInterleavedChanIfIndex.setStatus("current")


class _CnDslChannelType_Type(Integer32):
    """Custom type cnDslChannelType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noChannel", 1),
          ("fast", 2),
          ("interleaved", 3),
          ("fastAndInterleaved", 4))
    )


_CnDslChannelType_Type.__name__ = "Integer32"
_CnDslChannelType_Object = MibTableColumn
cnDslChannelType = _CnDslChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 5),
    _CnDslChannelType_Type()
)
cnDslChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslChannelType.setStatus("current")


class _CnDslG992dot1Mode_Type(Integer32):
    """Custom type cnDslG992dot1Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_CnDslG992dot1Mode_Type.__name__ = "Integer32"
_CnDslG992dot1Mode_Object = MibTableColumn
cnDslG992dot1Mode = _CnDslG992dot1Mode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 6),
    _CnDslG992dot1Mode_Type()
)
cnDslG992dot1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslG992dot1Mode.setStatus("current")


class _CnDslG992dot2Mode_Type(Integer32):
    """Custom type cnDslG992dot2Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_CnDslG992dot2Mode_Type.__name__ = "Integer32"
_CnDslG992dot2Mode_Object = MibTableColumn
cnDslG992dot2Mode = _CnDslG992dot2Mode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 7),
    _CnDslG992dot2Mode_Type()
)
cnDslG992dot2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslG992dot2Mode.setStatus("current")


class _CnDslT1dot413Mode_Type(Integer32):
    """Custom type cnDslT1dot413Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_CnDslT1dot413Mode_Type.__name__ = "Integer32"
_CnDslT1dot413Mode_Object = MibTableColumn
cnDslT1dot413Mode = _CnDslT1dot413Mode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 8),
    _CnDslT1dot413Mode_Type()
)
cnDslT1dot413Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDslT1dot413Mode.setStatus("current")


class _CnDslCurrentMode_Type(Integer32):
    """Custom type cnDslCurrentMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cnDslG992dot1", 1),
          ("cnDslG992dot2", 2),
          ("cnDslT1dot413", 3),
          ("unknown", 4))
    )


_CnDslCurrentMode_Type.__name__ = "Integer32"
_CnDslCurrentMode_Object = MibTableColumn
cnDslCurrentMode = _CnDslCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 9),
    _CnDslCurrentMode_Type()
)
cnDslCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDslCurrentMode.setStatus("current")


class _CnDslLineStatus_Type(Integer32):
    """Custom type cnDslLineStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dslLineUp", 1),
          ("dslLineDown", 2))
    )


_CnDslLineStatus_Type.__name__ = "Integer32"
_CnDslLineStatus_Object = MibTableColumn
cnDslLineStatus = _CnDslLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 10),
    _CnDslLineStatus_Type()
)
cnDslLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDslLineStatus.setStatus("current")
_CnDslLineStatusLastChange_Type = TimeStamp
_CnDslLineStatusLastChange_Object = MibTableColumn
cnDslLineStatusLastChange = _CnDslLineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 3, 1, 11),
    _CnDslLineStatusLastChange_Type()
)
cnDslLineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnDslLineStatusLastChange.setStatus("current")
_CnDslModuleConformance_ObjectIdentity = ObjectIdentity
cnDslModuleConformance = _CnDslModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 4)
)
_CnDslGroups_ObjectIdentity = ObjectIdentity
cnDslGroups = _CnDslGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 4, 1)
)
_CnDslTraps_ObjectIdentity = ObjectIdentity
cnDslTraps = _CnDslTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 5)
)

# Managed Objects groups

cnDslCNX5ObjectGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 4, 1, 1)
)
cnDslCNX5ObjectGroups.setObjects(
      *(("CEM-DSL", "cnDslInterfaceIdString5"),
        ("CEM-DSL", "cnDslInterfaceIdString4"),
        ("CEM-DSL", "cnDslInterfaceIdString3"),
        ("CEM-DSL", "cnDslInterfaceIdString2"),
        ("CEM-DSL", "cnDslInterfaceIdString1"),
        ("CEM-DSL", "cnDslEnableAlarms"),
        ("CEM-DSL", "cnDslEnableBitSwapping"),
        ("CEM-DSL", "cnDslFastChanIfIndex"),
        ("CEM-DSL", "cnDslInterleavedChanIfIndex"),
        ("CEM-DSL", "cnDslChannelType"),
        ("CEM-DSL", "cnDslG992dot1Mode"),
        ("CEM-DSL", "cnDslG992dot2Mode"),
        ("CEM-DSL", "cnDslT1dot413Mode"))
)
if mibBuilder.loadTexts:
    cnDslCNX5ObjectGroups.setStatus("current")

cnDslCN1K5ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 4, 1, 2)
)
cnDslCN1K5ObjectGroup.setObjects(
      *(("CEM-DSL", "cnDslInterfaceIdString5"),
        ("CEM-DSL", "cnDslInterfaceIdString4"),
        ("CEM-DSL", "cnDslInterfaceIdString3"),
        ("CEM-DSL", "cnDslInterfaceIdString2"),
        ("CEM-DSL", "cnDslInterfaceIdString1"),
        ("CEM-DSL", "cnDslEnableAlarms"),
        ("CEM-DSL", "cnDslEnableBitSwapping"),
        ("CEM-DSL", "cnDslFastChanIfIndex"),
        ("CEM-DSL", "cnDslInterleavedChanIfIndex"),
        ("CEM-DSL", "cnDslChannelType"),
        ("CEM-DSL", "cnDslG992dot1Mode"),
        ("CEM-DSL", "cnDslG992dot2Mode"),
        ("CEM-DSL", "cnDslT1dot413Mode"))
)
if mibBuilder.loadTexts:
    cnDslCN1K5ObjectGroup.setStatus("current")


# Notification objects

cnDslLineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 5, 1, 5, 0, 1)
)
cnDslLineStatusChange.setObjects(
      *(("CEM-DSL", "cnDslLineStatus"),
        ("CEM-DSL", "cnDslLineStatusLastChange"))
)
if mibBuilder.loadTexts:
    cnDslLineStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-DSL",
    **{"cnDslMIB": cnDslMIB,
       "cnDslObjects": cnDslObjects,
       "cnDslInterfaceIdTable": cnDslInterfaceIdTable,
       "cnDslInterfaceIdEntry": cnDslInterfaceIdEntry,
       "cnDslInterfaceIdString1": cnDslInterfaceIdString1,
       "cnDslInterfaceIdString2": cnDslInterfaceIdString2,
       "cnDslInterfaceIdString3": cnDslInterfaceIdString3,
       "cnDslInterfaceIdString4": cnDslInterfaceIdString4,
       "cnDslInterfaceIdString5": cnDslInterfaceIdString5,
       "cnDslInterfaceConfTable": cnDslInterfaceConfTable,
       "cnDslInterfaceConfEntry": cnDslInterfaceConfEntry,
       "cnDslEnableAlarms": cnDslEnableAlarms,
       "cnDslEnableBitSwapping": cnDslEnableBitSwapping,
       "cnDslFastChanIfIndex": cnDslFastChanIfIndex,
       "cnDslInterleavedChanIfIndex": cnDslInterleavedChanIfIndex,
       "cnDslChannelType": cnDslChannelType,
       "cnDslG992dot1Mode": cnDslG992dot1Mode,
       "cnDslG992dot2Mode": cnDslG992dot2Mode,
       "cnDslT1dot413Mode": cnDslT1dot413Mode,
       "cnDslCurrentMode": cnDslCurrentMode,
       "cnDslLineStatus": cnDslLineStatus,
       "cnDslLineStatusLastChange": cnDslLineStatusLastChange,
       "cnDslModuleConformance": cnDslModuleConformance,
       "cnDslGroups": cnDslGroups,
       "cnDslCNX5ObjectGroups": cnDslCNX5ObjectGroups,
       "cnDslCN1K5ObjectGroup": cnDslCN1K5ObjectGroup,
       "cnDslTraps": cnDslTraps,
       "cnDslLineStatusChange": cnDslLineStatusChange}
)
