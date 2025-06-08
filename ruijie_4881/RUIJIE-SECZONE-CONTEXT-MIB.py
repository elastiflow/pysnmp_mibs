# SNMP MIB module (RUIJIE-SECZONE-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-SECZONE-CONTEXT-MIB.mib
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

ruijieSecZoneVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68)
)
if mibBuilder.loadTexts:
    ruijieSecZoneVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSecZoneVCMIBObjects_ObjectIdentity = ObjectIdentity
ruijieSecZoneVCMIBObjects = _RuijieSecZoneVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1)
)
_RuijieSecZoneChainVCTable_Object = MibTable
ruijieSecZoneChainVCTable = _RuijieSecZoneChainVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieSecZoneChainVCTable.setStatus("current")
_RuijieSecZoneChainVCEntry_Object = MibTableRow
ruijieSecZoneChainVCEntry = _RuijieSecZoneChainVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1)
)
ruijieSecZoneChainVCEntry.setIndexNames(
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneContextNameVC"),
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneChainNameVC"),
)
if mibBuilder.loadTexts:
    ruijieSecZoneChainVCEntry.setStatus("current")


class _RuijieSecZoneContextNameVC_Type(DisplayString):
    """Custom type ruijieSecZoneContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieSecZoneContextNameVC_Type.__name__ = "DisplayString"
_RuijieSecZoneContextNameVC_Object = MibTableColumn
ruijieSecZoneContextNameVC = _RuijieSecZoneContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 1),
    _RuijieSecZoneContextNameVC_Type()
)
ruijieSecZoneContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecZoneContextNameVC.setStatus("current")


class _RuijieSecZoneChainNameVC_Type(DisplayString):
    """Custom type ruijieSecZoneChainNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSecZoneChainNameVC_Type.__name__ = "DisplayString"
_RuijieSecZoneChainNameVC_Object = MibTableColumn
ruijieSecZoneChainNameVC = _RuijieSecZoneChainNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 2),
    _RuijieSecZoneChainNameVC_Type()
)
ruijieSecZoneChainNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSecZoneChainNameVC.setStatus("current")


class _RuijieSecZoneLevelVC_Type(Integer32):
    """Custom type ruijieSecZoneLevelVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieSecZoneLevelVC_Type.__name__ = "Integer32"
_RuijieSecZoneLevelVC_Object = MibTableColumn
ruijieSecZoneLevelVC = _RuijieSecZoneLevelVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 3),
    _RuijieSecZoneLevelVC_Type()
)
ruijieSecZoneLevelVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneLevelVC.setStatus("current")


class _RuijieSecZoneAclNameVC_Type(DisplayString):
    """Custom type ruijieSecZoneAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieSecZoneAclNameVC_Type.__name__ = "DisplayString"
_RuijieSecZoneAclNameVC_Object = MibTableColumn
ruijieSecZoneAclNameVC = _RuijieSecZoneAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 4),
    _RuijieSecZoneAclNameVC_Type()
)
ruijieSecZoneAclNameVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneAclNameVC.setStatus("current")


class _RuijieSecZoneViolationNotifyThreshVC_Type(Integer32):
    """Custom type ruijieSecZoneViolationNotifyThreshVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSecZoneViolationNotifyThreshVC_Type.__name__ = "Integer32"
_RuijieSecZoneViolationNotifyThreshVC_Object = MibTableColumn
ruijieSecZoneViolationNotifyThreshVC = _RuijieSecZoneViolationNotifyThreshVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 5),
    _RuijieSecZoneViolationNotifyThreshVC_Type()
)
ruijieSecZoneViolationNotifyThreshVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationNotifyThreshVC.setStatus("current")


class _RuijieSecZoneViolationNotifyActionVC_Type(Integer32):
    """Custom type ruijieSecZoneViolationNotifyActionVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nologtrap", 0),
          ("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_RuijieSecZoneViolationNotifyActionVC_Type.__name__ = "Integer32"
_RuijieSecZoneViolationNotifyActionVC_Object = MibTableColumn
ruijieSecZoneViolationNotifyActionVC = _RuijieSecZoneViolationNotifyActionVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 6),
    _RuijieSecZoneViolationNotifyActionVC_Type()
)
ruijieSecZoneViolationNotifyActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationNotifyActionVC.setStatus("current")


