# SNMP MIB module (CISCO-SIBU-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SIBU-FLASH-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoSibuFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45)
)
if mibBuilder.loadTexts:
    ciscoSibuFlashMIB.setRevisions(
        ("1998-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSibuFlashMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBObjects = _CiscoSibuFlashMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1)
)
_CsfUpgrade_ObjectIdentity = ObjectIdentity
csfUpgrade = _CsfUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1)
)


class _CsfUpgradeFirmwareVersion_Type(DisplayString):
    """Custom type csfUpgradeFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CsfUpgradeFirmwareVersion_Type.__name__ = "DisplayString"
_CsfUpgradeFirmwareVersion_Object = MibScalar
csfUpgradeFirmwareVersion = _CsfUpgradeFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 1),
    _CsfUpgradeFirmwareVersion_Type()
)
csfUpgradeFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfUpgradeFirmwareVersion.setStatus("current")


class _CsfUpgradeFlashSize_Type(Integer32):
    """Custom type csfUpgradeFlashSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsfUpgradeFlashSize_Type.__name__ = "Integer32"
_CsfUpgradeFlashSize_Object = MibScalar
csfUpgradeFlashSize = _CsfUpgradeFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 2),
    _CsfUpgradeFlashSize_Type()
)
csfUpgradeFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfUpgradeFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    csfUpgradeFlashSize.setUnits("kbytes")


class _CsfUpgradeTFTPServerAddress_Type(IpAddress):
    """Custom type csfUpgradeTFTPServerAddress based on IpAddress"""
    defaultHexValue = "00000000"


_CsfUpgradeTFTPServerAddress_Type.__name__ = "IpAddress"
_CsfUpgradeTFTPServerAddress_Object = MibScalar
csfUpgradeTFTPServerAddress = _CsfUpgradeTFTPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 3),
    _CsfUpgradeTFTPServerAddress_Type()
)
csfUpgradeTFTPServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeTFTPServerAddress.setStatus("current")


class _CsfUpgradeTFTPLoadFilename_Type(DisplayString):
    """Custom type csfUpgradeTFTPLoadFilename based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsfUpgradeTFTPLoadFilename_Type.__name__ = "DisplayString"
_CsfUpgradeTFTPLoadFilename_Object = MibScalar
csfUpgradeTFTPLoadFilename = _CsfUpgradeTFTPLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 4),
    _CsfUpgradeTFTPLoadFilename_Type()
)
csfUpgradeTFTPLoadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeTFTPLoadFilename.setStatus("current")


class _CsfUpgradeTFTPInitiate_Type(Integer32):
    """Custom type csfUpgradeTFTPInitiate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upgrade", 1),
          ("noUpgrade", 2))
    )


_CsfUpgradeTFTPInitiate_Type.__name__ = "Integer32"
_CsfUpgradeTFTPInitiate_Object = MibScalar
csfUpgradeTFTPInitiate = _CsfUpgradeTFTPInitiate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 5),
    _CsfUpgradeTFTPInitiate_Type()
)
csfUpgradeTFTPInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeTFTPInitiate.setStatus("current")


class _CsfUpgradeFlashMode_Type(Integer32):
    """Custom type csfUpgradeFlashMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("temporary", 2))
    )


_CsfUpgradeFlashMode_Type.__name__ = "Integer32"
_CsfUpgradeFlashMode_Object = MibScalar
csfUpgradeFlashMode = _CsfUpgradeFlashMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 6),
    _CsfUpgradeFlashMode_Type()
)
csfUpgradeFlashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csfUpgradeFlashMode.setStatus("current")


class _CsfUpgradeFirmwareStatus_Type(Integer32):
    """Custom type csfUpgradeFirmwareStatus based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("inProgress", 2),
          ("succeeded", 3),
          ("failed", 4))
    )


_CsfUpgradeFirmwareStatus_Type.__name__ = "Integer32"
_CsfUpgradeFirmwareStatus_Object = MibScalar
csfUpgradeFirmwareStatus = _CsfUpgradeFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 1, 1, 7),
    _CsfUpgradeFirmwareStatus_Type()
)
csfUpgradeFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csfUpgradeFirmwareStatus.setStatus("current")
_CiscoSibuFlashMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBNotificationsPrefix = _CiscoSibuFlashMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 2)
)
_CiscoSibuFlashMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBNotifications = _CiscoSibuFlashMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 2, 0)
)
_CiscoSibuFlashMIBComformance_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBComformance = _CiscoSibuFlashMIBComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3)
)
_CiscoSibuFlashMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBCompliances = _CiscoSibuFlashMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1)
)
_CiscoSibuFlashMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSibuFlashMIBGroups = _CiscoSibuFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2)
)

# Managed Objects groups

ciscoSibuFlashMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 2, 1)
)
ciscoSibuFlashMIBGroup.setObjects(
      *(("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareVersion"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashSize"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPServerAddress"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPLoadFilename"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeTFTPInitiate"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFlashMode"),
        ("CISCO-SIBU-FLASH-MIB", "csfUpgradeFirmwareStatus"))
)
if mibBuilder.loadTexts:
    ciscoSibuFlashMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSibuFlashCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 45, 3, 1, 1)
)
ciscoSibuFlashCompliance.setObjects(
    ("CISCO-SIBU-FLASH-MIB", "ciscoSibuFlashMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoSibuFlashCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SIBU-FLASH-MIB",
    **{"ciscoSibuFlashMIB": ciscoSibuFlashMIB,
       "ciscoSibuFlashMIBObjects": ciscoSibuFlashMIBObjects,
       "csfUpgrade": csfUpgrade,
       "csfUpgradeFirmwareVersion": csfUpgradeFirmwareVersion,
       "csfUpgradeFlashSize": csfUpgradeFlashSize,
       "csfUpgradeTFTPServerAddress": csfUpgradeTFTPServerAddress,
       "csfUpgradeTFTPLoadFilename": csfUpgradeTFTPLoadFilename,
       "csfUpgradeTFTPInitiate": csfUpgradeTFTPInitiate,
       "csfUpgradeFlashMode": csfUpgradeFlashMode,
       "csfUpgradeFirmwareStatus": csfUpgradeFirmwareStatus,
       "ciscoSibuFlashMIBNotificationsPrefix": ciscoSibuFlashMIBNotificationsPrefix,
       "ciscoSibuFlashMIBNotifications": ciscoSibuFlashMIBNotifications,
       "ciscoSibuFlashMIBComformance": ciscoSibuFlashMIBComformance,
       "ciscoSibuFlashMIBCompliances": ciscoSibuFlashMIBCompliances,
       "ciscoSibuFlashCompliance": ciscoSibuFlashCompliance,
       "ciscoSibuFlashMIBGroups": ciscoSibuFlashMIBGroups,
       "ciscoSibuFlashMIBGroup": ciscoSibuFlashMIBGroup}
)
