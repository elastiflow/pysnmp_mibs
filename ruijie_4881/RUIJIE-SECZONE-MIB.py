# SNMP MIB module (RUIJIE-SECZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SECZONE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:10 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus")

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

ruijieSecZoneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54)
)
if mibBuilder.loadTexts:
    ruijieSecZoneMIB.setRevisions(
        ("2009-08-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSecZoneMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSecZoneMIBObjects = _RuijieSecZoneMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1)
)
_RuijieSecZoneChainTable_Object = MibTable
ruijieSecZoneChainTable = _RuijieSecZoneChainTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieSecZoneChainTable.setStatus("current")
_RuijieSecZoneChainEntry_Object = MibTableRow
ruijieSecZoneChainEntry = _RuijieSecZoneChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1)
)
ruijieSecZoneChainEntry.setIndexNames(
    (0, "RUIJIE-SECZONE-MIB", "ruijieSecZoneChainName"),
)
if mibBuilder.loadTexts:
    ruijieSecZoneChainEntry.setStatus("current")


class _RuijieSecZoneChainName_Type(DisplayString):
    """Custom type ruijieSecZoneChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSecZoneChainName_Type.__name__ = "DisplayString"
_RuijieSecZoneChainName_Object = MibTableColumn
ruijieSecZoneChainName = _RuijieSecZoneChainName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 1),
    _RuijieSecZoneChainName_Type()
)
ruijieSecZoneChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecZoneChainName.setStatus("current")


class _RuijieSecZoneLevel_Type(Integer32):
    """Custom type ruijieSecZoneLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieSecZoneLevel_Type.__name__ = "Integer32"
_RuijieSecZoneLevel_Object = MibTableColumn
ruijieSecZoneLevel = _RuijieSecZoneLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 2),
    _RuijieSecZoneLevel_Type()
)
ruijieSecZoneLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneLevel.setStatus("current")


class _RuijieSecZoneAclName_Type(DisplayString):
    """Custom type ruijieSecZoneAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSecZoneAclName_Type.__name__ = "DisplayString"
_RuijieSecZoneAclName_Object = MibTableColumn
ruijieSecZoneAclName = _RuijieSecZoneAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 3),
    _RuijieSecZoneAclName_Type()
)
ruijieSecZoneAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneAclName.setStatus("current")


class _RuijieSecZoneViolationNotifyThresh_Type(Integer32):
    """Custom type ruijieSecZoneViolationNotifyThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSecZoneViolationNotifyThresh_Type.__name__ = "Integer32"
_RuijieSecZoneViolationNotifyThresh_Object = MibTableColumn
ruijieSecZoneViolationNotifyThresh = _RuijieSecZoneViolationNotifyThresh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 4),
    _RuijieSecZoneViolationNotifyThresh_Type()
)
ruijieSecZoneViolationNotifyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationNotifyThresh.setStatus("current")


class _RuijieSecZoneViolationNotifyAction_Type(Integer32):
    """Custom type ruijieSecZoneViolationNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_RuijieSecZoneViolationNotifyAction_Type.__name__ = "Integer32"
_RuijieSecZoneViolationNotifyAction_Object = MibTableColumn
ruijieSecZoneViolationNotifyAction = _RuijieSecZoneViolationNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 5),
    _RuijieSecZoneViolationNotifyAction_Type()
)
ruijieSecZoneViolationNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationNotifyAction.setStatus("current")


class _RuijieSecZoneViolationBlockThresh_Type(Integer32):
    """Custom type ruijieSecZoneViolationBlockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSecZoneViolationBlockThresh_Type.__name__ = "Integer32"
_RuijieSecZoneViolationBlockThresh_Object = MibTableColumn
ruijieSecZoneViolationBlockThresh = _RuijieSecZoneViolationBlockThresh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 6),
    _RuijieSecZoneViolationBlockThresh_Type()
)
ruijieSecZoneViolationBlockThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationBlockThresh.setStatus("current")


class _RuijieSecZoneViolationBlockAction_Type(Integer32):
    """Custom type ruijieSecZoneViolationBlockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_RuijieSecZoneViolationBlockAction_Type.__name__ = "Integer32"
_RuijieSecZoneViolationBlockAction_Object = MibTableColumn
ruijieSecZoneViolationBlockAction = _RuijieSecZoneViolationBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 7),
    _RuijieSecZoneViolationBlockAction_Type()
)
ruijieSecZoneViolationBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationBlockAction.setStatus("current")


class _RuijieSecZoneViolationBlockTimeout_Type(Integer32):
    """Custom type ruijieSecZoneViolationBlockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuijieSecZoneViolationBlockTimeout_Type.__name__ = "Integer32"