class _RuijieSecZoneViolationBlockThreshVC_Type(Integer32):
    """Custom type ruijieSecZoneViolationBlockThreshVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijieSecZoneViolationBlockThreshVC_Type.__name__ = "Integer32"
_RuijieSecZoneViolationBlockThreshVC_Object = MibTableColumn
ruijieSecZoneViolationBlockThreshVC = _RuijieSecZoneViolationBlockThreshVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 7),
    _RuijieSecZoneViolationBlockThreshVC_Type()
)
ruijieSecZoneViolationBlockThreshVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationBlockThreshVC.setStatus("current")


class _RuijieSecZoneViolationBlockActionVC_Type(Integer32):
    """Custom type ruijieSecZoneViolationBlockActionVC based on Integer32"""
    defaultValue = 1

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


_RuijieSecZoneViolationBlockActionVC_Type.__name__ = "Integer32"
_RuijieSecZoneViolationBlockActionVC_Object = MibTableColumn
ruijieSecZoneViolationBlockActionVC = _RuijieSecZoneViolationBlockActionVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 8),
    _RuijieSecZoneViolationBlockActionVC_Type()
)
ruijieSecZoneViolationBlockActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationBlockActionVC.setStatus("current")


class _RuijieSecZoneViolationBlockTimeoutVC_Type(Integer32):
    """Custom type ruijieSecZoneViolationBlockTimeoutVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RuijieSecZoneViolationBlockTimeoutVC_Type.__name__ = "Integer32"
_RuijieSecZoneViolationBlockTimeoutVC_Object = MibTableColumn
ruijieSecZoneViolationBlockTimeoutVC = _RuijieSecZoneViolationBlockTimeoutVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 9),
    _RuijieSecZoneViolationBlockTimeoutVC_Type()
)
ruijieSecZoneViolationBlockTimeoutVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneViolationBlockTimeoutVC.setStatus("current")
_RuijieSecZoneChainEntryStatusVC_Type = RowStatus
_RuijieSecZoneChainEntryStatusVC_Object = MibTableColumn
ruijieSecZoneChainEntryStatusVC = _RuijieSecZoneChainEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 1, 1, 10),
    _RuijieSecZoneChainEntryStatusVC_Type()
)
ruijieSecZoneChainEntryStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieSecZoneChainEntryStatusVC.setStatus("current")
_RuijieSecZone2ZoneVCTable_Object = MibTable
ruijieSecZone2ZoneVCTable = _RuijieSecZone2ZoneVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieSecZone2ZoneVCTable.setStatus("current")
_RuijieSecZone2ZoneVCEntry_Object = MibTableRow
ruijieSecZone2ZoneVCEntry = _RuijieSecZone2ZoneVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2, 1)
)
ruijieSecZone2ZoneVCEntry.setIndexNames(
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZone2ZoneContextNameVC"),
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZoneFirstNameVC"),
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZoneSecondNameVC"),
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZone2ZoneAclNameVC"),
)
if mibBuilder.loadTexts:
    ruijieSecZone2ZoneVCEntry.setStatus("current")


class _RuijieZone2ZoneContextNameVC_Type(DisplayString):
    """Custom type ruijieZone2ZoneContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieZone2ZoneContextNameVC_Type.__name__ = "DisplayString"
_RuijieZone2ZoneContextNameVC_Object = MibTableColumn
ruijieZone2ZoneContextNameVC = _RuijieZone2ZoneContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2, 1, 1),
    _RuijieZone2ZoneContextNameVC_Type()
)
ruijieZone2ZoneContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZone2ZoneContextNameVC.setStatus("current")


class _RuijieZoneFirstNameVC_Type(DisplayString):
    """Custom type ruijieZoneFirstNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieZoneFirstNameVC_Type.__name__ = "DisplayString"
_RuijieZoneFirstNameVC_Object = MibTableColumn
ruijieZoneFirstNameVC = _RuijieZoneFirstNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2, 1, 2),
    _RuijieZoneFirstNameVC_Type()
)
ruijieZoneFirstNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZoneFirstNameVC.setStatus("current")


class _RuijieZoneSecondNameVC_Type(DisplayString):
    """Custom type ruijieZoneSecondNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieZoneSecondNameVC_Type.__name__ = "DisplayString"
_RuijieZoneSecondNameVC_Object = MibTableColumn
ruijieZoneSecondNameVC = _RuijieZoneSecondNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2, 1, 3),
    _RuijieZoneSecondNameVC_Type()
)
ruijieZoneSecondNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZoneSecondNameVC.setStatus("current")


class _RuijieZone2ZoneAclNameVC_Type(DisplayString):
    """Custom type ruijieZone2ZoneAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieZone2ZoneAclNameVC_Type.__name__ = "DisplayString"
