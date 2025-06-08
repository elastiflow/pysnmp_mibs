# SNMP MIB module (CISCO-WLAN-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-WLAN-VLAN-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:16 2025
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

(CDot11IfMicAlgorithm,
 CDot11IfWepKeyPermuteAlgorithm,
 WepKeyType128) = mibBuilder.importSymbols(
    "CISCO-DOT11-IF-MIB",
    "CDot11IfMicAlgorithm",
    "CDot11IfWepKeyPermuteAlgorithm",
    "WepKeyType128")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWlanVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268)
)
if mibBuilder.loadTexts:
    ciscoWlanVlanMIB.setRevisions(
        ("2002-06-12 00:00",
         "2002-04-04 00:00",
         "2002-03-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CwvlVlanIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWlanVlanMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoWlanVlanMIBNotifications = _CiscoWlanVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 0)
)
_CiscoWlanVlanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWlanVlanMIBObjects = _CiscoWlanVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1)
)
_CwvlRoamDomainConfig_ObjectIdentity = ObjectIdentity
cwvlRoamDomainConfig = _CwvlRoamDomainConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1)
)


class _CwvlWlanDot1qEncapEnabled_Type(TruthValue):
    """Custom type cwvlWlanDot1qEncapEnabled based on TruthValue"""
    defaultValue = 2


_CwvlWlanDot1qEncapEnabled_Type.__name__ = "TruthValue"
_CwvlWlanDot1qEncapEnabled_Object = MibScalar
cwvlWlanDot1qEncapEnabled = _CwvlWlanDot1qEncapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 1),
    _CwvlWlanDot1qEncapEnabled_Type()
)
cwvlWlanDot1qEncapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlWlanDot1qEncapEnabled.setStatus("current")


class _CwvlBridgingNativeVlanId_Type(CwvlVlanIdOrZero):
    """Custom type cwvlBridgingNativeVlanId based on CwvlVlanIdOrZero"""
    defaultValue = 0


_CwvlBridgingNativeVlanId_Type.__name__ = "CwvlVlanIdOrZero"
_CwvlBridgingNativeVlanId_Object = MibScalar
cwvlBridgingNativeVlanId = _CwvlBridgingNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 2),
    _CwvlBridgingNativeVlanId_Type()
)
cwvlBridgingNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlBridgingNativeVlanId.setStatus("current")


class _CwvlVoIPVlanEnabled_Type(TruthValue):
    """Custom type cwvlVoIPVlanEnabled based on TruthValue"""
    defaultValue = 1


_CwvlVoIPVlanEnabled_Type.__name__ = "TruthValue"
_CwvlVoIPVlanEnabled_Object = MibScalar
cwvlVoIPVlanEnabled = _CwvlVoIPVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 3),
    _CwvlVoIPVlanEnabled_Type()
)
cwvlVoIPVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlVoIPVlanEnabled.setStatus("current")


class _CwvlVoIPVlanId_Type(CwvlVlanIdOrZero):
    """Custom type cwvlVoIPVlanId based on CwvlVlanIdOrZero"""
    defaultValue = 4095


_CwvlVoIPVlanId_Type.__name__ = "CwvlVlanIdOrZero"
_CwvlVoIPVlanId_Object = MibScalar
cwvlVoIPVlanId = _CwvlVoIPVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 4),
    _CwvlVoIPVlanId_Type()
)
cwvlVoIPVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlVoIPVlanId.setStatus("current")


class _CwvlPublicVlanId_Type(CwvlVlanIdOrZero):
    """Custom type cwvlPublicVlanId based on CwvlVlanIdOrZero"""
    defaultValue = 0


_CwvlPublicVlanId_Type.__name__ = "CwvlVlanIdOrZero"
_CwvlPublicVlanId_Object = MibScalar
cwvlPublicVlanId = _CwvlPublicVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 1, 5),
    _CwvlPublicVlanId_Type()
)
cwvlPublicVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlPublicVlanId.setStatus("current")
_CwvlDot11VlanConfig_ObjectIdentity = ObjectIdentity
cwvlDot11VlanConfig = _CwvlDot11VlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2)
)
_CwvlWlanVlanTable_Object = MibTable
cwvlWlanVlanTable = _CwvlWlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwvlWlanVlanTable.setStatus("current")
_CwvlWlanVlanEntry_Object = MibTableRow
cwvlWlanVlanEntry = _CwvlWlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1)
)
cwvlWlanVlanEntry.setIndexNames(
    (0, "CISCO-WLAN-VLAN-MIB", "cwvlWlanVlanId"),
)
if mibBuilder.loadTexts:
    cwvlWlanVlanEntry.setStatus("current")
