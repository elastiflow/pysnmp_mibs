# SNMP MIB module (RUIJIE-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-UPGRADE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieUpgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158)
)
if mibBuilder.loadTexts:
    ruijieUpgradeMIB.setRevisions(
        ("2018-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieUpgradeMIBObjects_ObjectIdentity = ObjectIdentity
ruijieUpgradeMIBObjects = _RuijieUpgradeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 1)
)
_RuijieUpgradeMIBGroups_ObjectIdentity = ObjectIdentity
ruijieUpgradeMIBGroups = _RuijieUpgradeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 1, 1)
)


class _RuijieFileSystemUpgradeDownloadUrl_Type(DisplayString):
    """Custom type ruijieFileSystemUpgradeDownloadUrl based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieFileSystemUpgradeDownloadUrl_Type.__name__ = "DisplayString"
_RuijieFileSystemUpgradeDownloadUrl_Object = MibScalar
ruijieFileSystemUpgradeDownloadUrl = _RuijieFileSystemUpgradeDownloadUrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 1, 1, 1),
    _RuijieFileSystemUpgradeDownloadUrl_Type()
)
ruijieFileSystemUpgradeDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieFileSystemUpgradeDownloadUrl.setStatus("current")


class _RuijieFileSystemUpgradeDownloadFlag_Type(Integer32):
    """Custom type ruijieFileSystemUpgradeDownloadFlag based on Integer32"""
    defaultValue = 0


_RuijieFileSystemUpgradeDownloadFlag_Type.__name__ = "Integer32"
_RuijieFileSystemUpgradeDownloadFlag_Object = MibScalar
ruijieFileSystemUpgradeDownloadFlag = _RuijieFileSystemUpgradeDownloadFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 1, 1, 2),
    _RuijieFileSystemUpgradeDownloadFlag_Type()
)
ruijieFileSystemUpgradeDownloadFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieFileSystemUpgradeDownloadFlag.setStatus("current")
_RuijieUpgradeMIBTraps_ObjectIdentity = ObjectIdentity
ruijieUpgradeMIBTraps = _RuijieUpgradeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 2)
)
_RuijieUpgradeMIBConformance_ObjectIdentity = ObjectIdentity
ruijieUpgradeMIBConformance = _RuijieUpgradeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 3)
)
_RuijieUpgradeMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieUpgradeMIBCompliances = _RuijieUpgradeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 3, 1)
)
_RuijieSystemCurrtenVersion_Type = DisplayString
_RuijieSystemCurrtenVersion_Object = MibScalar
ruijieSystemCurrtenVersion = _RuijieSystemCurrtenVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 3, 1, 1),
    _RuijieSystemCurrtenVersion_Type()
)
ruijieSystemCurrtenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemCurrtenVersion.setStatus("current")
_RuijieSystemUpgradeFailNo_Type = Integer32
_RuijieSystemUpgradeFailNo_Object = MibScalar
ruijieSystemUpgradeFailNo = _RuijieSystemUpgradeFailNo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 3, 1, 2),
    _RuijieSystemUpgradeFailNo_Type()
)
ruijieSystemUpgradeFailNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemUpgradeFailNo.setStatus("current")
_RuijieSystemUpgradeFailReason_Type = DisplayString
_RuijieSystemUpgradeFailReason_Object = MibScalar
ruijieSystemUpgradeFailReason = _RuijieSystemUpgradeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 3, 1, 3),
    _RuijieSystemUpgradeFailReason_Type()
)
ruijieSystemUpgradeFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemUpgradeFailReason.setStatus("current")
_RuijieSystemUpgradeFailVersion_Type = DisplayString
_RuijieSystemUpgradeFailVersion_Object = MibScalar
ruijieSystemUpgradeFailVersion = _RuijieSystemUpgradeFailVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 3, 1, 4),
    _RuijieSystemUpgradeFailVersion_Type()
)
ruijieSystemUpgradeFailVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSystemUpgradeFailVersion.setStatus("current")

# Managed Objects groups


# Notification objects

ruijieUpgradeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 2, 1)
)
ruijieUpgradeFailTrap.setObjects(
      *(("RUIJIE-UPGRADE-MIB", "ruijieSystemCurrtenVersion"),
        ("RUIJIE-UPGRADE-MIB", "ruijieSystemUpgradeFailNo"),
        ("RUIJIE-UPGRADE-MIB", "ruijieSystemUpgradeFailReason"),
        ("RUIJIE-UPGRADE-MIB", "ruijieSystemUpgradeFailVersion"))
)
if mibBuilder.loadTexts:
    ruijieUpgradeFailTrap.setStatus(
        "current"
    )

ruijieUpgradeFailRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 158, 2, 2)
)
ruijieUpgradeFailRecovTrap.setObjects(
      *(("RUIJIE-UPGRADE-MIB", "ruijieSystemCurrtenVersion"),
        ("RUIJIE-UPGRADE-MIB", "ruijieSystemUpgradeFailNo"),
        ("RUIJIE-UPGRADE-MIB", "ruijieSystemUpgradeFailReason"),
        ("RUIJIE-UPGRADE-MIB", "ruijieSystemUpgradeFailVersion"))
)
if mibBuilder.loadTexts:
    ruijieUpgradeFailRecovTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-UPGRADE-MIB",
    **{"ruijieUpgradeMIB": ruijieUpgradeMIB,
       "ruijieUpgradeMIBObjects": ruijieUpgradeMIBObjects,
       "ruijieUpgradeMIBGroups": ruijieUpgradeMIBGroups,
       "ruijieFileSystemUpgradeDownloadUrl": ruijieFileSystemUpgradeDownloadUrl,
       "ruijieFileSystemUpgradeDownloadFlag": ruijieFileSystemUpgradeDownloadFlag,
       "ruijieUpgradeMIBTraps": ruijieUpgradeMIBTraps,
       "ruijieUpgradeFailTrap": ruijieUpgradeFailTrap,
       "ruijieUpgradeFailRecovTrap": ruijieUpgradeFailRecovTrap,
       "ruijieUpgradeMIBConformance": ruijieUpgradeMIBConformance,
       "ruijieUpgradeMIBCompliances": ruijieUpgradeMIBCompliances,
       "ruijieSystemCurrtenVersion": ruijieSystemCurrtenVersion,
       "ruijieSystemUpgradeFailNo": ruijieSystemUpgradeFailNo,
       "ruijieSystemUpgradeFailReason": ruijieSystemUpgradeFailReason,
       "ruijieSystemUpgradeFailVersion": ruijieSystemUpgradeFailVersion}
)