_RuijieZone2ZoneAclNameVC_Object = MibTableColumn
ruijieZone2ZoneAclNameVC = _RuijieZone2ZoneAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2, 1, 4),
    _RuijieZone2ZoneAclNameVC_Type()
)
ruijieZone2ZoneAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieZone2ZoneAclNameVC.setStatus("current")
_RuijieZone2ZoneEntryStautsVC_Type = RowStatus
_RuijieZone2ZoneEntryStautsVC_Object = MibTableColumn
ruijieZone2ZoneEntryStautsVC = _RuijieZone2ZoneEntryStautsVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 2, 1, 5),
    _RuijieZone2ZoneEntryStautsVC_Type()
)
ruijieZone2ZoneEntryStautsVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieZone2ZoneEntryStautsVC.setStatus("current")
_RuijieSecZoneBlockingVCTable_Object = MibTable
ruijieSecZoneBlockingVCTable = _RuijieSecZoneBlockingVCTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieSecZoneBlockingVCTable.setStatus("current")
_RuijieSecZoneBlockingVCEntry_Object = MibTableRow
ruijieSecZoneBlockingVCEntry = _RuijieSecZoneBlockingVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3, 1)
)
ruijieSecZoneBlockingVCEntry.setIndexNames(
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingContextNameVC"),
    (0, "RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingIPVC"),
)
if mibBuilder.loadTexts:
    ruijieSecZoneBlockingVCEntry.setStatus("current")


class _RuijieBockingContextNameVC_Type(DisplayString):
    """Custom type ruijieBockingContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_RuijieBockingContextNameVC_Type.__name__ = "DisplayString"
_RuijieBockingContextNameVC_Object = MibTableColumn
ruijieBockingContextNameVC = _RuijieBockingContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3, 1, 1),
    _RuijieBockingContextNameVC_Type()
)
ruijieBockingContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingContextNameVC.setStatus("current")
_RuijieBockingIPVC_Type = IpAddress
_RuijieBockingIPVC_Object = MibTableColumn
ruijieBockingIPVC = _RuijieBockingIPVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3, 1, 2),
    _RuijieBockingIPVC_Type()
)
ruijieBockingIPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingIPVC.setStatus("current")


class _RuijieBockingCurrentStatusVC_Type(Integer32):
    """Custom type ruijieBockingCurrentStatusVC based on Integer32"""
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


_RuijieBockingCurrentStatusVC_Type.__name__ = "Integer32"
_RuijieBockingCurrentStatusVC_Object = MibTableColumn
ruijieBockingCurrentStatusVC = _RuijieBockingCurrentStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3, 1, 3),
    _RuijieBockingCurrentStatusVC_Type()
)
ruijieBockingCurrentStatusVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingCurrentStatusVC.setStatus("current")


class _RuijieBockingTryAccessZoneNameVC_Type(DisplayString):
    """Custom type ruijieBockingTryAccessZoneNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieBockingTryAccessZoneNameVC_Type.__name__ = "DisplayString"
_RuijieBockingTryAccessZoneNameVC_Object = MibTableColumn
ruijieBockingTryAccessZoneNameVC = _RuijieBockingTryAccessZoneNameVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3, 1, 4),
    _RuijieBockingTryAccessZoneNameVC_Type()
)
ruijieBockingTryAccessZoneNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieBockingTryAccessZoneNameVC.setStatus("current")
_RuijieBockingEntryStatusVC_Type = ConfigStatus
_RuijieBockingEntryStatusVC_Object = MibTableColumn
ruijieBockingEntryStatusVC = _RuijieBockingEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 1, 3, 1, 5),
    _RuijieBockingEntryStatusVC_Type()
)
ruijieBockingEntryStatusVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieBockingEntryStatusVC.setStatus("current")
_RuijieSecZoneVCMIBConformance_ObjectIdentity = ObjectIdentity
ruijieSecZoneVCMIBConformance = _RuijieSecZoneVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 3)
)
_RuijieSecZoneVCMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieSecZoneVCMIBCompliances = _RuijieSecZoneVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 3, 1)
)
_RuijieSecZoneVCMIBGroups_ObjectIdentity = ObjectIdentity
ruijieSecZoneVCMIBGroups = _RuijieSecZoneVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 3, 2)
)