_CwvlWlanVlanId_Type = CwvlVlanIdOrZero
_CwvlWlanVlanId_Object = MibTableColumn
cwvlWlanVlanId = _CwvlWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 1),
    _CwvlWlanVlanId_Type()
)
cwvlWlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwvlWlanVlanId.setStatus("current")


class _CwvlWlanEnabled_Type(TruthValue):
    """Custom type cwvlWlanEnabled based on TruthValue"""
    defaultValue = 1


_CwvlWlanEnabled_Type.__name__ = "TruthValue"
_CwvlWlanEnabled_Object = MibTableColumn
cwvlWlanEnabled = _CwvlWlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 2),
    _CwvlWlanEnabled_Type()
)
cwvlWlanEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanEnabled.setStatus("current")


class _CwvlWlanNUcastKeyRotateInterval_Type(Unsigned32):
    """Custom type cwvlWlanNUcastKeyRotateInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_CwvlWlanNUcastKeyRotateInterval_Type.__name__ = "Unsigned32"
_CwvlWlanNUcastKeyRotateInterval_Object = MibTableColumn
cwvlWlanNUcastKeyRotateInterval = _CwvlWlanNUcastKeyRotateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 3),
    _CwvlWlanNUcastKeyRotateInterval_Type()
)
cwvlWlanNUcastKeyRotateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyRotateInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyRotateInterval.setUnits("seconds")


class _CwvlWlanEncryptionMode_Type(Integer32):
    """Custom type cwvlWlanEncryptionMode based on Integer32"""
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
        *(("none", 1),
          ("wep", 2),
          ("aes", 3))
    )


_CwvlWlanEncryptionMode_Type.__name__ = "Integer32"
_CwvlWlanEncryptionMode_Object = MibTableColumn
cwvlWlanEncryptionMode = _CwvlWlanEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 4),
    _CwvlWlanEncryptionMode_Type()
)
cwvlWlanEncryptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanEncryptionMode.setStatus("current")


class _CwvlWlanEncryptionMandatory_Type(TruthValue):
    """Custom type cwvlWlanEncryptionMandatory based on TruthValue"""
    defaultValue = 1


_CwvlWlanEncryptionMandatory_Type.__name__ = "TruthValue"
_CwvlWlanEncryptionMandatory_Object = MibTableColumn
cwvlWlanEncryptionMandatory = _CwvlWlanEncryptionMandatory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 5),
    _CwvlWlanEncryptionMandatory_Type()
)
cwvlWlanEncryptionMandatory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanEncryptionMandatory.setStatus("current")


class _CwvlWlanMicAlgorithm_Type(CDot11IfMicAlgorithm):
    """Custom type cwvlWlanMicAlgorithm based on CDot11IfMicAlgorithm"""
    defaultValue = 1


_CwvlWlanMicAlgorithm_Type.__name__ = "CDot11IfMicAlgorithm"
_CwvlWlanMicAlgorithm_Object = MibTableColumn
cwvlWlanMicAlgorithm = _CwvlWlanMicAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 6),
    _CwvlWlanMicAlgorithm_Type()
)
cwvlWlanMicAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanMicAlgorithm.setStatus("current")


class _CwvlWlanWepKeyPermuteAlgorithm_Type(CDot11IfWepKeyPermuteAlgorithm):
    """Custom type cwvlWlanWepKeyPermuteAlgorithm based on CDot11IfWepKeyPermuteAlgorithm"""
    defaultValue = 1


_CwvlWlanWepKeyPermuteAlgorithm_Type.__name__ = "CDot11IfWepKeyPermuteAlgorithm"
_CwvlWlanWepKeyPermuteAlgorithm_Object = MibTableColumn
cwvlWlanWepKeyPermuteAlgorithm = _CwvlWlanWepKeyPermuteAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 7),
    _CwvlWlanWepKeyPermuteAlgorithm_Type()
)
cwvlWlanWepKeyPermuteAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanWepKeyPermuteAlgorithm.setStatus("current")


class _CwvlWlanWepKeyHashing_Type(TruthValue):
    """Custom type cwvlWlanWepKeyHashing based on TruthValue"""
    defaultValue = 2


_CwvlWlanWepKeyHashing_Type.__name__ = "TruthValue"
_CwvlWlanWepKeyHashing_Object = MibTableColumn
cwvlWlanWepKeyHashing = _CwvlWlanWepKeyHashing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 8),
    _CwvlWlanWepKeyHashing_Type()
)
cwvlWlanWepKeyHashing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanWepKeyHashing.setStatus("current")


class _CwvlWlanEncryptionAlgorithm_Type(Integer32):
    """Custom type cwvlWlanEncryptionAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("cisco", 2))
    )