_RuijieSecZoneViolationBlockTimeout_Object = MibTableColumn
ruijieSecZoneViolationBlockTimeout = _RuijieSecZoneViolationBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 8),
    _RuijieSecZoneViolationBlockTimeout_Type()
)
ruijieSecZoneViolationBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationBlockTimeout.setStatus("current")
_RuijieSecZoneChainEntryStatus_Type = RowStatus
_RuijieSecZoneChainEntryStatus_Object = MibTableColumn
ruijieSecZoneChainEntryStatus = _RuijieSecZoneChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 1, 1, 9),
    _RuijieSecZoneChainEntryStatus_Type()
)
ruijieSecZoneChainEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieSecZoneChainEntryStatus.setStatus("current")
_RuijieSecZone2ZoneTable_Object = MibTable
ruijieSecZone2ZoneTable = _RuijieSecZone2ZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieSecZone2ZoneTable.setStatus("current")
_RuijieSecZone2ZoneEntry_Object = MibTableRow
ruijieSecZone2ZoneEntry = _RuijieSecZone2ZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 2, 1)
)
ruijieSecZone2ZoneEntry.setIndexNames(
    (0, "RUIJIE-SECZONE-MIB", "ruijieZoneFirstName"),
    (0, "RUIJIE-SECZONE-MIB", "ruijieZoneSecondName"),
    (0, "RUIJIE-SECZONE-MIB", "ruijieZone2ZoneAclName"),
)
if mibBuilder.loadTexts:
    ruijieSecZone2ZoneEntry.setStatus("current")


class _RuijieZoneFirstName_Type(DisplayString):
    """Custom type ruijieZoneFirstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieZoneFirstName_Type.__name__ = "DisplayString"
_RuijieZoneFirstName_Object = MibTableColumn
ruijieZoneFirstName = _RuijieZoneFirstName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 2, 1, 1),
    _RuijieZoneFirstName_Type()
)
ruijieZoneFirstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZoneFirstName.setStatus("current")


class _RuijieZoneSecondName_Type(DisplayString):
    """Custom type ruijieZoneSecondName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieZoneSecondName_Type.__name__ = "DisplayString"
_RuijieZoneSecondName_Object = MibTableColumn
ruijieZoneSecondName = _RuijieZoneSecondName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 2, 1, 2),
    _RuijieZoneSecondName_Type()
)
ruijieZoneSecondName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZoneSecondName.setStatus("current")


class _RuijieZone2ZoneAclName_Type(DisplayString):
    """Custom type ruijieZone2ZoneAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieZone2ZoneAclName_Type.__name__ = "DisplayString"
_RuijieZone2ZoneAclName_Object = MibTableColumn
ruijieZone2ZoneAclName = _RuijieZone2ZoneAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 2, 1, 3),
    _RuijieZone2ZoneAclName_Type()
)
ruijieZone2ZoneAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZone2ZoneAclName.setStatus("current")
_RuijieZone2ZoneEntryStauts_Type = RowStatus
_RuijieZone2ZoneEntryStauts_Object = MibTableColumn
ruijieZone2ZoneEntryStauts = _RuijieZone2ZoneEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 2, 1, 4),
    _RuijieZone2ZoneEntryStauts_Type()
)
ruijieZone2ZoneEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieZone2ZoneEntryStauts.setStatus("current")
_RuijieSecZoneBlockingTable_Object = MibTable
ruijieSecZoneBlockingTable = _RuijieSecZoneBlockingTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieSecZoneBlockingTable.setStatus("current")
_RuijieSecZoneBlockingEntry_Object = MibTableRow
ruijieSecZoneBlockingEntry = _RuijieSecZoneBlockingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 3, 1)
)
ruijieSecZoneBlockingEntry.setIndexNames(
    (0, "RUIJIE-SECZONE-MIB", "ruijieBockingIP"),
)
if mibBuilder.loadTexts:
    ruijieSecZoneBlockingEntry.setStatus("current")
_RuijieBockingIP_Type = IpAddress
_RuijieBockingIP_Object = MibTableColumn
ruijieBockingIP = _RuijieBockingIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 3, 1, 1),
    _RuijieBockingIP_Type()
)
ruijieBockingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingIP.setStatus("current")


class _RuijieBockingCurrentStatus_Type(Integer32):
    """Custom type ruijieBockingCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_RuijieBockingCurrentStatus_Type.__name__ = "Integer32"