# Managed Objects groups

ruijieSecZoneVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 3, 2, 1)
)
ruijieSecZoneVCMIBGroup.setObjects(
      *(("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneContextNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneChainNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneLevelVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneAclNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneViolationNotifyThreshVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneViolationNotifyActionVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneViolationBlockThreshVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneViolationBlockActionVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneViolationBlockTimeoutVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneChainEntryStatusVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZone2ZoneContextNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZoneFirstNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZoneSecondNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZone2ZoneAclNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieZone2ZoneEntryStautsVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingContextNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingIPVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingCurrentStatusVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingTryAccessZoneNameVC"),
        ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieBockingEntryStatusVC"))
)
if mibBuilder.loadTexts:
    ruijieSecZoneVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieSecZoneVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 68, 3, 1, 1)
)
ruijieSecZoneVCMIBCompliance.setObjects(
    ("RUIJIE-SECZONE-CONTEXT-MIB", "ruijieSecZoneVCMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieSecZoneVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-SECZONE-CONTEXT-MIB",
    **{"ruijieSecZoneVCMIB": ruijieSecZoneVCMIB,
       "ruijieSecZoneVCMIBObjects": ruijieSecZoneVCMIBObjects,
       "ruijieSecZoneChainVCTable": ruijieSecZoneChainVCTable,
       "ruijieSecZoneChainVCEntry": ruijieSecZoneChainVCEntry,
       "ruijieSecZoneContextNameVC": ruijieSecZoneContextNameVC,
       "ruijieSecZoneChainNameVC": ruijieSecZoneChainNameVC,
       "ruijieSecZoneLevelVC": ruijieSecZoneLevelVC,
       "ruijieSecZoneAclNameVC": ruijieSecZoneAclNameVC,
       "ruijieSecZoneViolationNotifyThreshVC": ruijieSecZoneViolationNotifyThreshVC,
       "ruijieSecZoneViolationNotifyActionVC": ruijieSecZoneViolationNotifyActionVC,
       "ruijieSecZoneViolationBlockThreshVC": ruijieSecZoneViolationBlockThreshVC,
       "ruijieSecZoneViolationBlockActionVC": ruijieSecZoneViolationBlockActionVC,
       "ruijieSecZoneViolationBlockTimeoutVC": ruijieSecZoneViolationBlockTimeoutVC,
       "ruijieSecZoneChainEntryStatusVC": ruijieSecZoneChainEntryStatusVC,
       "ruijieSecZone2ZoneVCTable": ruijieSecZone2ZoneVCTable,
       "ruijieSecZone2ZoneVCEntry": ruijieSecZone2ZoneVCEntry,
       "ruijieZone2ZoneContextNameVC": ruijieZone2ZoneContextNameVC,
       "ruijieZoneFirstNameVC": ruijieZoneFirstNameVC,
       "ruijieZoneSecondNameVC": ruijieZoneSecondNameVC,
       "ruijieZone2ZoneAclNameVC": ruijieZone2ZoneAclNameVC,
       "ruijieZone2ZoneEntryStautsVC": ruijieZone2ZoneEntryStautsVC,
       "ruijieSecZoneBlockingVCTable": ruijieSecZoneBlockingVCTable,
       "ruijieSecZoneBlockingVCEntry": ruijieSecZoneBlockingVCEntry,
       "ruijieBockingContextNameVC": ruijieBockingContextNameVC,
       "ruijieBockingIPVC": ruijieBockingIPVC,
       "ruijieBockingCurrentStatusVC": ruijieBockingCurrentStatusVC,
       "ruijieBockingTryAccessZoneNameVC": ruijieBockingTryAccessZoneNameVC,
       "ruijieBockingEntryStatusVC": ruijieBockingEntryStatusVC,
       "ruijieSecZoneVCMIBConformance": ruijieSecZoneVCMIBConformance,
       "ruijieSecZoneVCMIBCompliances": ruijieSecZoneVCMIBCompliances,
       "ruijieSecZoneVCMIBCompliance": ruijieSecZoneVCMIBCompliance,
       "ruijieSecZoneVCMIBGroups": ruijieSecZoneVCMIBGroups,
       "ruijieSecZoneVCMIBGroup": ruijieSecZoneVCMIBGroup}
)
