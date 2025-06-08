# SNMP MIB module (ZHONE-REMOTE-SW-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHONE-REMOTE-SW-UPGRADE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:11:11 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zhone,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhone",
    "zhoneModules")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneRemoteSwUpgrade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117)
)
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgrade.setRevisions(
        ("2009-07-01 07:45",
         "2009-06-09 08:33")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneRemoteSwUpgradeTable_Object = MibTable
zhoneRemoteSwUpgradeTable = _ZhoneRemoteSwUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1)
)
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeTable.setStatus("current")
_ZhoneRemoteSwUpgradeEntry_Object = MibTableRow
zhoneRemoteSwUpgradeEntry = _ZhoneRemoteSwUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1)
)
zhoneRemoteSwUpgradeEntry.setIndexNames(
    (0, "ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeIndex"),
)
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeEntry.setStatus("current")


class _ZhoneRemoteSwUpgradeIndex_Type(Integer32):
    """Custom type zhoneRemoteSwUpgradeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneRemoteSwUpgradeIndex_Type.__name__ = "Integer32"
_ZhoneRemoteSwUpgradeIndex_Object = MibTableColumn
zhoneRemoteSwUpgradeIndex = _ZhoneRemoteSwUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1, 1),
    _ZhoneRemoteSwUpgradeIndex_Type()
)
zhoneRemoteSwUpgradeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeIndex.setStatus("current")
_ZhoneRemoteSwUpgradeRowStatus_Type = ZhoneRowStatus
_ZhoneRemoteSwUpgradeRowStatus_Object = MibTableColumn
zhoneRemoteSwUpgradeRowStatus = _ZhoneRemoteSwUpgradeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1, 2),
    _ZhoneRemoteSwUpgradeRowStatus_Type()
)
zhoneRemoteSwUpgradeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeRowStatus.setStatus("current")


class _ZhoneRemoteSwUpgradeEnabled_Type(TruthValue):
    """Custom type zhoneRemoteSwUpgradeEnabled based on TruthValue"""
    defaultValue = 1


_ZhoneRemoteSwUpgradeEnabled_Type.__name__ = "TruthValue"
_ZhoneRemoteSwUpgradeEnabled_Object = MibTableColumn
zhoneRemoteSwUpgradeEnabled = _ZhoneRemoteSwUpgradeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1, 3),
    _ZhoneRemoteSwUpgradeEnabled_Type()
)
zhoneRemoteSwUpgradeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeEnabled.setStatus("current")


class _ZhoneRemoteSwUpgradeModel_Type(OctetString):
    """Custom type zhoneRemoteSwUpgradeModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZhoneRemoteSwUpgradeModel_Type.__name__ = "OctetString"
_ZhoneRemoteSwUpgradeModel_Object = MibTableColumn
zhoneRemoteSwUpgradeModel = _ZhoneRemoteSwUpgradeModel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1, 4),
    _ZhoneRemoteSwUpgradeModel_Type()
)
zhoneRemoteSwUpgradeModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeModel.setStatus("current")


class _ZhoneRemoteSwUpgradeSwVersion_Type(OctetString):
    """Custom type zhoneRemoteSwUpgradeSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZhoneRemoteSwUpgradeSwVersion_Type.__name__ = "OctetString"
_ZhoneRemoteSwUpgradeSwVersion_Object = MibTableColumn
zhoneRemoteSwUpgradeSwVersion = _ZhoneRemoteSwUpgradeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1, 5),
    _ZhoneRemoteSwUpgradeSwVersion_Type()
)
zhoneRemoteSwUpgradeSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeSwVersion.setStatus("current")


class _ZhoneRemoteSwUpgradeFileName_Type(OctetString):
    """Custom type zhoneRemoteSwUpgradeFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ZhoneRemoteSwUpgradeFileName_Type.__name__ = "OctetString"
_ZhoneRemoteSwUpgradeFileName_Object = MibTableColumn
zhoneRemoteSwUpgradeFileName = _ZhoneRemoteSwUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 1, 1, 6),
    _ZhoneRemoteSwUpgradeFileName_Type()
)
zhoneRemoteSwUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeFileName.setStatus("current")


class _ZhoneRemoteSwUpgradeIndexNext_Type(Unsigned32):
    """Custom type zhoneRemoteSwUpgradeIndexNext based on Unsigned32"""
    defaultValue = 1


_ZhoneRemoteSwUpgradeIndexNext_Type.__name__ = "Unsigned32"
_ZhoneRemoteSwUpgradeIndexNext_Object = MibScalar
zhoneRemoteSwUpgradeIndexNext = _ZhoneRemoteSwUpgradeIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 5504, 6, 117, 2),
    _ZhoneRemoteSwUpgradeIndexNext_Type()
)
zhoneRemoteSwUpgradeIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneRemoteSwUpgradeIndexNext.setStatus("current")
_ZhoneCompliances_ObjectIdentity = ObjectIdentity
zhoneCompliances = _ZhoneCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 9)
)
_ZhoneGroups_ObjectIdentity = ObjectIdentity
zhoneGroups = _ZhoneGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1)
)

# Managed Objects groups

zhoneAutoUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 9, 1, 30)
)
zhoneAutoUpgradeGroup.setObjects(
      *(("ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeModel"),
        ("ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeSwVersion"),
        ("ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeRowStatus"),
        ("ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeIndexNext"),
        ("ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeFileName"),
        ("ZHONE-REMOTE-SW-UPGRADE-MIB", "zhoneRemoteSwUpgradeEnabled"))
)
if mibBuilder.loadTexts:
    zhoneAutoUpgradeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-REMOTE-SW-UPGRADE-MIB",
    **{"zhoneRemoteSwUpgrade": zhoneRemoteSwUpgrade,
       "zhoneRemoteSwUpgradeTable": zhoneRemoteSwUpgradeTable,
       "zhoneRemoteSwUpgradeEntry": zhoneRemoteSwUpgradeEntry,
       "zhoneRemoteSwUpgradeIndex": zhoneRemoteSwUpgradeIndex,
       "zhoneRemoteSwUpgradeRowStatus": zhoneRemoteSwUpgradeRowStatus,
       "zhoneRemoteSwUpgradeEnabled": zhoneRemoteSwUpgradeEnabled,
       "zhoneRemoteSwUpgradeModel": zhoneRemoteSwUpgradeModel,
       "zhoneRemoteSwUpgradeSwVersion": zhoneRemoteSwUpgradeSwVersion,
       "zhoneRemoteSwUpgradeFileName": zhoneRemoteSwUpgradeFileName,
       "zhoneRemoteSwUpgradeIndexNext": zhoneRemoteSwUpgradeIndexNext,
       "zhoneCompliances": zhoneCompliances,
       "zhoneGroups": zhoneGroups,
       "zhoneAutoUpgradeGroup": zhoneAutoUpgradeGroup}
)
