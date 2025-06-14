# SNMP MIB module (CISCO-POE-PD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-POE-PD-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:25 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoPoePdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414)
)
if mibBuilder.loadTexts:
    ciscoPoePdMIB.setRevisions(
        ("2004-05-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CpoePdPowerSourceType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("acAdaptor", 2),
          ("thirdParty", 3),
          ("classic", 4),
          ("midspan", 5),
          ("cdpNegotiated", 6),
          ("highPowerClassic", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CpoePdMIBNotifications_ObjectIdentity = ObjectIdentity
cpoePdMIBNotifications = _CpoePdMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 0)
)
_CpoePdMIBObjects_ObjectIdentity = ObjectIdentity
cpoePdMIBObjects = _CpoePdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1)
)
_CpoePdInformation_ObjectIdentity = ObjectIdentity
cpoePdInformation = _CpoePdInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1)
)


class _CpoePdCurrentPowerLevel_Type(Unsigned32):
    """Custom type cpoePdCurrentPowerLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpoePdCurrentPowerLevel_Type.__name__ = "Unsigned32"
_CpoePdCurrentPowerLevel_Object = MibScalar
cpoePdCurrentPowerLevel = _CpoePdCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 1),
    _CpoePdCurrentPowerLevel_Type()
)
cpoePdCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpoePdCurrentPowerLevel.setStatus("current")
_CpoePdCurrentPowerSource_Type = CpoePdPowerSourceType
_CpoePdCurrentPowerSource_Object = MibScalar
cpoePdCurrentPowerSource = _CpoePdCurrentPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 2),
    _CpoePdCurrentPowerSource_Type()
)
cpoePdCurrentPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpoePdCurrentPowerSource.setStatus("current")
_CpoePdSupportedPowerLevelTable_Object = MibTable
cpoePdSupportedPowerLevelTable = _CpoePdSupportedPowerLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cpoePdSupportedPowerLevelTable.setStatus("current")
_CpoePdSupportedPowerLevelEntry_Object = MibTableRow
cpoePdSupportedPowerLevelEntry = _CpoePdSupportedPowerLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1)
)
cpoePdSupportedPowerLevelEntry.setIndexNames(
    (0, "CISCO-POE-PD-MIB", "cpoePdSupportedPowerLevel"),
)
if mibBuilder.loadTexts:
    cpoePdSupportedPowerLevelEntry.setStatus("current")


class _CpoePdSupportedPowerLevel_Type(Unsigned32):
    """Custom type cpoePdSupportedPowerLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpoePdSupportedPowerLevel_Type.__name__ = "Unsigned32"
_CpoePdSupportedPowerLevel_Object = MibTableColumn
cpoePdSupportedPowerLevel = _CpoePdSupportedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 1),
    _CpoePdSupportedPowerLevel_Type()
)
cpoePdSupportedPowerLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpoePdSupportedPowerLevel.setStatus("current")


class _CpoePdSupportedPower_Type(Unsigned32):
    """Custom type cpoePdSupportedPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpoePdSupportedPower_Type.__name__ = "Unsigned32"
_CpoePdSupportedPower_Object = MibTableColumn
cpoePdSupportedPower = _CpoePdSupportedPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 2),
    _CpoePdSupportedPower_Type()
)
cpoePdSupportedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpoePdSupportedPower.setStatus("current")
if mibBuilder.loadTexts:
    cpoePdSupportedPower.setUnits("milliwatts")
_CpoePdSupportedPowerMode_Type = SnmpAdminString
_CpoePdSupportedPowerMode_Object = MibTableColumn
cpoePdSupportedPowerMode = _CpoePdSupportedPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 3),
    _CpoePdSupportedPowerMode_Type()
)
cpoePdSupportedPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpoePdSupportedPowerMode.setStatus("current")
_CpoePdMIBConformance_ObjectIdentity = ObjectIdentity
cpoePdMIBConformance = _CpoePdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 2)
)
_CpoePdMIBCompliances_ObjectIdentity = ObjectIdentity
cpoePdMIBCompliances = _CpoePdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1)
)
_CpoePdMIBGroups_ObjectIdentity = ObjectIdentity
cpoePdMIBGroups = _CpoePdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2)
)

# Managed Objects groups

cpoePdInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2, 1)
)
cpoePdInformationGroup.setObjects(
      *(("CISCO-POE-PD-MIB", "cpoePdCurrentPowerLevel"),
        ("CISCO-POE-PD-MIB", "cpoePdCurrentPowerSource"),
        ("CISCO-POE-PD-MIB", "cpoePdSupportedPower"),
        ("CISCO-POE-PD-MIB", "cpoePdSupportedPowerMode"))
)
if mibBuilder.loadTexts:
    cpoePdInformationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpoePdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1, 1)
)
cpoePdMIBCompliance.setObjects(
    ("CISCO-POE-PD-MIB", "cpoePdInformationGroup")
)
if mibBuilder.loadTexts:
    cpoePdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-POE-PD-MIB",
    **{"CpoePdPowerSourceType": CpoePdPowerSourceType,
       "ciscoPoePdMIB": ciscoPoePdMIB,
       "cpoePdMIBNotifications": cpoePdMIBNotifications,
       "cpoePdMIBObjects": cpoePdMIBObjects,
       "cpoePdInformation": cpoePdInformation,
       "cpoePdCurrentPowerLevel": cpoePdCurrentPowerLevel,
       "cpoePdCurrentPowerSource": cpoePdCurrentPowerSource,
       "cpoePdSupportedPowerLevelTable": cpoePdSupportedPowerLevelTable,
       "cpoePdSupportedPowerLevelEntry": cpoePdSupportedPowerLevelEntry,
       "cpoePdSupportedPowerLevel": cpoePdSupportedPowerLevel,
       "cpoePdSupportedPower": cpoePdSupportedPower,
       "cpoePdSupportedPowerMode": cpoePdSupportedPowerMode,
       "cpoePdMIBConformance": cpoePdMIBConformance,
       "cpoePdMIBCompliances": cpoePdMIBCompliances,
       "cpoePdMIBCompliance": cpoePdMIBCompliance,
       "cpoePdMIBGroups": cpoePdMIBGroups,
       "cpoePdInformationGroup": cpoePdInformationGroup}
)