_CwvlWlanEncryptionAlgorithm_Type.__name__ = "Integer32"
_CwvlWlanEncryptionAlgorithm_Object = MibTableColumn
cwvlWlanEncryptionAlgorithm = _CwvlWlanEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 9),
    _CwvlWlanEncryptionAlgorithm_Type()
)
cwvlWlanEncryptionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanEncryptionAlgorithm.setStatus("current")
_CwvlWlanRowStatus_Type = RowStatus
_CwvlWlanRowStatus_Object = MibTableColumn
cwvlWlanRowStatus = _CwvlWlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 1, 1, 10),
    _CwvlWlanRowStatus_Type()
)
cwvlWlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwvlWlanRowStatus.setStatus("current")
_CwvlWlanNUcastKeyTable_Object = MibTable
cwvlWlanNUcastKeyTable = _CwvlWlanNUcastKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyTable.setStatus("current")
_CwvlWlanNUcastKeyEntry_Object = MibTableRow
cwvlWlanNUcastKeyEntry = _CwvlWlanNUcastKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1)
)
cwvlWlanNUcastKeyEntry.setIndexNames(
    (0, "CISCO-WLAN-VLAN-MIB", "cwvlWlanVlanId"),
    (0, "CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyIndex"),
)
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyEntry.setStatus("current")


class _CwvlWlanNUcastKeyIndex_Type(Unsigned32):
    """Custom type cwvlWlanNUcastKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CwvlWlanNUcastKeyIndex_Type.__name__ = "Unsigned32"
_CwvlWlanNUcastKeyIndex_Object = MibTableColumn
cwvlWlanNUcastKeyIndex = _CwvlWlanNUcastKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1, 1),
    _CwvlWlanNUcastKeyIndex_Type()
)
cwvlWlanNUcastKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyIndex.setStatus("current")


class _CwvlWlanNUcastKeyLen_Type(Unsigned32):
    """Custom type cwvlWlanNUcastKeyLen based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_CwvlWlanNUcastKeyLen_Type.__name__ = "Unsigned32"
_CwvlWlanNUcastKeyLen_Object = MibTableColumn
cwvlWlanNUcastKeyLen = _CwvlWlanNUcastKeyLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1, 2),
    _CwvlWlanNUcastKeyLen_Type()
)
cwvlWlanNUcastKeyLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyLen.setStatus("current")
_CwvlWlanNUcastKeyValue_Type = WepKeyType128
_CwvlWlanNUcastKeyValue_Object = MibTableColumn
cwvlWlanNUcastKeyValue = _CwvlWlanNUcastKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 2, 1, 3),
    _CwvlWlanNUcastKeyValue_Type()
)
cwvlWlanNUcastKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlWlanNUcastKeyValue.setStatus("current")


class _CwvlWlanWepChangeNotifEnabled_Type(TruthValue):
    """Custom type cwvlWlanWepChangeNotifEnabled based on TruthValue"""
    defaultValue = 2


_CwvlWlanWepChangeNotifEnabled_Type.__name__ = "TruthValue"
_CwvlWlanWepChangeNotifEnabled_Object = MibScalar
cwvlWlanWepChangeNotifEnabled = _CwvlWlanWepChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 1, 2, 3),
    _CwvlWlanWepChangeNotifEnabled_Type()
)
cwvlWlanWepChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwvlWlanWepChangeNotifEnabled.setStatus("current")
_CiscoWlanVlanMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWlanVlanMIBConformance = _CiscoWlanVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2)
)
_CiscoWlanVlanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWlanVlanMIBCompliances = _CiscoWlanVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 1)
)
_CiscoWlanVlanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWlanVlanMIBGroups = _CiscoWlanVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2)
)

# Managed Objects groups

ciscoWlanRoamDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2, 1)
)
ciscoWlanRoamDomainGroup.setObjects(
      *(("CISCO-WLAN-VLAN-MIB", "cwvlWlanDot1qEncapEnabled"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlBridgingNativeVlanId"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlVoIPVlanEnabled"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlVoIPVlanId"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlPublicVlanId"))
)
if mibBuilder.loadTexts:
    ciscoWlanRoamDomainGroup.setStatus("current")