_RuijieBockingCurrentStatus_Object = MibTableColumn
ruijieBockingCurrentStatus = _RuijieBockingCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 3, 1, 2),
    _RuijieBockingCurrentStatus_Type()
)
ruijieBockingCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingCurrentStatus.setStatus("current")


class _RuijieBockingTryAccessZoneName_Type(DisplayString):
    """Custom type ruijieBockingTryAccessZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieBockingTryAccessZoneName_Type.__name__ = "DisplayString"
_RuijieBockingTryAccessZoneName_Object = MibTableColumn
ruijieBockingTryAccessZoneName = _RuijieBockingTryAccessZoneName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 3, 1, 3),
    _RuijieBockingTryAccessZoneName_Type()
)
ruijieBockingTryAccessZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingTryAccessZoneName.setStatus("current")
_RuijieBockingEntryStatus_Type = ConfigStatus
_RuijieBockingEntryStatus_Object = MibTableColumn
ruijieBockingEntryStatus = _RuijieBockingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 3, 1, 4),
    _RuijieBockingEntryStatus_Type()
)
ruijieBockingEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieBockingEntryStatus.setStatus("current")


class _RuijieGlobalViolationNotifyThresh_Type(Integer32):
    """Custom type ruijieGlobalViolationNotifyThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieGlobalViolationNotifyThresh_Type.__name__ = "Integer32"
_RuijieGlobalViolationNotifyThresh_Object = MibScalar
ruijieGlobalViolationNotifyThresh = _RuijieGlobalViolationNotifyThresh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 4),
    _RuijieGlobalViolationNotifyThresh_Type()
)
ruijieGlobalViolationNotifyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalViolationNotifyThresh.setStatus("current")


class _RuijieGlobalViolationNotifyAction_Type(Integer32):
    """Custom type ruijieGlobalViolationNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_RuijieGlobalViolationNotifyAction_Type.__name__ = "Integer32"
_RuijieGlobalViolationNotifyAction_Object = MibScalar
ruijieGlobalViolationNotifyAction = _RuijieGlobalViolationNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 5),
    _RuijieGlobalViolationNotifyAction_Type()
)
ruijieGlobalViolationNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalViolationNotifyAction.setStatus("current")


class _RuijieGlobalViolationBlockThresh_Type(Integer32):
    """Custom type ruijieGlobalViolationBlockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieGlobalViolationBlockThresh_Type.__name__ = "Integer32"
_RuijieGlobalViolationBlockThresh_Object = MibScalar
ruijieGlobalViolationBlockThresh = _RuijieGlobalViolationBlockThresh_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 6),
    _RuijieGlobalViolationBlockThresh_Type()
)
ruijieGlobalViolationBlockThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalViolationBlockThresh.setStatus("current")


class _RuijieGlobalViolationBlockAction_Type(Integer32):
    """Custom type ruijieGlobalViolationBlockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_RuijieGlobalViolationBlockAction_Type.__name__ = "Integer32"
_RuijieGlobalViolationBlockAction_Object = MibScalar
ruijieGlobalViolationBlockAction = _RuijieGlobalViolationBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 7),
    _RuijieGlobalViolationBlockAction_Type()
)
ruijieGlobalViolationBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalViolationBlockAction.setStatus("current")


class _RuijieGlobalViolationBlockTimeout_Type(Integer32):
    """Custom type ruijieGlobalViolationBlockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuijieGlobalViolationBlockTimeout_Type.__name__ = "Integer32"
