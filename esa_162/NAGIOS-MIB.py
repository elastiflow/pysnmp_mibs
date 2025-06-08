# SNMP MIB module (NAGIOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/esa_162/NAGIOS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:16:25 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

esa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 162)
)
if mibBuilder.loadTexts:
    esa.setRevisions(
        ("2015-12-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SubSystemIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Esoc_ObjectIdentity = ObjectIdentity
esoc = _Esoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1)
)
_Nagios_ObjectIdentity = ObjectIdentity
nagios = _Nagios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 2)
)
_SubTable_Object = MibTable
subTable = _SubTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000)
)
if mibBuilder.loadTexts:
    subTable.setStatus("current")
_SubEntry_Object = MibTableRow
subEntry = _SubEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1)
)
subEntry.setIndexNames(
    (0, "NAGIOS-MIB", "subIndex"),
)
if mibBuilder.loadTexts:
    subEntry.setStatus("current")
_SubIndex_Type = SubSystemIndex
_SubIndex_Object = MibTableColumn
subIndex = _SubIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 1),
    _SubIndex_Type()
)
subIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subIndex.setStatus("current")


class _SubHostName_Type(DisplayString):
    """Custom type subHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubHostName_Type.__name__ = "DisplayString"
_SubHostName_Object = MibTableColumn
subHostName = _SubHostName_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 2),
    _SubHostName_Type()
)
subHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subHostName.setStatus("current")


class _SubStatus_Type(Integer32):
    """Custom type subStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )


_SubStatus_Type.__name__ = "Integer32"
_SubStatus_Object = MibTableColumn
subStatus = _SubStatus_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 3),
    _SubStatus_Type()
)
subStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subStatus.setStatus("current")


class _SubDownStatus_Type(Integer32):
    """Custom type subDownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("set", 1))
    )


_SubDownStatus_Type.__name__ = "Integer32"
_SubDownStatus_Object = MibTableColumn
subDownStatus = _SubDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 4),
    _SubDownStatus_Type()
)
subDownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDownStatus.setStatus("current")


class _SubDownInfo_Type(DisplayString):
    """Custom type subDownInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubDownInfo_Type.__name__ = "DisplayString"
_SubDownInfo_Object = MibTableColumn
subDownInfo = _SubDownInfo_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 5),
    _SubDownInfo_Type()
)
subDownInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subDownInfo.setStatus("current")


class _SubSerSumStatus_Type(Integer32):
    """Custom type subSerSumStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("warning", 1),
          ("critical", 2),
          ("unknown", 3),
          ("notimplemented", 4))
    )


_SubSerSumStatus_Type.__name__ = "Integer32"
_SubSerSumStatus_Object = MibTableColumn
subSerSumStatus = _SubSerSumStatus_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 6),
    _SubSerSumStatus_Type()
)
subSerSumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSerSumStatus.setStatus("current")


class _SubSerSumInfo_Type(DisplayString):
    """Custom type subSerSumInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubSerSumInfo_Type.__name__ = "DisplayString"
_SubSerSumInfo_Object = MibTableColumn
subSerSumInfo = _SubSerSumInfo_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1000, 1, 7),
    _SubSerSumInfo_Type()
)
subSerSumInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSerSumInfo.setStatus("current")
_SubConformance_ObjectIdentity = ObjectIdentity
subConformance = _SubConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1001)
)
_SubGroups_ObjectIdentity = ObjectIdentity
subGroups = _SubGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1001, 1)
)

# Managed Objects groups

subInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 162, 1, 2, 1001, 1, 1)
)
subInformationGroup.setObjects(
      *(("NAGIOS-MIB", "subIndex"),
        ("NAGIOS-MIB", "subHostName"),
        ("NAGIOS-MIB", "subStatus"),
        ("NAGIOS-MIB", "subDownStatus"),
        ("NAGIOS-MIB", "subDownInfo"),
        ("NAGIOS-MIB", "subSerSumStatus"),
        ("NAGIOS-MIB", "subSerSumInfo"))
)
if mibBuilder.loadTexts:
    subInformationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NAGIOS-MIB",
    **{"SubSystemIndex": SubSystemIndex,
       "esa": esa,
       "esoc": esoc,
       "nagios": nagios,
       "subTable": subTable,
       "subEntry": subEntry,
       "subIndex": subIndex,
       "subHostName": subHostName,
       "subStatus": subStatus,
       "subDownStatus": subDownStatus,
       "subDownInfo": subDownInfo,
       "subSerSumStatus": subSerSumStatus,
       "subSerSumInfo": subSerSumInfo,
       "subConformance": subConformance,
       "subGroups": subGroups,
       "subInformationGroup": subInformationGroup}
)