ciscoWlanDot11VlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2, 2)
)
ciscoWlanDot11VlanConfigGroup.setObjects(
      *(("CISCO-WLAN-VLAN-MIB", "cwvlWlanEnabled"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyRotateInterval"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanEncryptionMode"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanEncryptionMandatory"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanMicAlgorithm"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanWepKeyPermuteAlgorithm"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanWepKeyHashing"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanEncryptionAlgorithm"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanRowStatus"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyLen"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyValue"),
        ("CISCO-WLAN-VLAN-MIB", "cwvlWlanWepChangeNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoWlanDot11VlanConfigGroup.setStatus("current")


# Notification objects

ciscoWlanVlanWepChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 0, 1)
)
ciscoWlanVlanWepChangeNotif.setObjects(
    ("CISCO-WLAN-VLAN-MIB", "cwvlWlanNUcastKeyValue")
)
if mibBuilder.loadTexts:
    ciscoWlanVlanWepChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoWlanVlanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 2, 3)
)
ciscoWlanVlanNotificationGroup.setObjects(
    ("CISCO-WLAN-VLAN-MIB", "ciscoWlanVlanWepChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoWlanVlanNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWlanVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 268, 2, 1, 1)
)
ciscoWlanVlanMIBCompliance.setObjects(
      *(("CISCO-WLAN-VLAN-MIB", "ciscoWlanRoamDomainGroup"),
        ("CISCO-WLAN-VLAN-MIB", "ciscoWlanVlanNotificationGroup"),
        ("CISCO-WLAN-VLAN-MIB", "ciscoWlanDot11VlanConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoWlanVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WLAN-VLAN-MIB",
    **{"CwvlVlanIdOrZero": CwvlVlanIdOrZero,
       "ciscoWlanVlanMIB": ciscoWlanVlanMIB,
       "ciscoWlanVlanMIBNotifications": ciscoWlanVlanMIBNotifications,
       "ciscoWlanVlanWepChangeNotif": ciscoWlanVlanWepChangeNotif,
       "ciscoWlanVlanMIBObjects": ciscoWlanVlanMIBObjects,
       "cwvlRoamDomainConfig": cwvlRoamDomainConfig,
       "cwvlWlanDot1qEncapEnabled": cwvlWlanDot1qEncapEnabled,
       "cwvlBridgingNativeVlanId": cwvlBridgingNativeVlanId,
       "cwvlVoIPVlanEnabled": cwvlVoIPVlanEnabled,
       "cwvlVoIPVlanId": cwvlVoIPVlanId,
       "cwvlPublicVlanId": cwvlPublicVlanId,
       "cwvlDot11VlanConfig": cwvlDot11VlanConfig,
       "cwvlWlanVlanTable": cwvlWlanVlanTable,
       "cwvlWlanVlanEntry": cwvlWlanVlanEntry,
       "cwvlWlanVlanId": cwvlWlanVlanId,
       "cwvlWlanEnabled": cwvlWlanEnabled,
       "cwvlWlanNUcastKeyRotateInterval": cwvlWlanNUcastKeyRotateInterval,
       "cwvlWlanEncryptionMode": cwvlWlanEncryptionMode,
       "cwvlWlanEncryptionMandatory": cwvlWlanEncryptionMandatory,
       "cwvlWlanMicAlgorithm": cwvlWlanMicAlgorithm,
       "cwvlWlanWepKeyPermuteAlgorithm": cwvlWlanWepKeyPermuteAlgorithm,
       "cwvlWlanWepKeyHashing": cwvlWlanWepKeyHashing,
       "cwvlWlanEncryptionAlgorithm": cwvlWlanEncryptionAlgorithm,
       "cwvlWlanRowStatus": cwvlWlanRowStatus,
       "cwvlWlanNUcastKeyTable": cwvlWlanNUcastKeyTable,
       "cwvlWlanNUcastKeyEntry": cwvlWlanNUcastKeyEntry,
       "cwvlWlanNUcastKeyIndex": cwvlWlanNUcastKeyIndex,
       "cwvlWlanNUcastKeyLen": cwvlWlanNUcastKeyLen,
       "cwvlWlanNUcastKeyValue": cwvlWlanNUcastKeyValue,
       "cwvlWlanWepChangeNotifEnabled": cwvlWlanWepChangeNotifEnabled,
       "ciscoWlanVlanMIBConformance": ciscoWlanVlanMIBConformance,
       "ciscoWlanVlanMIBCompliances": ciscoWlanVlanMIBCompliances,
       "ciscoWlanVlanMIBCompliance": ciscoWlanVlanMIBCompliance,
       "ciscoWlanVlanMIBGroups": ciscoWlanVlanMIBGroups,
       "ciscoWlanRoamDomainGroup": ciscoWlanRoamDomainGroup,
       "ciscoWlanDot11VlanConfigGroup": ciscoWlanDot11VlanConfigGroup,
       "ciscoWlanVlanNotificationGroup": ciscoWlanVlanNotificationGroup}
)