_RuijieGlobalViolationBlockTimeout_Object = MibScalar
ruijieGlobalViolationBlockTimeout = _RuijieGlobalViolationBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 8),
    _RuijieGlobalViolationBlockTimeout_Type()
)
ruijieGlobalViolationBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieGlobalViolationBlockTimeout.setStatus("current")
_ViolationTime_Type = DisplayString
_ViolationTime_Object = MibScalar
violationTime = _ViolationTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 9),
    _ViolationTime_Type()
)
violationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationTime.setStatus("current")
_ViolationSrcIP_Type = IpAddress
_ViolationSrcIP_Object = MibScalar
violationSrcIP = _ViolationSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 10),
    _ViolationSrcIP_Type()
)
violationSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationSrcIP.setStatus("current")
_ViolationDestIP_Type = IpAddress
_ViolationDestIP_Object = MibScalar
violationDestIP = _ViolationDestIP_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 11),
    _ViolationDestIP_Type()
)
violationDestIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationDestIP.setStatus("current")
_ViolationProtocol_Type = Integer32
_ViolationProtocol_Object = MibScalar
violationProtocol = _ViolationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 12),
    _ViolationProtocol_Type()
)
violationProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationProtocol.setStatus("current")
_ViolationL4Key_Type = Integer32
_ViolationL4Key_Object = MibScalar
violationL4Key = _ViolationL4Key_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 1, 13),
    _ViolationL4Key_Type()
)
violationL4Key.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationL4Key.setStatus("current")
_RuijieSecZoneMIBTraps_ObjectIdentity = ObjectIdentity
ruijieSecZoneMIBTraps = _RuijieSecZoneMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 2)
)
_RuijieSecZoneMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSecZoneMIBConformance = _RuijieSecZoneMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3)
)
_RuijieSecZoneMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSecZoneMIBCompliances = _RuijieSecZoneMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3, 1)
)
_RuijieSecZoneMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSecZoneMIBGroups = _RuijieSecZoneMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3, 2)
)

# Managed Objects groups

ruijieSecZoneMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3, 2, 1)
)
ruijieSecZoneMIBGroup.setObjects(
      *(("RUIJIE-SECZONE-MIB", "ruijieSecZoneChainName"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneLevel"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneAclName"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneViolationNotifyThresh"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneViolationNotifyAction"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneViolationBlockThresh"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneViolationBlockAction"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneViolationBlockTimeout"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneChainEntryStatus"),
        ("RUIJIE-SECZONE-MIB", "ruijieZoneFirstName"),
        ("RUIJIE-SECZONE-MIB", "ruijieZoneSecondName"),
        ("RUIJIE-SECZONE-MIB", "ruijieZone2ZoneAclName"),
        ("RUIJIE-SECZONE-MIB", "ruijieZone2ZoneEntryStauts"),
        ("RUIJIE-SECZONE-MIB", "ruijieBockingIP"),
        ("RUIJIE-SECZONE-MIB", "ruijieBockingCurrentStatus"),
        ("RUIJIE-SECZONE-MIB", "ruijieBockingTryAccessZoneName"),
        ("RUIJIE-SECZONE-MIB", "ruijieBockingEntryStatus"),
        ("RUIJIE-SECZONE-MIB", "ruijieGlobalViolationNotifyThresh"),
        ("RUIJIE-SECZONE-MIB", "ruijieGlobalViolationNotifyAction"),
        ("RUIJIE-SECZONE-MIB", "ruijieGlobalViolationBlockThresh"),
        ("RUIJIE-SECZONE-MIB", "ruijieGlobalViolationBlockAction"),
        ("RUIJIE-SECZONE-MIB", "ruijieGlobalViolationBlockTimeout"))
)
if mibBuilder.loadTexts:
    ruijieSecZoneMIBGroup.setStatus("current")

ruijieSecZoneNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3, 2, 2)
)
ruijieSecZoneNotifObjectsGroup.setObjects(
      *(("RUIJIE-SECZONE-MIB", "violationTime"),
        ("RUIJIE-SECZONE-MIB", "violationSrcIP"),
        ("RUIJIE-SECZONE-MIB", "violationDestIP"),
        ("RUIJIE-SECZONE-MIB", "violationProtocol"),
        ("RUIJIE-SECZONE-MIB", "violationL4Key"))
)
if mibBuilder.loadTexts:
    ruijieSecZoneNotifObjectsGroup.setStatus("current")


# Notification objects

ruijieSecZoneViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 2, 1)
)
ruijieSecZoneViolationTrap.setObjects(
      *(("RUIJIE-SECZONE-MIB", "violationTime"),
        ("RUIJIE-SECZONE-MIB", "violationSrcIP"),
        ("RUIJIE-SECZONE-MIB", "violationDestIP"),
        ("RUIJIE-SECZONE-MIB", "violationProtocol"),
        ("RUIJIE-SECZONE-MIB", "violationL4Key"),
        ("RUIJIE-SECZONE-MIB", "ruijieZoneFirstName"),
        ("RUIJIE-SECZONE-MIB", "ruijieZoneSecondName"))
)
if mibBuilder.loadTexts:
    ruijieSecZoneViolationTrap.setStatus(
        "current"
    )


# Notifications groups

ruijieSecZoneNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3, 2, 3)
)
ruijieSecZoneNotificationsGroup.setObjects(
    ("RUIJIE-SECZONE-MIB", "ruijieSecZoneViolationTrap")
)
if mibBuilder.loadTexts:
    ruijieSecZoneNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieSecZoneMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 54, 3, 1, 1)
)
ruijieSecZoneMIBCompliance.setObjects(
      *(("RUIJIE-SECZONE-MIB", "ruijieSecZoneMIBGroup"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneNotifObjectsGroup"),
        ("RUIJIE-SECZONE-MIB", "ruijieSecZoneNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ruijieSecZoneMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SECZONE-MIB",
    **{"ruijieSecZoneMIB": ruijieSecZoneMIB,
       "ruijieSecZoneMIBObjects": ruijieSecZoneMIBObjects,
       "ruijieSecZoneChainTable": ruijieSecZoneChainTable,
       "ruijieSecZoneChainEntry": ruijieSecZoneChainEntry,
       "ruijieSecZoneChainName": ruijieSecZoneChainName,
       "ruijieSecZoneLevel": ruijieSecZoneLevel,
       "ruijieSecZoneAclName": ruijieSecZoneAclName,
       "ruijieSecZoneViolationNotifyThresh": ruijieSecZoneViolationNotifyThresh,
       "ruijieSecZoneViolationNotifyAction": ruijieSecZoneViolationNotifyAction,
       "ruijieSecZoneViolationBlockThresh": ruijieSecZoneViolationBlockThresh,
       "ruijieSecZoneViolationBlockAction": ruijieSecZoneViolationBlockAction,
       "ruijieSecZoneViolationBlockTimeout": ruijieSecZoneViolationBlockTimeout,
       "ruijieSecZoneChainEntryStatus": ruijieSecZoneChainEntryStatus,
       "ruijieSecZone2ZoneTable": ruijieSecZone2ZoneTable,
       "ruijieSecZone2ZoneEntry": ruijieSecZone2ZoneEntry,
       "ruijieZoneFirstName": ruijieZoneFirstName,
       "ruijieZoneSecondName": ruijieZoneSecondName,
       "ruijieZone2ZoneAclName": ruijieZone2ZoneAclName,
       "ruijieZone2ZoneEntryStauts": ruijieZone2ZoneEntryStauts,
       "ruijieSecZoneBlockingTable": ruijieSecZoneBlockingTable,
       "ruijieSecZoneBlockingEntry": ruijieSecZoneBlockingEntry,
       "ruijieBockingIP": ruijieBockingIP,
       "ruijieBockingCurrentStatus": ruijieBockingCurrentStatus,
       "ruijieBockingTryAccessZoneName": ruijieBockingTryAccessZoneName,
       "ruijieBockingEntryStatus": ruijieBockingEntryStatus,
       "ruijieGlobalViolationNotifyThresh": ruijieGlobalViolationNotifyThresh,
       "ruijieGlobalViolationNotifyAction": ruijieGlobalViolationNotifyAction,
       "ruijieGlobalViolationBlockThresh": ruijieGlobalViolationBlockThresh,
       "ruijieGlobalViolationBlockAction": ruijieGlobalViolationBlockAction,
       "ruijieGlobalViolationBlockTimeout": ruijieGlobalViolationBlockTimeout,
       "violationTime": violationTime,
       "violationSrcIP": violationSrcIP,
       "violationDestIP": violationDestIP,
       "violationProtocol": violationProtocol,
       "violationL4Key": violationL4Key,
       "ruijieSecZoneMIBTraps": ruijieSecZoneMIBTraps,
       "ruijieSecZoneViolationTrap": ruijieSecZoneViolationTrap,
       "ruijieSecZoneMIBConformance": ruijieSecZoneMIBConformance,
       "ruijieSecZoneMIBCompliances": ruijieSecZoneMIBCompliances,
       "ruijieSecZoneMIBCompliance": ruijieSecZoneMIBCompliance,
       "ruijieSecZoneMIBGroups": ruijieSecZoneMIBGroups,
       "ruijieSecZoneMIBGroup": ruijieSecZoneMIBGroup,
       "ruijieSecZoneNotifObjectsGroup": ruijieSecZoneNotifObjectsGroup,
       "ruijieSecZoneNotificationsGroup": ruijieSecZoneNotificationsGroup}
)
