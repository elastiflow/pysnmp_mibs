# SNMP MIB module (DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_40288/DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:50:32 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

(KeyChange,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "KeyChange")

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

dpsInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 2)
)
if mibBuilder.loadTexts:
    dpsInfo.setRevisions(
        ("2013-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DPSUsmAuthPrivProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAuthProtocol", 1),
          ("hmacMD5Auth", 2),
          ("hmacSHAAuth", 3),
          ("noPrivProtocol", 4),
          ("desPrivProtocol", 5),
          ("aesPrivProtocol", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Deltapowersolutions_ObjectIdentity = ObjectIdentity
deltapowersolutions = _Deltapowersolutions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1)
)
_Root_ObjectIdentity = ObjectIdentity
root = _Root_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2)
)
_Ipv4TrapTable_Object = MibTable
ipv4TrapTable = _Ipv4TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipv4TrapTable.setStatus("current")
_Ipv4TrapEntry_Object = MibTableRow
ipv4TrapEntry = _Ipv4TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 1, 1)
)
ipv4TrapEntry.setIndexNames(
    (0, "DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "ipv4TrapReceiverNumber"),
)
if mibBuilder.loadTexts:
    ipv4TrapEntry.setStatus("current")


class _Ipv4TrapReceiverNumber_Type(Integer32):
    """Custom type ipv4TrapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Ipv4TrapReceiverNumber_Type.__name__ = "Integer32"
_Ipv4TrapReceiverNumber_Object = MibTableColumn
ipv4TrapReceiverNumber = _Ipv4TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 1, 1, 1),
    _Ipv4TrapReceiverNumber_Type()
)
ipv4TrapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv4TrapReceiverNumber.setStatus("current")


class _Ipv4TrapEnabled_Type(Integer32):
    """Custom type ipv4TrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ipv4TrapEnabled_Type.__name__ = "Integer32"
_Ipv4TrapEnabled_Object = MibTableColumn
ipv4TrapEnabled = _Ipv4TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 1, 1, 2),
    _Ipv4TrapEnabled_Type()
)
ipv4TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapEnabled.setStatus("current")
_Ipv4TrapReceiverIPAddress_Type = IpAddress
_Ipv4TrapReceiverIPAddress_Object = MibTableColumn
ipv4TrapReceiverIPAddress = _Ipv4TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 1, 1, 3),
    _Ipv4TrapReceiverIPAddress_Type()
)
ipv4TrapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapReceiverIPAddress.setStatus("current")


class _Ipv4TrapCommunity_Type(DisplayString):
    """Custom type ipv4TrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Ipv4TrapCommunity_Type.__name__ = "DisplayString"
_Ipv4TrapCommunity_Object = MibTableColumn
ipv4TrapCommunity = _Ipv4TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 1, 1, 4),
    _Ipv4TrapCommunity_Type()
)
ipv4TrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapCommunity.setStatus("current")


class _Siteid_Type(DisplayString):
    """Custom type siteid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Siteid_Type.__name__ = "DisplayString"
_Siteid_Object = MibScalar
siteid = _Siteid_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 2),
    _Siteid_Type()
)
siteid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteid.setStatus("current")
_Ipv6TrapTable_Object = MibTable
ipv6TrapTable = _Ipv6TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipv6TrapTable.setStatus("current")
_Ipv6TrapEntry_Object = MibTableRow
ipv6TrapEntry = _Ipv6TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 3, 1)
)
ipv6TrapEntry.setIndexNames(
    (0, "DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "ipv6TrapReceiverNumber"),
)
if mibBuilder.loadTexts:
    ipv6TrapEntry.setStatus("current")


class _Ipv6TrapReceiverNumber_Type(Integer32):
    """Custom type ipv6TrapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Ipv6TrapReceiverNumber_Type.__name__ = "Integer32"
_Ipv6TrapReceiverNumber_Object = MibTableColumn
ipv6TrapReceiverNumber = _Ipv6TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 3, 1, 1),
    _Ipv6TrapReceiverNumber_Type()
)
ipv6TrapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6TrapReceiverNumber.setStatus("current")


class _Ipv6TrapEnabled_Type(Integer32):
    """Custom type ipv6TrapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Ipv6TrapEnabled_Type.__name__ = "Integer32"
_Ipv6TrapEnabled_Object = MibTableColumn
ipv6TrapEnabled = _Ipv6TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 3, 1, 2),
    _Ipv6TrapEnabled_Type()
)
ipv6TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6TrapEnabled.setStatus("current")


class _Ipv6TrapReceiverIPv6Address_Type(DisplayString):
    """Custom type ipv6TrapReceiverIPv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_Ipv6TrapReceiverIPv6Address_Type.__name__ = "DisplayString"
_Ipv6TrapReceiverIPv6Address_Object = MibTableColumn
ipv6TrapReceiverIPv6Address = _Ipv6TrapReceiverIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 3, 1, 3),
    _Ipv6TrapReceiverIPv6Address_Type()
)
ipv6TrapReceiverIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6TrapReceiverIPv6Address.setStatus("current")


class _Ipv6TrapCommunity_Type(DisplayString):
    """Custom type ipv6TrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Ipv6TrapCommunity_Type.__name__ = "DisplayString"
_Ipv6TrapCommunity_Object = MibTableColumn
ipv6TrapCommunity = _Ipv6TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 2, 3, 1, 4),
    _Ipv6TrapCommunity_Type()
)
ipv6TrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6TrapCommunity.setStatus("current")
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3)
)
_EAlarms_ObjectIdentity = ObjectIdentity
eAlarms = _EAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1)
)
_EAlarmsGp_ObjectIdentity = ObjectIdentity
eAlarmsGp = _EAlarmsGp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1)
)


class _ECellOverVolProtectionMod1_Type(Integer32):
    """Custom type eCellOverVolProtectionMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod1_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod1_Object = MibScalar
eCellOverVolProtectionMod1 = _ECellOverVolProtectionMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 1),
    _ECellOverVolProtectionMod1_Type()
)
eCellOverVolProtectionMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod1.setStatus("current")


class _ECellOverVolProtectionMod2_Type(Integer32):
    """Custom type eCellOverVolProtectionMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod2_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod2_Object = MibScalar
eCellOverVolProtectionMod2 = _ECellOverVolProtectionMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 2),
    _ECellOverVolProtectionMod2_Type()
)
eCellOverVolProtectionMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod2.setStatus("current")


class _ECellOverVolProtectionMod3_Type(Integer32):
    """Custom type eCellOverVolProtectionMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod3_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod3_Object = MibScalar
eCellOverVolProtectionMod3 = _ECellOverVolProtectionMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 3),
    _ECellOverVolProtectionMod3_Type()
)
eCellOverVolProtectionMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod3.setStatus("current")


class _ECellOverVolProtectionMod4_Type(Integer32):
    """Custom type eCellOverVolProtectionMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod4_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod4_Object = MibScalar
eCellOverVolProtectionMod4 = _ECellOverVolProtectionMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 4),
    _ECellOverVolProtectionMod4_Type()
)
eCellOverVolProtectionMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod4.setStatus("current")


class _ECellOverVolProtectionMod5_Type(Integer32):
    """Custom type eCellOverVolProtectionMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod5_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod5_Object = MibScalar
eCellOverVolProtectionMod5 = _ECellOverVolProtectionMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 5),
    _ECellOverVolProtectionMod5_Type()
)
eCellOverVolProtectionMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod5.setStatus("current")


class _ECellOverVolProtectionMod6_Type(Integer32):
    """Custom type eCellOverVolProtectionMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod6_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod6_Object = MibScalar
eCellOverVolProtectionMod6 = _ECellOverVolProtectionMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 6),
    _ECellOverVolProtectionMod6_Type()
)
eCellOverVolProtectionMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod6.setStatus("current")


class _ECellOverVolProtectionMod7_Type(Integer32):
    """Custom type eCellOverVolProtectionMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod7_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod7_Object = MibScalar
eCellOverVolProtectionMod7 = _ECellOverVolProtectionMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 7),
    _ECellOverVolProtectionMod7_Type()
)
eCellOverVolProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod7.setStatus("current")


class _ECellUnderVolProtectionMod1_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod1_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod1_Object = MibScalar
eCellUnderVolProtectionMod1 = _ECellUnderVolProtectionMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 8),
    _ECellUnderVolProtectionMod1_Type()
)
eCellUnderVolProtectionMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod1.setStatus("current")


class _ECellUnderVolProtectionMod2_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod2_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod2_Object = MibScalar
eCellUnderVolProtectionMod2 = _ECellUnderVolProtectionMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 9),
    _ECellUnderVolProtectionMod2_Type()
)
eCellUnderVolProtectionMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod2.setStatus("current")


class _ECellUnderVolProtectionMod3_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod3_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod3_Object = MibScalar
eCellUnderVolProtectionMod3 = _ECellUnderVolProtectionMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 10),
    _ECellUnderVolProtectionMod3_Type()
)
eCellUnderVolProtectionMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod3.setStatus("current")


class _ECellUnderVolProtectionMod4_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod4_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod4_Object = MibScalar
eCellUnderVolProtectionMod4 = _ECellUnderVolProtectionMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 11),
    _ECellUnderVolProtectionMod4_Type()
)
eCellUnderVolProtectionMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod4.setStatus("current")


class _ECellUnderVolProtectionMod5_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod5_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod5_Object = MibScalar
eCellUnderVolProtectionMod5 = _ECellUnderVolProtectionMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 12),
    _ECellUnderVolProtectionMod5_Type()
)
eCellUnderVolProtectionMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod5.setStatus("current")


class _ECellUnderVolProtectionMod6_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod6_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod6_Object = MibScalar
eCellUnderVolProtectionMod6 = _ECellUnderVolProtectionMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 13),
    _ECellUnderVolProtectionMod6_Type()
)
eCellUnderVolProtectionMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod6.setStatus("current")


class _ECellUnderVolProtectionMod7_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod7_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod7_Object = MibScalar
eCellUnderVolProtectionMod7 = _ECellUnderVolProtectionMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 14),
    _ECellUnderVolProtectionMod7_Type()
)
eCellUnderVolProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod7.setStatus("current")


class _EModuleCellUnbalancedMod1_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod1_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod1_Object = MibScalar
eModuleCellUnbalancedMod1 = _EModuleCellUnbalancedMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 15),
    _EModuleCellUnbalancedMod1_Type()
)
eModuleCellUnbalancedMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod1.setStatus("current")


class _EModuleCellUnbalancedMod2_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod2_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod2_Object = MibScalar
eModuleCellUnbalancedMod2 = _EModuleCellUnbalancedMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 16),
    _EModuleCellUnbalancedMod2_Type()
)
eModuleCellUnbalancedMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod2.setStatus("current")


class _EModuleCellUnbalancedMod3_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod3_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod3_Object = MibScalar
eModuleCellUnbalancedMod3 = _EModuleCellUnbalancedMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 17),
    _EModuleCellUnbalancedMod3_Type()
)
eModuleCellUnbalancedMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod3.setStatus("current")


class _EModuleCellUnbalancedMod4_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod4_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod4_Object = MibScalar
eModuleCellUnbalancedMod4 = _EModuleCellUnbalancedMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 18),
    _EModuleCellUnbalancedMod4_Type()
)
eModuleCellUnbalancedMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod4.setStatus("current")


class _EModuleCellUnbalancedMod5_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod5_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod5_Object = MibScalar
eModuleCellUnbalancedMod5 = _EModuleCellUnbalancedMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 19),
    _EModuleCellUnbalancedMod5_Type()
)
eModuleCellUnbalancedMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod5.setStatus("current")


class _EModuleCellUnbalancedMod6_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod6_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod6_Object = MibScalar
eModuleCellUnbalancedMod6 = _EModuleCellUnbalancedMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 20),
    _EModuleCellUnbalancedMod6_Type()
)
eModuleCellUnbalancedMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod6.setStatus("current")


class _EModuleCellUnbalancedMod7_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod7_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod7_Object = MibScalar
eModuleCellUnbalancedMod7 = _EModuleCellUnbalancedMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 21),
    _EModuleCellUnbalancedMod7_Type()
)
eModuleCellUnbalancedMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod7.setStatus("current")


class _EBattUnderVolWarningMod1_Type(Integer32):
    """Custom type eBattUnderVolWarningMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod1_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod1_Object = MibScalar
eBattUnderVolWarningMod1 = _EBattUnderVolWarningMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 22),
    _EBattUnderVolWarningMod1_Type()
)
eBattUnderVolWarningMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod1.setStatus("current")


class _EBattUnderVolWarningMod2_Type(Integer32):
    """Custom type eBattUnderVolWarningMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod2_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod2_Object = MibScalar
eBattUnderVolWarningMod2 = _EBattUnderVolWarningMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 23),
    _EBattUnderVolWarningMod2_Type()
)
eBattUnderVolWarningMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod2.setStatus("current")


class _EBattUnderVolWarningMod3_Type(Integer32):
    """Custom type eBattUnderVolWarningMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod3_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod3_Object = MibScalar
eBattUnderVolWarningMod3 = _EBattUnderVolWarningMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 24),
    _EBattUnderVolWarningMod3_Type()
)
eBattUnderVolWarningMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod3.setStatus("current")


class _EBattUnderVolWarningMod4_Type(Integer32):
    """Custom type eBattUnderVolWarningMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod4_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod4_Object = MibScalar
eBattUnderVolWarningMod4 = _EBattUnderVolWarningMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 25),
    _EBattUnderVolWarningMod4_Type()
)
eBattUnderVolWarningMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod4.setStatus("current")


class _EBattUnderVolWarningMod5_Type(Integer32):
    """Custom type eBattUnderVolWarningMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod5_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod5_Object = MibScalar
eBattUnderVolWarningMod5 = _EBattUnderVolWarningMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 26),
    _EBattUnderVolWarningMod5_Type()
)
eBattUnderVolWarningMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod5.setStatus("current")


class _EBattUnderVolWarningMod6_Type(Integer32):
    """Custom type eBattUnderVolWarningMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod6_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod6_Object = MibScalar
eBattUnderVolWarningMod6 = _EBattUnderVolWarningMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 27),
    _EBattUnderVolWarningMod6_Type()
)
eBattUnderVolWarningMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod6.setStatus("current")


class _EBattUnderVolWarningMod7_Type(Integer32):
    """Custom type eBattUnderVolWarningMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod7_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod7_Object = MibScalar
eBattUnderVolWarningMod7 = _EBattUnderVolWarningMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 28),
    _EBattUnderVolWarningMod7_Type()
)
eBattUnderVolWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod7.setStatus("current")


class _EBattOverVolWarningMod1_Type(Integer32):
    """Custom type eBattOverVolWarningMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod1_Type.__name__ = "Integer32"
_EBattOverVolWarningMod1_Object = MibScalar
eBattOverVolWarningMod1 = _EBattOverVolWarningMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 29),
    _EBattOverVolWarningMod1_Type()
)
eBattOverVolWarningMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod1.setStatus("current")


class _EBattOverVolWarningMod2_Type(Integer32):
    """Custom type eBattOverVolWarningMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod2_Type.__name__ = "Integer32"
_EBattOverVolWarningMod2_Object = MibScalar
eBattOverVolWarningMod2 = _EBattOverVolWarningMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 30),
    _EBattOverVolWarningMod2_Type()
)
eBattOverVolWarningMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod2.setStatus("current")


class _EBattOverVolWarningMod3_Type(Integer32):
    """Custom type eBattOverVolWarningMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod3_Type.__name__ = "Integer32"
_EBattOverVolWarningMod3_Object = MibScalar
eBattOverVolWarningMod3 = _EBattOverVolWarningMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 31),
    _EBattOverVolWarningMod3_Type()
)
eBattOverVolWarningMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod3.setStatus("current")


class _EBattOverVolWarningMod4_Type(Integer32):
    """Custom type eBattOverVolWarningMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod4_Type.__name__ = "Integer32"
_EBattOverVolWarningMod4_Object = MibScalar
eBattOverVolWarningMod4 = _EBattOverVolWarningMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 32),
    _EBattOverVolWarningMod4_Type()
)
eBattOverVolWarningMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod4.setStatus("current")


class _EBattOverVolWarningMod5_Type(Integer32):
    """Custom type eBattOverVolWarningMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod5_Type.__name__ = "Integer32"
_EBattOverVolWarningMod5_Object = MibScalar
eBattOverVolWarningMod5 = _EBattOverVolWarningMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 33),
    _EBattOverVolWarningMod5_Type()
)
eBattOverVolWarningMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod5.setStatus("current")


class _EBattOverVolWarningMod6_Type(Integer32):
    """Custom type eBattOverVolWarningMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod6_Type.__name__ = "Integer32"
_EBattOverVolWarningMod6_Object = MibScalar
eBattOverVolWarningMod6 = _EBattOverVolWarningMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 34),
    _EBattOverVolWarningMod6_Type()
)
eBattOverVolWarningMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod6.setStatus("current")


class _EBattOverVolWarningMod7_Type(Integer32):
    """Custom type eBattOverVolWarningMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod7_Type.__name__ = "Integer32"
_EBattOverVolWarningMod7_Object = MibScalar
eBattOverVolWarningMod7 = _EBattOverVolWarningMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 35),
    _EBattOverVolWarningMod7_Type()
)
eBattOverVolWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod7.setStatus("current")


class _ECellChgOverTempProtMod1_Type(Integer32):
    """Custom type eCellChgOverTempProtMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod1_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod1_Object = MibScalar
eCellChgOverTempProtMod1 = _ECellChgOverTempProtMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 36),
    _ECellChgOverTempProtMod1_Type()
)
eCellChgOverTempProtMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod1.setStatus("current")


class _ECellChgOverTempProtMod2_Type(Integer32):
    """Custom type eCellChgOverTempProtMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod2_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod2_Object = MibScalar
eCellChgOverTempProtMod2 = _ECellChgOverTempProtMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 37),
    _ECellChgOverTempProtMod2_Type()
)
eCellChgOverTempProtMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod2.setStatus("current")


class _ECellChgOverTempProtMod3_Type(Integer32):
    """Custom type eCellChgOverTempProtMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod3_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod3_Object = MibScalar
eCellChgOverTempProtMod3 = _ECellChgOverTempProtMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 38),
    _ECellChgOverTempProtMod3_Type()
)
eCellChgOverTempProtMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod3.setStatus("current")


class _ECellChgOverTempProtMod4_Type(Integer32):
    """Custom type eCellChgOverTempProtMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod4_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod4_Object = MibScalar
eCellChgOverTempProtMod4 = _ECellChgOverTempProtMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 39),
    _ECellChgOverTempProtMod4_Type()
)
eCellChgOverTempProtMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod4.setStatus("current")


class _ECellChgOverTempProtMod5_Type(Integer32):
    """Custom type eCellChgOverTempProtMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod5_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod5_Object = MibScalar
eCellChgOverTempProtMod5 = _ECellChgOverTempProtMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 40),
    _ECellChgOverTempProtMod5_Type()
)
eCellChgOverTempProtMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod5.setStatus("current")


class _ECellChgOverTempProtMod6_Type(Integer32):
    """Custom type eCellChgOverTempProtMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod6_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod6_Object = MibScalar
eCellChgOverTempProtMod6 = _ECellChgOverTempProtMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 41),
    _ECellChgOverTempProtMod6_Type()
)
eCellChgOverTempProtMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod6.setStatus("current")


class _ECellChgOverTempProtMod7_Type(Integer32):
    """Custom type eCellChgOverTempProtMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod7_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod7_Object = MibScalar
eCellChgOverTempProtMod7 = _ECellChgOverTempProtMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 42),
    _ECellChgOverTempProtMod7_Type()
)
eCellChgOverTempProtMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod7.setStatus("current")


class _ECellDisChgOverTempProtMod1_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod1_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod1_Object = MibScalar
eCellDisChgOverTempProtMod1 = _ECellDisChgOverTempProtMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 43),
    _ECellDisChgOverTempProtMod1_Type()
)
eCellDisChgOverTempProtMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod1.setStatus("current")


class _ECellDisChgOverTempProtMod2_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod2_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod2_Object = MibScalar
eCellDisChgOverTempProtMod2 = _ECellDisChgOverTempProtMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 44),
    _ECellDisChgOverTempProtMod2_Type()
)
eCellDisChgOverTempProtMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod2.setStatus("current")


class _ECellDisChgOverTempProtMod3_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod3_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod3_Object = MibScalar
eCellDisChgOverTempProtMod3 = _ECellDisChgOverTempProtMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 45),
    _ECellDisChgOverTempProtMod3_Type()
)
eCellDisChgOverTempProtMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod3.setStatus("current")


class _ECellDisChgOverTempProtMod4_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod4_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod4_Object = MibScalar
eCellDisChgOverTempProtMod4 = _ECellDisChgOverTempProtMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 46),
    _ECellDisChgOverTempProtMod4_Type()
)
eCellDisChgOverTempProtMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod4.setStatus("current")


class _ECellDisChgOverTempProtMod5_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod5_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod5_Object = MibScalar
eCellDisChgOverTempProtMod5 = _ECellDisChgOverTempProtMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 47),
    _ECellDisChgOverTempProtMod5_Type()
)
eCellDisChgOverTempProtMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod5.setStatus("current")


class _ECellDisChgOverTempProtMod6_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod6_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod6_Object = MibScalar
eCellDisChgOverTempProtMod6 = _ECellDisChgOverTempProtMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 48),
    _ECellDisChgOverTempProtMod6_Type()
)
eCellDisChgOverTempProtMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod6.setStatus("current")


class _ECellDisChgOverTempProtMod7_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod7_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod7_Object = MibScalar
eCellDisChgOverTempProtMod7 = _ECellDisChgOverTempProtMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 49),
    _ECellDisChgOverTempProtMod7_Type()
)
eCellDisChgOverTempProtMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod7.setStatus("current")


class _EAnyCellUnderTempProtMod1_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod1_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod1_Object = MibScalar
eAnyCellUnderTempProtMod1 = _EAnyCellUnderTempProtMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 50),
    _EAnyCellUnderTempProtMod1_Type()
)
eAnyCellUnderTempProtMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod1.setStatus("current")


class _EAnyCellUnderTempProtMod2_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod2_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod2_Object = MibScalar
eAnyCellUnderTempProtMod2 = _EAnyCellUnderTempProtMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 51),
    _EAnyCellUnderTempProtMod2_Type()
)
eAnyCellUnderTempProtMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod2.setStatus("current")


class _EAnyCellUnderTempProtMod3_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod3_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod3_Object = MibScalar
eAnyCellUnderTempProtMod3 = _EAnyCellUnderTempProtMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 52),
    _EAnyCellUnderTempProtMod3_Type()
)
eAnyCellUnderTempProtMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod3.setStatus("current")


class _EAnyCellUnderTempProtMod4_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod4_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod4_Object = MibScalar
eAnyCellUnderTempProtMod4 = _EAnyCellUnderTempProtMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 53),
    _EAnyCellUnderTempProtMod4_Type()
)
eAnyCellUnderTempProtMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod4.setStatus("current")


class _EAnyCellUnderTempProtMod5_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod5_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod5_Object = MibScalar
eAnyCellUnderTempProtMod5 = _EAnyCellUnderTempProtMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 54),
    _EAnyCellUnderTempProtMod5_Type()
)
eAnyCellUnderTempProtMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod5.setStatus("current")


class _EAnyCellUnderTempProtMod6_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod6_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod6_Object = MibScalar
eAnyCellUnderTempProtMod6 = _EAnyCellUnderTempProtMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 55),
    _EAnyCellUnderTempProtMod6_Type()
)
eAnyCellUnderTempProtMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod6.setStatus("current")


class _EAnyCellUnderTempProtMod7_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod7_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod7_Object = MibScalar
eAnyCellUnderTempProtMod7 = _EAnyCellUnderTempProtMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 56),
    _EAnyCellUnderTempProtMod7_Type()
)
eAnyCellUnderTempProtMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod7.setStatus("current")


class _EBattChgOverCurrWarningMod1_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod1_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod1_Object = MibScalar
eBattChgOverCurrWarningMod1 = _EBattChgOverCurrWarningMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 57),
    _EBattChgOverCurrWarningMod1_Type()
)
eBattChgOverCurrWarningMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod1.setStatus("current")


class _EBattChgOverCurrWarningMod2_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod2_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod2_Object = MibScalar
eBattChgOverCurrWarningMod2 = _EBattChgOverCurrWarningMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 58),
    _EBattChgOverCurrWarningMod2_Type()
)
eBattChgOverCurrWarningMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod2.setStatus("current")


class _EBattChgOverCurrWarningMod3_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod3_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod3_Object = MibScalar
eBattChgOverCurrWarningMod3 = _EBattChgOverCurrWarningMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 59),
    _EBattChgOverCurrWarningMod3_Type()
)
eBattChgOverCurrWarningMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod3.setStatus("current")


class _EBattChgOverCurrWarningMod4_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod4_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod4_Object = MibScalar
eBattChgOverCurrWarningMod4 = _EBattChgOverCurrWarningMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 60),
    _EBattChgOverCurrWarningMod4_Type()
)
eBattChgOverCurrWarningMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod4.setStatus("current")


class _EBattChgOverCurrWarningMod5_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod5_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod5_Object = MibScalar
eBattChgOverCurrWarningMod5 = _EBattChgOverCurrWarningMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 61),
    _EBattChgOverCurrWarningMod5_Type()
)
eBattChgOverCurrWarningMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod5.setStatus("current")


class _EBattChgOverCurrWarningMod6_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod6_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod6_Object = MibScalar
eBattChgOverCurrWarningMod6 = _EBattChgOverCurrWarningMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 62),
    _EBattChgOverCurrWarningMod6_Type()
)
eBattChgOverCurrWarningMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod6.setStatus("current")


class _EBattChgOverCurrWarningMod7_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod7_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod7_Object = MibScalar
eBattChgOverCurrWarningMod7 = _EBattChgOverCurrWarningMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 63),
    _EBattChgOverCurrWarningMod7_Type()
)
eBattChgOverCurrWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod7.setStatus("current")


class _EBattDisChgOverCurrWarnMod1_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod1_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod1_Object = MibScalar
eBattDisChgOverCurrWarnMod1 = _EBattDisChgOverCurrWarnMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 64),
    _EBattDisChgOverCurrWarnMod1_Type()
)
eBattDisChgOverCurrWarnMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod1.setStatus("current")


class _EBattDisChgOverCurrWarnMod2_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod2_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod2_Object = MibScalar
eBattDisChgOverCurrWarnMod2 = _EBattDisChgOverCurrWarnMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 65),
    _EBattDisChgOverCurrWarnMod2_Type()
)
eBattDisChgOverCurrWarnMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod2.setStatus("current")


class _EBattDisChgOverCurrWarnMod3_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod3_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod3_Object = MibScalar
eBattDisChgOverCurrWarnMod3 = _EBattDisChgOverCurrWarnMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 66),
    _EBattDisChgOverCurrWarnMod3_Type()
)
eBattDisChgOverCurrWarnMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod3.setStatus("current")


class _EBattDisChgOverCurrWarnMod4_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod4_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod4_Object = MibScalar
eBattDisChgOverCurrWarnMod4 = _EBattDisChgOverCurrWarnMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 67),
    _EBattDisChgOverCurrWarnMod4_Type()
)
eBattDisChgOverCurrWarnMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod4.setStatus("current")


class _EBattDisChgOverCurrWarnMod5_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod5_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod5_Object = MibScalar
eBattDisChgOverCurrWarnMod5 = _EBattDisChgOverCurrWarnMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 68),
    _EBattDisChgOverCurrWarnMod5_Type()
)
eBattDisChgOverCurrWarnMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod5.setStatus("current")


class _EBattDisChgOverCurrWarnMod6_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod6_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod6_Object = MibScalar
eBattDisChgOverCurrWarnMod6 = _EBattDisChgOverCurrWarnMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 69),
    _EBattDisChgOverCurrWarnMod6_Type()
)
eBattDisChgOverCurrWarnMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod6.setStatus("current")


class _EBattDisChgOverCurrWarnMod7_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod7_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod7_Object = MibScalar
eBattDisChgOverCurrWarnMod7 = _EBattDisChgOverCurrWarnMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 70),
    _EBattDisChgOverCurrWarnMod7_Type()
)
eBattDisChgOverCurrWarnMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod7.setStatus("current")


class _EBattLowSOCWarningMod1_Type(Integer32):
    """Custom type eBattLowSOCWarningMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod1_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod1_Object = MibScalar
eBattLowSOCWarningMod1 = _EBattLowSOCWarningMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 71),
    _EBattLowSOCWarningMod1_Type()
)
eBattLowSOCWarningMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod1.setStatus("current")


class _EBattLowSOCWarningMod2_Type(Integer32):
    """Custom type eBattLowSOCWarningMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod2_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod2_Object = MibScalar
eBattLowSOCWarningMod2 = _EBattLowSOCWarningMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 72),
    _EBattLowSOCWarningMod2_Type()
)
eBattLowSOCWarningMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod2.setStatus("current")


class _EBattLowSOCWarningMod3_Type(Integer32):
    """Custom type eBattLowSOCWarningMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod3_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod3_Object = MibScalar
eBattLowSOCWarningMod3 = _EBattLowSOCWarningMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 73),
    _EBattLowSOCWarningMod3_Type()
)
eBattLowSOCWarningMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod3.setStatus("current")


class _EBattLowSOCWarningMod4_Type(Integer32):
    """Custom type eBattLowSOCWarningMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod4_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod4_Object = MibScalar
eBattLowSOCWarningMod4 = _EBattLowSOCWarningMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 74),
    _EBattLowSOCWarningMod4_Type()
)
eBattLowSOCWarningMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod4.setStatus("current")


class _EBattLowSOCWarningMod5_Type(Integer32):
    """Custom type eBattLowSOCWarningMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod5_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod5_Object = MibScalar
eBattLowSOCWarningMod5 = _EBattLowSOCWarningMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 75),
    _EBattLowSOCWarningMod5_Type()
)
eBattLowSOCWarningMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod5.setStatus("current")


class _EBattLowSOCWarningMod6_Type(Integer32):
    """Custom type eBattLowSOCWarningMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod6_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod6_Object = MibScalar
eBattLowSOCWarningMod6 = _EBattLowSOCWarningMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 76),
    _EBattLowSOCWarningMod6_Type()
)
eBattLowSOCWarningMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod6.setStatus("current")


class _EBattLowSOCWarningMod7_Type(Integer32):
    """Custom type eBattLowSOCWarningMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod7_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod7_Object = MibScalar
eBattLowSOCWarningMod7 = _EBattLowSOCWarningMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 77),
    _EBattLowSOCWarningMod7_Type()
)
eBattLowSOCWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod7.setStatus("current")


class _EBattOverCurrProtectionMod1_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod1_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod1_Object = MibScalar
eBattOverCurrProtectionMod1 = _EBattOverCurrProtectionMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 78),
    _EBattOverCurrProtectionMod1_Type()
)
eBattOverCurrProtectionMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod1.setStatus("current")


class _EBattOverCurrProtectionMod2_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod2_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod2_Object = MibScalar
eBattOverCurrProtectionMod2 = _EBattOverCurrProtectionMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 79),
    _EBattOverCurrProtectionMod2_Type()
)
eBattOverCurrProtectionMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod2.setStatus("current")


class _EBattOverCurrProtectionMod3_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod3_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod3_Object = MibScalar
eBattOverCurrProtectionMod3 = _EBattOverCurrProtectionMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 80),
    _EBattOverCurrProtectionMod3_Type()
)
eBattOverCurrProtectionMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod3.setStatus("current")


class _EBattOverCurrProtectionMod4_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod4_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod4_Object = MibScalar
eBattOverCurrProtectionMod4 = _EBattOverCurrProtectionMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 81),
    _EBattOverCurrProtectionMod4_Type()
)
eBattOverCurrProtectionMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod4.setStatus("current")


class _EBattOverCurrProtectionMod5_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod5_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod5_Object = MibScalar
eBattOverCurrProtectionMod5 = _EBattOverCurrProtectionMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 82),
    _EBattOverCurrProtectionMod5_Type()
)
eBattOverCurrProtectionMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod5.setStatus("current")


class _EBattOverCurrProtectionMod6_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod6_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod6_Object = MibScalar
eBattOverCurrProtectionMod6 = _EBattOverCurrProtectionMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 83),
    _EBattOverCurrProtectionMod6_Type()
)
eBattOverCurrProtectionMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod6.setStatus("current")


class _EBattOverCurrProtectionMod7_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod7_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod7_Object = MibScalar
eBattOverCurrProtectionMod7 = _EBattOverCurrProtectionMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 84),
    _EBattOverCurrProtectionMod7_Type()
)
eBattOverCurrProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod7.setStatus("current")


class _EBattOverVolProtectionMod1_Type(Integer32):
    """Custom type eBattOverVolProtectionMod1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod1_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod1_Object = MibScalar
eBattOverVolProtectionMod1 = _EBattOverVolProtectionMod1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 85),
    _EBattOverVolProtectionMod1_Type()
)
eBattOverVolProtectionMod1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod1.setStatus("current")


class _EBattOverVolProtectionMod2_Type(Integer32):
    """Custom type eBattOverVolProtectionMod2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod2_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod2_Object = MibScalar
eBattOverVolProtectionMod2 = _EBattOverVolProtectionMod2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 86),
    _EBattOverVolProtectionMod2_Type()
)
eBattOverVolProtectionMod2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod2.setStatus("current")


class _EBattOverVolProtectionMod3_Type(Integer32):
    """Custom type eBattOverVolProtectionMod3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod3_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod3_Object = MibScalar
eBattOverVolProtectionMod3 = _EBattOverVolProtectionMod3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 87),
    _EBattOverVolProtectionMod3_Type()
)
eBattOverVolProtectionMod3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod3.setStatus("current")


class _EBattOverVolProtectionMod4_Type(Integer32):
    """Custom type eBattOverVolProtectionMod4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod4_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod4_Object = MibScalar
eBattOverVolProtectionMod4 = _EBattOverVolProtectionMod4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 88),
    _EBattOverVolProtectionMod4_Type()
)
eBattOverVolProtectionMod4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod4.setStatus("current")


class _EBattOverVolProtectionMod5_Type(Integer32):
    """Custom type eBattOverVolProtectionMod5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod5_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod5_Object = MibScalar
eBattOverVolProtectionMod5 = _EBattOverVolProtectionMod5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 89),
    _EBattOverVolProtectionMod5_Type()
)
eBattOverVolProtectionMod5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod5.setStatus("current")


class _EBattOverVolProtectionMod6_Type(Integer32):
    """Custom type eBattOverVolProtectionMod6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod6_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod6_Object = MibScalar
eBattOverVolProtectionMod6 = _EBattOverVolProtectionMod6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 90),
    _EBattOverVolProtectionMod6_Type()
)
eBattOverVolProtectionMod6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod6.setStatus("current")


class _EBattOverVolProtectionMod7_Type(Integer32):
    """Custom type eBattOverVolProtectionMod7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod7_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod7_Object = MibScalar
eBattOverVolProtectionMod7 = _EBattOverVolProtectionMod7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 91),
    _EBattOverVolProtectionMod7_Type()
)
eBattOverVolProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod7.setStatus("current")


class _EBattBankVolAlarm_Type(Integer32):
    """Custom type eBattBankVolAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattBankVolAlarm_Type.__name__ = "Integer32"
_EBattBankVolAlarm_Object = MibScalar
eBattBankVolAlarm = _EBattBankVolAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 92),
    _EBattBankVolAlarm_Type()
)
eBattBankVolAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattBankVolAlarm.setStatus("current")


class _EBattUnderVolProtAnyModule_Type(Integer32):
    """Custom type eBattUnderVolProtAnyModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolProtAnyModule_Type.__name__ = "Integer32"
_EBattUnderVolProtAnyModule_Object = MibScalar
eBattUnderVolProtAnyModule = _EBattUnderVolProtAnyModule_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 93),
    _EBattUnderVolProtAnyModule_Type()
)
eBattUnderVolProtAnyModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolProtAnyModule.setStatus("current")


class _EModule1Isolated_Type(Integer32):
    """Custom type eModule1Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule1Isolated_Type.__name__ = "Integer32"
_EModule1Isolated_Object = MibScalar
eModule1Isolated = _EModule1Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 94),
    _EModule1Isolated_Type()
)
eModule1Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule1Isolated.setStatus("current")


class _EModule2Isolated_Type(Integer32):
    """Custom type eModule2Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule2Isolated_Type.__name__ = "Integer32"
_EModule2Isolated_Object = MibScalar
eModule2Isolated = _EModule2Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 95),
    _EModule2Isolated_Type()
)
eModule2Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule2Isolated.setStatus("current")


class _EModule3Isolated_Type(Integer32):
    """Custom type eModule3Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule3Isolated_Type.__name__ = "Integer32"
_EModule3Isolated_Object = MibScalar
eModule3Isolated = _EModule3Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 96),
    _EModule3Isolated_Type()
)
eModule3Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule3Isolated.setStatus("current")


class _EModule4Isolated_Type(Integer32):
    """Custom type eModule4Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule4Isolated_Type.__name__ = "Integer32"
_EModule4Isolated_Object = MibScalar
eModule4Isolated = _EModule4Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 97),
    _EModule4Isolated_Type()
)
eModule4Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule4Isolated.setStatus("current")


class _EModule5Isolated_Type(Integer32):
    """Custom type eModule5Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule5Isolated_Type.__name__ = "Integer32"
_EModule5Isolated_Object = MibScalar
eModule5Isolated = _EModule5Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 98),
    _EModule5Isolated_Type()
)
eModule5Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule5Isolated.setStatus("current")


class _EModule6Isolated_Type(Integer32):
    """Custom type eModule6Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule6Isolated_Type.__name__ = "Integer32"
_EModule6Isolated_Object = MibScalar
eModule6Isolated = _EModule6Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 99),
    _EModule6Isolated_Type()
)
eModule6Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule6Isolated.setStatus("current")


class _EModule7Isolated_Type(Integer32):
    """Custom type eModule7Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule7Isolated_Type.__name__ = "Integer32"
_EModule7Isolated_Object = MibScalar
eModule7Isolated = _EModule7Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 100),
    _EModule7Isolated_Type()
)
eModule7Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule7Isolated.setStatus("current")


class _EBatteryBanklevel1lowVolAL_Type(Integer32):
    """Custom type eBatteryBanklevel1lowVolAL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryBanklevel1lowVolAL_Type.__name__ = "Integer32"
_EBatteryBanklevel1lowVolAL_Object = MibScalar
eBatteryBanklevel1lowVolAL = _EBatteryBanklevel1lowVolAL_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 101),
    _EBatteryBanklevel1lowVolAL_Type()
)
eBatteryBanklevel1lowVolAL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryBanklevel1lowVolAL.setStatus("current")


class _EBatteryBanklevel2lowVolAL_Type(Integer32):
    """Custom type eBatteryBanklevel2lowVolAL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryBanklevel2lowVolAL_Type.__name__ = "Integer32"
_EBatteryBanklevel2lowVolAL_Object = MibScalar
eBatteryBanklevel2lowVolAL = _EBatteryBanklevel2lowVolAL_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 102),
    _EBatteryBanklevel2lowVolAL_Type()
)
eBatteryBanklevel2lowVolAL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryBanklevel2lowVolAL.setStatus("current")


class _EBatteryBankhighTempAlarm_Type(Integer32):
    """Custom type eBatteryBankhighTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryBankhighTempAlarm_Type.__name__ = "Integer32"
_EBatteryBankhighTempAlarm_Object = MibScalar
eBatteryBankhighTempAlarm = _EBatteryBankhighTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 103),
    _EBatteryBankhighTempAlarm_Type()
)
eBatteryBankhighTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryBankhighTempAlarm.setStatus("current")


class _EBatteryBanklowTempAlarm_Type(Integer32):
    """Custom type eBatteryBanklowTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryBanklowTempAlarm_Type.__name__ = "Integer32"
_EBatteryBanklowTempAlarm_Object = MibScalar
eBatteryBanklowTempAlarm = _EBatteryBanklowTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 104),
    _EBatteryBanklowTempAlarm_Type()
)
eBatteryBanklowTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryBanklowTempAlarm.setStatus("current")


class _EAnymoduleCurrhighAlarm_Type(Integer32):
    """Custom type eAnymoduleCurrhighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnymoduleCurrhighAlarm_Type.__name__ = "Integer32"
_EAnymoduleCurrhighAlarm_Object = MibScalar
eAnymoduleCurrhighAlarm = _EAnymoduleCurrhighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 106),
    _EAnymoduleCurrhighAlarm_Type()
)
eAnymoduleCurrhighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnymoduleCurrhighAlarm.setStatus("current")


class _ESOCBelowLvl1ThresAlAnyMod_Type(Integer32):
    """Custom type eSOCBelowLvl1ThresAlAnyMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESOCBelowLvl1ThresAlAnyMod_Type.__name__ = "Integer32"
_ESOCBelowLvl1ThresAlAnyMod_Object = MibScalar
eSOCBelowLvl1ThresAlAnyMod = _ESOCBelowLvl1ThresAlAnyMod_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 107),
    _ESOCBelowLvl1ThresAlAnyMod_Type()
)
eSOCBelowLvl1ThresAlAnyMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCBelowLvl1ThresAlAnyMod.setStatus("current")


class _ESystemfail_Type(Integer32):
    """Custom type eSystemfail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESystemfail_Type.__name__ = "Integer32"
_ESystemfail_Object = MibScalar
eSystemfail = _ESystemfail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 108),
    _ESystemfail_Type()
)
eSystemfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSystemfail.setStatus("current")


class _EMasterCBMSControllerFailAl_Type(Integer32):
    """Custom type eMasterCBMSControllerFailAl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMasterCBMSControllerFailAl_Type.__name__ = "Integer32"
_EMasterCBMSControllerFailAl_Object = MibScalar
eMasterCBMSControllerFailAl = _EMasterCBMSControllerFailAl_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 109),
    _EMasterCBMSControllerFailAl_Type()
)
eMasterCBMSControllerFailAl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMasterCBMSControllerFailAl.setStatus("current")


class _ECellIsGoingOvTemp_1stLevel_Type(Integer32):
    """Custom type eCellIsGoingOvTemp_1stLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellIsGoingOvTemp_1stLevel_Type.__name__ = "Integer32"
_ECellIsGoingOvTemp_1stLevel_Object = MibScalar
eCellIsGoingOvTemp_1stLevel = _ECellIsGoingOvTemp_1stLevel_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 110),
    _ECellIsGoingOvTemp_1stLevel_Type()
)
eCellIsGoingOvTemp_1stLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellIsGoingOvTemp_1stLevel.setStatus("current")


class _ECellIsGoingOvChg1_stLevel_Type(Integer32):
    """Custom type eCellIsGoingOvChg1_stLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellIsGoingOvChg1_stLevel_Type.__name__ = "Integer32"
_ECellIsGoingOvChg1_stLevel_Object = MibScalar
eCellIsGoingOvChg1_stLevel = _ECellIsGoingOvChg1_stLevel_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 111),
    _ECellIsGoingOvChg1_stLevel_Type()
)
eCellIsGoingOvChg1_stLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellIsGoingOvChg1_stLevel.setStatus("current")


class _ECellIsGoingOvChg2_ndLevel_Type(Integer32):
    """Custom type eCellIsGoingOvChg2_ndLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellIsGoingOvChg2_ndLevel_Type.__name__ = "Integer32"
_ECellIsGoingOvChg2_ndLevel_Object = MibScalar
eCellIsGoingOvChg2_ndLevel = _ECellIsGoingOvChg2_ndLevel_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 112),
    _ECellIsGoingOvChg2_ndLevel_Type()
)
eCellIsGoingOvChg2_ndLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellIsGoingOvChg2_ndLevel.setStatus("current")


class _ECellIsGoingunderVol_Type(Integer32):
    """Custom type eCellIsGoingunderVol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellIsGoingunderVol_Type.__name__ = "Integer32"
_ECellIsGoingunderVol_Object = MibScalar
eCellIsGoingunderVol = _ECellIsGoingunderVol_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 113),
    _ECellIsGoingunderVol_Type()
)
eCellIsGoingunderVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellIsGoingunderVol.setStatus("current")


class _ELowSOC_Type(Integer32):
    """Custom type eLowSOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELowSOC_Type.__name__ = "Integer32"
_ELowSOC_Object = MibScalar
eLowSOC = _ELowSOC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 114),
    _ELowSOC_Type()
)
eLowSOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLowSOC.setStatus("current")


class _EAmosfetisgoingoverTemp_Type(Integer32):
    """Custom type eAmosfetisgoingoverTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAmosfetisgoingoverTemp_Type.__name__ = "Integer32"
_EAmosfetisgoingoverTemp_Object = MibScalar
eAmosfetisgoingoverTemp = _EAmosfetisgoingoverTemp_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 115),
    _EAmosfetisgoingoverTemp_Type()
)
eAmosfetisgoingoverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAmosfetisgoingoverTemp.setStatus("current")


class _EHeaterFailure_Type(Integer32):
    """Custom type eHeaterFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHeaterFailure_Type.__name__ = "Integer32"
_EHeaterFailure_Object = MibScalar
eHeaterFailure = _EHeaterFailure_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 116),
    _EHeaterFailure_Type()
)
eHeaterFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHeaterFailure.setStatus("current")


class _ELowSOH_Type(Integer32):
    """Custom type eLowSOH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELowSOH_Type.__name__ = "Integer32"
_ELowSOH_Object = MibScalar
eLowSOH = _ELowSOH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 117),
    _ELowSOH_Type()
)
eLowSOH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLowSOH.setStatus("current")


class _EUnbalancecell_Type(Integer32):
    """Custom type eUnbalancecell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EUnbalancecell_Type.__name__ = "Integer32"
_EUnbalancecell_Object = MibScalar
eUnbalancecell = _EUnbalancecell_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 118),
    _EUnbalancecell_Type()
)
eUnbalancecell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUnbalancecell.setStatus("current")


class _EMosfetTempoutofRange_Type(Integer32):
    """Custom type eMosfetTempoutofRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetTempoutofRange_Type.__name__ = "Integer32"
_EMosfetTempoutofRange_Object = MibScalar
eMosfetTempoutofRange = _EMosfetTempoutofRange_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 119),
    _EMosfetTempoutofRange_Type()
)
eMosfetTempoutofRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetTempoutofRange.setStatus("current")


class _EEmergencyAlarmModule1_Type(Integer32):
    """Custom type eEmergencyAlarmModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule1_Type.__name__ = "Integer32"
_EEmergencyAlarmModule1_Object = MibScalar
eEmergencyAlarmModule1 = _EEmergencyAlarmModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 120),
    _EEmergencyAlarmModule1_Type()
)
eEmergencyAlarmModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule1.setStatus("current")


class _ECellTempoutofRangeModule1_Type(Integer32):
    """Custom type eCellTempoutofRangeModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule1_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule1_Object = MibScalar
eCellTempoutofRangeModule1 = _ECellTempoutofRangeModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 121),
    _ECellTempoutofRangeModule1_Type()
)
eCellTempoutofRangeModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule1.setStatus("current")


class _EHighBatterysupplyModule1_Type(Integer32):
    """Custom type eHighBatterysupplyModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule1_Type.__name__ = "Integer32"
_EHighBatterysupplyModule1_Object = MibScalar
eHighBatterysupplyModule1 = _EHighBatterysupplyModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 122),
    _EHighBatterysupplyModule1_Type()
)
eHighBatterysupplyModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule1.setStatus("current")


class _EMosfetisoverTempModule1_Type(Integer32):
    """Custom type eMosfetisoverTempModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule1_Type.__name__ = "Integer32"
_EMosfetisoverTempModule1_Object = MibScalar
eMosfetisoverTempModule1 = _EMosfetisoverTempModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 123),
    _EMosfetisoverTempModule1_Type()
)
eMosfetisoverTempModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule1.setStatus("current")


class _EAutotestFailureModule1_Type(Integer32):
    """Custom type eAutotestFailureModule1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule1_Type.__name__ = "Integer32"
_EAutotestFailureModule1_Object = MibScalar
eAutotestFailureModule1 = _EAutotestFailureModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 124),
    _EAutotestFailureModule1_Type()
)
eAutotestFailureModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule1.setStatus("current")


class _EEmergencyAlarmModule2_Type(Integer32):
    """Custom type eEmergencyAlarmModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule2_Type.__name__ = "Integer32"
_EEmergencyAlarmModule2_Object = MibScalar
eEmergencyAlarmModule2 = _EEmergencyAlarmModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 125),
    _EEmergencyAlarmModule2_Type()
)
eEmergencyAlarmModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule2.setStatus("current")


class _ECellTempoutofRangeModule2_Type(Integer32):
    """Custom type eCellTempoutofRangeModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule2_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule2_Object = MibScalar
eCellTempoutofRangeModule2 = _ECellTempoutofRangeModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 126),
    _ECellTempoutofRangeModule2_Type()
)
eCellTempoutofRangeModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule2.setStatus("current")


class _EHighBatterysupplyModule2_Type(Integer32):
    """Custom type eHighBatterysupplyModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule2_Type.__name__ = "Integer32"
_EHighBatterysupplyModule2_Object = MibScalar
eHighBatterysupplyModule2 = _EHighBatterysupplyModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 127),
    _EHighBatterysupplyModule2_Type()
)
eHighBatterysupplyModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule2.setStatus("current")


class _EMosfetisoverTempModule2_Type(Integer32):
    """Custom type eMosfetisoverTempModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule2_Type.__name__ = "Integer32"
_EMosfetisoverTempModule2_Object = MibScalar
eMosfetisoverTempModule2 = _EMosfetisoverTempModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 128),
    _EMosfetisoverTempModule2_Type()
)
eMosfetisoverTempModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule2.setStatus("current")


class _EAutotestFailureModule2_Type(Integer32):
    """Custom type eAutotestFailureModule2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule2_Type.__name__ = "Integer32"
_EAutotestFailureModule2_Object = MibScalar
eAutotestFailureModule2 = _EAutotestFailureModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 129),
    _EAutotestFailureModule2_Type()
)
eAutotestFailureModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule2.setStatus("current")


class _EEmergencyAlarmModule3_Type(Integer32):
    """Custom type eEmergencyAlarmModule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule3_Type.__name__ = "Integer32"
_EEmergencyAlarmModule3_Object = MibScalar
eEmergencyAlarmModule3 = _EEmergencyAlarmModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 130),
    _EEmergencyAlarmModule3_Type()
)
eEmergencyAlarmModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule3.setStatus("current")


class _ECellTempoutofRangeModule3_Type(Integer32):
    """Custom type eCellTempoutofRangeModule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule3_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule3_Object = MibScalar
eCellTempoutofRangeModule3 = _ECellTempoutofRangeModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 131),
    _ECellTempoutofRangeModule3_Type()
)
eCellTempoutofRangeModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule3.setStatus("current")


class _EHighBatterysupplyModule3_Type(Integer32):
    """Custom type eHighBatterysupplyModule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule3_Type.__name__ = "Integer32"
_EHighBatterysupplyModule3_Object = MibScalar
eHighBatterysupplyModule3 = _EHighBatterysupplyModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 132),
    _EHighBatterysupplyModule3_Type()
)
eHighBatterysupplyModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule3.setStatus("current")


class _EMosfetisoverTempModule3_Type(Integer32):
    """Custom type eMosfetisoverTempModule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule3_Type.__name__ = "Integer32"
_EMosfetisoverTempModule3_Object = MibScalar
eMosfetisoverTempModule3 = _EMosfetisoverTempModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 133),
    _EMosfetisoverTempModule3_Type()
)
eMosfetisoverTempModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule3.setStatus("current")


class _EAutotestFailureModule3_Type(Integer32):
    """Custom type eAutotestFailureModule3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule3_Type.__name__ = "Integer32"
_EAutotestFailureModule3_Object = MibScalar
eAutotestFailureModule3 = _EAutotestFailureModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 134),
    _EAutotestFailureModule3_Type()
)
eAutotestFailureModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule3.setStatus("current")


class _EEmergencyAlarmModule4_Type(Integer32):
    """Custom type eEmergencyAlarmModule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule4_Type.__name__ = "Integer32"
_EEmergencyAlarmModule4_Object = MibScalar
eEmergencyAlarmModule4 = _EEmergencyAlarmModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 135),
    _EEmergencyAlarmModule4_Type()
)
eEmergencyAlarmModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule4.setStatus("current")


class _ECellTempoutofRangeModule4_Type(Integer32):
    """Custom type eCellTempoutofRangeModule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule4_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule4_Object = MibScalar
eCellTempoutofRangeModule4 = _ECellTempoutofRangeModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 136),
    _ECellTempoutofRangeModule4_Type()
)
eCellTempoutofRangeModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule4.setStatus("current")


class _EHighBatterysupplyModule4_Type(Integer32):
    """Custom type eHighBatterysupplyModule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule4_Type.__name__ = "Integer32"
_EHighBatterysupplyModule4_Object = MibScalar
eHighBatterysupplyModule4 = _EHighBatterysupplyModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 137),
    _EHighBatterysupplyModule4_Type()
)
eHighBatterysupplyModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule4.setStatus("current")


class _EMosfetisoverTempModule4_Type(Integer32):
    """Custom type eMosfetisoverTempModule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule4_Type.__name__ = "Integer32"
_EMosfetisoverTempModule4_Object = MibScalar
eMosfetisoverTempModule4 = _EMosfetisoverTempModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 138),
    _EMosfetisoverTempModule4_Type()
)
eMosfetisoverTempModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule4.setStatus("current")


class _EAutotestFailureModule4_Type(Integer32):
    """Custom type eAutotestFailureModule4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule4_Type.__name__ = "Integer32"
_EAutotestFailureModule4_Object = MibScalar
eAutotestFailureModule4 = _EAutotestFailureModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 139),
    _EAutotestFailureModule4_Type()
)
eAutotestFailureModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule4.setStatus("current")


class _EEmergencyAlarmModule5_Type(Integer32):
    """Custom type eEmergencyAlarmModule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule5_Type.__name__ = "Integer32"
_EEmergencyAlarmModule5_Object = MibScalar
eEmergencyAlarmModule5 = _EEmergencyAlarmModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 140),
    _EEmergencyAlarmModule5_Type()
)
eEmergencyAlarmModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule5.setStatus("current")


class _ECellTempoutofRangeModule5_Type(Integer32):
    """Custom type eCellTempoutofRangeModule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule5_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule5_Object = MibScalar
eCellTempoutofRangeModule5 = _ECellTempoutofRangeModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 141),
    _ECellTempoutofRangeModule5_Type()
)
eCellTempoutofRangeModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule5.setStatus("current")


class _EHighBatterysupplyModule5_Type(Integer32):
    """Custom type eHighBatterysupplyModule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule5_Type.__name__ = "Integer32"
_EHighBatterysupplyModule5_Object = MibScalar
eHighBatterysupplyModule5 = _EHighBatterysupplyModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 142),
    _EHighBatterysupplyModule5_Type()
)
eHighBatterysupplyModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule5.setStatus("current")


class _EMosfetisoverTempModule5_Type(Integer32):
    """Custom type eMosfetisoverTempModule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule5_Type.__name__ = "Integer32"
_EMosfetisoverTempModule5_Object = MibScalar
eMosfetisoverTempModule5 = _EMosfetisoverTempModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 143),
    _EMosfetisoverTempModule5_Type()
)
eMosfetisoverTempModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule5.setStatus("current")


class _EAutotestFailureModule5_Type(Integer32):
    """Custom type eAutotestFailureModule5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule5_Type.__name__ = "Integer32"
_EAutotestFailureModule5_Object = MibScalar
eAutotestFailureModule5 = _EAutotestFailureModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 144),
    _EAutotestFailureModule5_Type()
)
eAutotestFailureModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule5.setStatus("current")


class _EEmergencyAlarmModule6_Type(Integer32):
    """Custom type eEmergencyAlarmModule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule6_Type.__name__ = "Integer32"
_EEmergencyAlarmModule6_Object = MibScalar
eEmergencyAlarmModule6 = _EEmergencyAlarmModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 145),
    _EEmergencyAlarmModule6_Type()
)
eEmergencyAlarmModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule6.setStatus("current")


class _ECellTempoutofRangeModule6_Type(Integer32):
    """Custom type eCellTempoutofRangeModule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule6_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule6_Object = MibScalar
eCellTempoutofRangeModule6 = _ECellTempoutofRangeModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 146),
    _ECellTempoutofRangeModule6_Type()
)
eCellTempoutofRangeModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule6.setStatus("current")


class _EHighBatterysupplyModule6_Type(Integer32):
    """Custom type eHighBatterysupplyModule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule6_Type.__name__ = "Integer32"
_EHighBatterysupplyModule6_Object = MibScalar
eHighBatterysupplyModule6 = _EHighBatterysupplyModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 147),
    _EHighBatterysupplyModule6_Type()
)
eHighBatterysupplyModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule6.setStatus("current")


class _EMosfetisoverTempModule6_Type(Integer32):
    """Custom type eMosfetisoverTempModule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule6_Type.__name__ = "Integer32"
_EMosfetisoverTempModule6_Object = MibScalar
eMosfetisoverTempModule6 = _EMosfetisoverTempModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 148),
    _EMosfetisoverTempModule6_Type()
)
eMosfetisoverTempModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule6.setStatus("current")


class _EAutotestFailureModule6_Type(Integer32):
    """Custom type eAutotestFailureModule6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule6_Type.__name__ = "Integer32"
_EAutotestFailureModule6_Object = MibScalar
eAutotestFailureModule6 = _EAutotestFailureModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 149),
    _EAutotestFailureModule6_Type()
)
eAutotestFailureModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule6.setStatus("current")


class _EEmergencyAlarmModule7_Type(Integer32):
    """Custom type eEmergencyAlarmModule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEmergencyAlarmModule7_Type.__name__ = "Integer32"
_EEmergencyAlarmModule7_Object = MibScalar
eEmergencyAlarmModule7 = _EEmergencyAlarmModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 150),
    _EEmergencyAlarmModule7_Type()
)
eEmergencyAlarmModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEmergencyAlarmModule7.setStatus("current")


class _ECellTempoutofRangeModule7_Type(Integer32):
    """Custom type eCellTempoutofRangeModule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellTempoutofRangeModule7_Type.__name__ = "Integer32"
_ECellTempoutofRangeModule7_Object = MibScalar
eCellTempoutofRangeModule7 = _ECellTempoutofRangeModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 151),
    _ECellTempoutofRangeModule7_Type()
)
eCellTempoutofRangeModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellTempoutofRangeModule7.setStatus("current")


class _EHighBatterysupplyModule7_Type(Integer32):
    """Custom type eHighBatterysupplyModule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighBatterysupplyModule7_Type.__name__ = "Integer32"
_EHighBatterysupplyModule7_Object = MibScalar
eHighBatterysupplyModule7 = _EHighBatterysupplyModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 152),
    _EHighBatterysupplyModule7_Type()
)
eHighBatterysupplyModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighBatterysupplyModule7.setStatus("current")


class _EMosfetisoverTempModule7_Type(Integer32):
    """Custom type eMosfetisoverTempModule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMosfetisoverTempModule7_Type.__name__ = "Integer32"
_EMosfetisoverTempModule7_Object = MibScalar
eMosfetisoverTempModule7 = _EMosfetisoverTempModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 153),
    _EMosfetisoverTempModule7_Type()
)
eMosfetisoverTempModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMosfetisoverTempModule7.setStatus("current")


class _EAutotestFailureModule7_Type(Integer32):
    """Custom type eAutotestFailureModule7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAutotestFailureModule7_Type.__name__ = "Integer32"
_EAutotestFailureModule7_Object = MibScalar
eAutotestFailureModule7 = _EAutotestFailureModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 154),
    _EAutotestFailureModule7_Type()
)
eAutotestFailureModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAutotestFailureModule7.setStatus("current")


class _EACPowerfail_Type(Integer32):
    """Custom type eACPowerfail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EACPowerfail_Type.__name__ = "Integer32"
_EACPowerfail_Object = MibScalar
eACPowerfail = _EACPowerfail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 155),
    _EACPowerfail_Type()
)
eACPowerfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eACPowerfail.setStatus("current")


class _EACDBIncomerTrip_Type(Integer32):
    """Custom type eACDBIncomerTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EACDBIncomerTrip_Type.__name__ = "Integer32"
_EACDBIncomerTrip_Object = MibScalar
eACDBIncomerTrip = _EACDBIncomerTrip_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 156),
    _EACDBIncomerTrip_Type()
)
eACDBIncomerTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eACDBIncomerTrip.setStatus("current")


class _ERectifierModule1Fail_Type(Integer32):
    """Custom type eRectifierModule1Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ERectifierModule1Fail_Type.__name__ = "Integer32"
_ERectifierModule1Fail_Object = MibScalar
eRectifierModule1Fail = _ERectifierModule1Fail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 157),
    _ERectifierModule1Fail_Type()
)
eRectifierModule1Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRectifierModule1Fail.setStatus("current")


class _ERectifierModule2Fail_Type(Integer32):
    """Custom type eRectifierModule2Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ERectifierModule2Fail_Type.__name__ = "Integer32"
_ERectifierModule2Fail_Object = MibScalar
eRectifierModule2Fail = _ERectifierModule2Fail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 158),
    _ERectifierModule2Fail_Type()
)
eRectifierModule2Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRectifierModule2Fail.setStatus("current")


class _ERectifierModule3Fail_Type(Integer32):
    """Custom type eRectifierModule3Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ERectifierModule3Fail_Type.__name__ = "Integer32"
_ERectifierModule3Fail_Object = MibScalar
eRectifierModule3Fail = _ERectifierModule3Fail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 159),
    _ERectifierModule3Fail_Type()
)
eRectifierModule3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRectifierModule3Fail.setStatus("current")


class _ERectifierModule4Fail_Type(Integer32):
    """Custom type eRectifierModule4Fail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ERectifierModule4Fail_Type.__name__ = "Integer32"
_ERectifierModule4Fail_Object = MibScalar
eRectifierModule4Fail = _ERectifierModule4Fail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 160),
    _ERectifierModule4Fail_Type()
)
eRectifierModule4Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRectifierModule4Fail.setStatus("current")


class _ELoadFusetrip_Type(Integer32):
    """Custom type eLoadFusetrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELoadFusetrip_Type.__name__ = "Integer32"
_ELoadFusetrip_Object = MibScalar
eLoadFusetrip = _ELoadFusetrip_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 161),
    _ELoadFusetrip_Type()
)
eLoadFusetrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadFusetrip.setStatus("current")


class _ELLVDAlarm_Type(Integer32):
    """Custom type eLLVDAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELLVDAlarm_Type.__name__ = "Integer32"
_ELLVDAlarm_Object = MibScalar
eLLVDAlarm = _ELLVDAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 162),
    _ELLVDAlarm_Type()
)
eLLVDAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLLVDAlarm.setStatus("current")


class _EBLVDAlarm_Type(Integer32):
    """Custom type eBLVDAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBLVDAlarm_Type.__name__ = "Integer32"
_EBLVDAlarm_Object = MibScalar
eBLVDAlarm = _EBLVDAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 163),
    _EBLVDAlarm_Type()
)
eBLVDAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBLVDAlarm.setStatus("current")


class _EBatteryfuseFail_Type(Integer32):
    """Custom type eBatteryfuseFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryfuseFail_Type.__name__ = "Integer32"
_EBatteryfuseFail_Object = MibScalar
eBatteryfuseFail = _EBatteryfuseFail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 164),
    _EBatteryfuseFail_Type()
)
eBatteryfuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryfuseFail.setStatus("current")


class _EBatteryonLoad_Type(Integer32):
    """Custom type eBatteryonLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryonLoad_Type.__name__ = "Integer32"
_EBatteryonLoad_Object = MibScalar
eBatteryonLoad = _EBatteryonLoad_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 165),
    _EBatteryonLoad_Type()
)
eBatteryonLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryonLoad.setStatus("current")


class _ETopDoorOpen_Type(Integer32):
    """Custom type eTopDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ETopDoorOpen_Type.__name__ = "Integer32"
_ETopDoorOpen_Object = MibScalar
eTopDoorOpen = _ETopDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 166),
    _ETopDoorOpen_Type()
)
eTopDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTopDoorOpen.setStatus("current")


class _EBottomDoorOpen_Type(Integer32):
    """Custom type eBottomDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBottomDoorOpen_Type.__name__ = "Integer32"
_EBottomDoorOpen_Object = MibScalar
eBottomDoorOpen = _EBottomDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 167),
    _EBottomDoorOpen_Type()
)
eBottomDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBottomDoorOpen.setStatus("current")


class _EFireAlarm_Type(Integer32):
    """Custom type eFireAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EFireAlarm_Type.__name__ = "Integer32"
_EFireAlarm_Object = MibScalar
eFireAlarm = _EFireAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 168),
    _EFireAlarm_Type()
)
eFireAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFireAlarm.setStatus("current")


class _EShelterDoorOpen_Type(Integer32):
    """Custom type eShelterDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EShelterDoorOpen_Type.__name__ = "Integer32"
_EShelterDoorOpen_Object = MibScalar
eShelterDoorOpen = _EShelterDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 169),
    _EShelterDoorOpen_Type()
)
eShelterDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eShelterDoorOpen.setStatus("current")


class _EEquipmentDoorOpen_Type(Integer32):
    """Custom type eEquipmentDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEquipmentDoorOpen_Type.__name__ = "Integer32"
_EEquipmentDoorOpen_Object = MibScalar
eEquipmentDoorOpen = _EEquipmentDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 170),
    _EEquipmentDoorOpen_Type()
)
eEquipmentDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEquipmentDoorOpen.setStatus("current")


class _EDGFailToStart_Type(Integer32):
    """Custom type eDGFailToStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGFailToStart_Type.__name__ = "Integer32"
_EDGFailToStart_Object = MibScalar
eDGFailToStart = _EDGFailToStart_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 171),
    _EDGFailToStart_Type()
)
eDGFailToStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGFailToStart.setStatus("current")


class _EDGCanopyTempHigh_Type(Integer32):
    """Custom type eDGCanopyTempHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGCanopyTempHigh_Type.__name__ = "Integer32"
_EDGCanopyTempHigh_Object = MibScalar
eDGCanopyTempHigh = _EDGCanopyTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 172),
    _EDGCanopyTempHigh_Type()
)
eDGCanopyTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGCanopyTempHigh.setStatus("current")


class _EDGLowFuelLevelWarning_Type(Integer32):
    """Custom type eDGLowFuelLevelWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGLowFuelLevelWarning_Type.__name__ = "Integer32"
_EDGLowFuelLevelWarning_Object = MibScalar
eDGLowFuelLevelWarning = _EDGLowFuelLevelWarning_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 173),
    _EDGLowFuelLevelWarning_Type()
)
eDGLowFuelLevelWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGLowFuelLevelWarning.setStatus("current")


class _EDGLowFuelLevelTrip_Type(Integer32):
    """Custom type eDGLowFuelLevelTrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGLowFuelLevelTrip_Type.__name__ = "Integer32"
_EDGLowFuelLevelTrip_Object = MibScalar
eDGLowFuelLevelTrip = _EDGLowFuelLevelTrip_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 174),
    _EDGLowFuelLevelTrip_Type()
)
eDGLowFuelLevelTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGLowFuelLevelTrip.setStatus("current")


class _EDGUnderFrequency_Type(Integer32):
    """Custom type eDGUnderFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGUnderFrequency_Type.__name__ = "Integer32"
_EDGUnderFrequency_Object = MibScalar
eDGUnderFrequency = _EDGUnderFrequency_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 175),
    _EDGUnderFrequency_Type()
)
eDGUnderFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGUnderFrequency.setStatus("current")


class _EDGCommonFault_Type(Integer32):
    """Custom type eDGCommonFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGCommonFault_Type.__name__ = "Integer32"
_EDGCommonFault_Object = MibScalar
eDGCommonFault = _EDGCommonFault_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 176),
    _EDGCommonFault_Type()
)
eDGCommonFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGCommonFault.setStatus("current")


class _EDGOverload_Type(Integer32):
    """Custom type eDGOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGOverload_Type.__name__ = "Integer32"
_EDGOverload_Object = MibScalar
eDGOverload = _EDGOverload_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 177),
    _EDGOverload_Type()
)
eDGOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGOverload.setStatus("current")


class _ELoadOnDG_Type(Integer32):
    """Custom type eLoadOnDG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELoadOnDG_Type.__name__ = "Integer32"
_ELoadOnDG_Object = MibScalar
eLoadOnDG = _ELoadOnDG_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 178),
    _ELoadOnDG_Type()
)
eLoadOnDG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadOnDG.setStatus("current")


class _EDGEngineOverSpeed_Type(Integer32):
    """Custom type eDGEngineOverSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGEngineOverSpeed_Type.__name__ = "Integer32"
_EDGEngineOverSpeed_Object = MibScalar
eDGEngineOverSpeed = _EDGEngineOverSpeed_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 179),
    _EDGEngineOverSpeed_Type()
)
eDGEngineOverSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGEngineOverSpeed.setStatus("current")


class _EDGIdleRunning_Type(Integer32):
    """Custom type eDGIdleRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGIdleRunning_Type.__name__ = "Integer32"
_EDGIdleRunning_Object = MibScalar
eDGIdleRunning = _EDGIdleRunning_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 180),
    _EDGIdleRunning_Type()
)
eDGIdleRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGIdleRunning.setStatus("current")


class _EDGInManual_Type(Integer32):
    """Custom type eDGInManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGInManual_Type.__name__ = "Integer32"
_EDGInManual_Object = MibScalar
eDGInManual = _EDGInManual_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 181),
    _EDGInManual_Type()
)
eDGInManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGInManual.setStatus("current")


class _EDGBatteryChargerFaulty_Type(Integer32):
    """Custom type eDGBatteryChargerFaulty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGBatteryChargerFaulty_Type.__name__ = "Integer32"
_EDGBatteryChargerFaulty_Object = MibScalar
eDGBatteryChargerFaulty = _EDGBatteryChargerFaulty_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 182),
    _EDGBatteryChargerFaulty_Type()
)
eDGBatteryChargerFaulty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGBatteryChargerFaulty.setStatus("current")


class _EDGCanopyDoorOpen_Type(Integer32):
    """Custom type eDGCanopyDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGCanopyDoorOpen_Type.__name__ = "Integer32"
_EDGCanopyDoorOpen_Object = MibScalar
eDGCanopyDoorOpen = _EDGCanopyDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 183),
    _EDGCanopyDoorOpen_Type()
)
eDGCanopyDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGCanopyDoorOpen.setStatus("current")


class _EDGLLOP_Type(Integer32):
    """Custom type eDGLLOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGLLOP_Type.__name__ = "Integer32"
_EDGLLOP_Object = MibScalar
eDGLLOP = _EDGLLOP_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 184),
    _EDGLLOP_Type()
)
eDGLLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGLLOP.setStatus("current")


class _EDGReserve_Type(Integer32):
    """Custom type eDGReserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGReserve_Type.__name__ = "Integer32"
_EDGReserve_Object = MibScalar
eDGReserve = _EDGReserve_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 185),
    _EDGReserve_Type()
)
eDGReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGReserve.setStatus("current")


class _EShelterTempHigh_Type(Integer32):
    """Custom type eShelterTempHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EShelterTempHigh_Type.__name__ = "Integer32"
_EShelterTempHigh_Object = MibScalar
eShelterTempHigh = _EShelterTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 186),
    _EShelterTempHigh_Type()
)
eShelterTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eShelterTempHigh.setStatus("current")


class _EPACFault_Type(Integer32):
    """Custom type ePACFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPACFault_Type.__name__ = "Integer32"
_EPACFault_Object = MibScalar
ePACFault = _EPACFault_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 187),
    _EPACFault_Type()
)
ePACFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePACFault.setStatus("current")


class _EPACRunStatus_Type(Integer32):
    """Custom type ePACRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPACRunStatus_Type.__name__ = "Integer32"
_EPACRunStatus_Object = MibScalar
ePACRunStatus = _EPACRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 188),
    _EPACRunStatus_Type()
)
ePACRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePACRunStatus.setStatus("current")


class _EPACTripStatus_Type(Integer32):
    """Custom type ePACTripStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPACTripStatus_Type.__name__ = "Integer32"
_EPACTripStatus_Object = MibScalar
ePACTripStatus = _EPACTripStatus_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 189),
    _EPACTripStatus_Type()
)
ePACTripStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePACTripStatus.setStatus("current")


class _EDiffPressureFilterStatus_Type(Integer32):
    """Custom type eDiffPressureFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDiffPressureFilterStatus_Type.__name__ = "Integer32"
_EDiffPressureFilterStatus_Object = MibScalar
eDiffPressureFilterStatus = _EDiffPressureFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 190),
    _EDiffPressureFilterStatus_Type()
)
eDiffPressureFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDiffPressureFilterStatus.setStatus("current")


class _ECommFail_BMSToPC_Type(Integer32):
    """Custom type eCommFail_BMSToPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECommFail_BMSToPC_Type.__name__ = "Integer32"
_ECommFail_BMSToPC_Object = MibScalar
eCommFail_BMSToPC = _ECommFail_BMSToPC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 191),
    _ECommFail_BMSToPC_Type()
)
eCommFail_BMSToPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFail_BMSToPC.setStatus("current")


class _EAuxillaryEvent1_Type(Integer32):
    """Custom type eAuxillaryEvent1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAuxillaryEvent1_Type.__name__ = "Integer32"
_EAuxillaryEvent1_Object = MibScalar
eAuxillaryEvent1 = _EAuxillaryEvent1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 194),
    _EAuxillaryEvent1_Type()
)
eAuxillaryEvent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAuxillaryEvent1.setStatus("current")


class _EAuxillaryEvent2_Type(Integer32):
    """Custom type eAuxillaryEvent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAuxillaryEvent2_Type.__name__ = "Integer32"
_EAuxillaryEvent2_Object = MibScalar
eAuxillaryEvent2 = _EAuxillaryEvent2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 195),
    _EAuxillaryEvent2_Type()
)
eAuxillaryEvent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAuxillaryEvent2.setStatus("current")


class _EAuxillaryEvent3_Type(Integer32):
    """Custom type eAuxillaryEvent3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAuxillaryEvent3_Type.__name__ = "Integer32"
_EAuxillaryEvent3_Object = MibScalar
eAuxillaryEvent3 = _EAuxillaryEvent3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 196),
    _EAuxillaryEvent3_Type()
)
eAuxillaryEvent3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAuxillaryEvent3.setStatus("current")


class _EAuxillaryEvent4_Type(Integer32):
    """Custom type eAuxillaryEvent4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAuxillaryEvent4_Type.__name__ = "Integer32"
_EAuxillaryEvent4_Object = MibScalar
eAuxillaryEvent4 = _EAuxillaryEvent4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 197),
    _EAuxillaryEvent4_Type()
)
eAuxillaryEvent4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAuxillaryEvent4.setStatus("current")


class _EAuxillaryEvent5_Type(Integer32):
    """Custom type eAuxillaryEvent5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAuxillaryEvent5_Type.__name__ = "Integer32"
_EAuxillaryEvent5_Object = MibScalar
eAuxillaryEvent5 = _EAuxillaryEvent5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 198),
    _EAuxillaryEvent5_Type()
)
eAuxillaryEvent5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAuxillaryEvent5.setStatus("current")


class _EInverterFail1_Type(Integer32):
    """Custom type eInverterFail1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInverterFail1_Type.__name__ = "Integer32"
_EInverterFail1_Object = MibScalar
eInverterFail1 = _EInverterFail1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 199),
    _EInverterFail1_Type()
)
eInverterFail1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInverterFail1.setStatus("current")


class _EInverterFail2_Type(Integer32):
    """Custom type eInverterFail2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInverterFail2_Type.__name__ = "Integer32"
_EInverterFail2_Object = MibScalar
eInverterFail2 = _EInverterFail2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 200),
    _EInverterFail2_Type()
)
eInverterFail2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInverterFail2.setStatus("current")


class _ESPARE3_Type(Integer32):
    """Custom type eSPARE3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESPARE3_Type.__name__ = "Integer32"
_ESPARE3_Object = MibScalar
eSPARE3 = _ESPARE3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 201),
    _ESPARE3_Type()
)
eSPARE3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSPARE3.setStatus("current")


class _ESPARE4_Type(Integer32):
    """Custom type eSPARE4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESPARE4_Type.__name__ = "Integer32"
_ESPARE4_Object = MibScalar
eSPARE4 = _ESPARE4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 202),
    _ESPARE4_Type()
)
eSPARE4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSPARE4.setStatus("current")


class _ESPARE5_Type(Integer32):
    """Custom type eSPARE5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESPARE5_Type.__name__ = "Integer32"
_ESPARE5_Object = MibScalar
eSPARE5 = _ESPARE5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 203),
    _ESPARE5_Type()
)
eSPARE5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSPARE5.setStatus("current")


class _EModule1CommFailAlarm_Type(Integer32):
    """Custom type eModule1CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule1CommFailAlarm_Type.__name__ = "Integer32"
_EModule1CommFailAlarm_Object = MibScalar
eModule1CommFailAlarm = _EModule1CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 204),
    _EModule1CommFailAlarm_Type()
)
eModule1CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule1CommFailAlarm.setStatus("current")


class _EModule2CommFailAlarm_Type(Integer32):
    """Custom type eModule2CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule2CommFailAlarm_Type.__name__ = "Integer32"
_EModule2CommFailAlarm_Object = MibScalar
eModule2CommFailAlarm = _EModule2CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 205),
    _EModule2CommFailAlarm_Type()
)
eModule2CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule2CommFailAlarm.setStatus("current")


class _EModule3CommFailAlarm_Type(Integer32):
    """Custom type eModule3CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule3CommFailAlarm_Type.__name__ = "Integer32"
_EModule3CommFailAlarm_Object = MibScalar
eModule3CommFailAlarm = _EModule3CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 206),
    _EModule3CommFailAlarm_Type()
)
eModule3CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule3CommFailAlarm.setStatus("current")


class _EModule4CommFailAlarm_Type(Integer32):
    """Custom type eModule4CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule4CommFailAlarm_Type.__name__ = "Integer32"
_EModule4CommFailAlarm_Object = MibScalar
eModule4CommFailAlarm = _EModule4CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 207),
    _EModule4CommFailAlarm_Type()
)
eModule4CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule4CommFailAlarm.setStatus("current")


class _EModule5CommFailAlarm_Type(Integer32):
    """Custom type eModule5CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule5CommFailAlarm_Type.__name__ = "Integer32"
_EModule5CommFailAlarm_Object = MibScalar
eModule5CommFailAlarm = _EModule5CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 208),
    _EModule5CommFailAlarm_Type()
)
eModule5CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule5CommFailAlarm.setStatus("current")


class _EModule6CommFailAlarm_Type(Integer32):
    """Custom type eModule6CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule6CommFailAlarm_Type.__name__ = "Integer32"
_EModule6CommFailAlarm_Object = MibScalar
eModule6CommFailAlarm = _EModule6CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 209),
    _EModule6CommFailAlarm_Type()
)
eModule6CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule6CommFailAlarm.setStatus("current")


class _EModule7CommFailAlarm_Type(Integer32):
    """Custom type eModule7CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule7CommFailAlarm_Type.__name__ = "Integer32"
_EModule7CommFailAlarm_Object = MibScalar
eModule7CommFailAlarm = _EModule7CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 210),
    _EModule7CommFailAlarm_Type()
)
eModule7CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule7CommFailAlarm.setStatus("current")


class _EInverterOutputShort_Type(Integer32):
    """Custom type eInverterOutputShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInverterOutputShort_Type.__name__ = "Integer32"
_EInverterOutputShort_Object = MibScalar
eInverterOutputShort = _EInverterOutputShort_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 211),
    _EInverterOutputShort_Type()
)
eInverterOutputShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInverterOutputShort.setStatus("current")


class _EInverterOutputOverload_Type(Integer32):
    """Custom type eInverterOutputOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInverterOutputOverload_Type.__name__ = "Integer32"
_EInverterOutputOverload_Object = MibScalar
eInverterOutputOverload = _EInverterOutputOverload_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 212),
    _EInverterOutputOverload_Type()
)
eInverterOutputOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInverterOutputOverload.setStatus("current")


class _EInverterCommonFault_Type(Integer32):
    """Custom type eInverterCommonFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInverterCommonFault_Type.__name__ = "Integer32"
_EInverterCommonFault_Object = MibScalar
eInverterCommonFault = _EInverterCommonFault_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 213),
    _EInverterCommonFault_Type()
)
eInverterCommonFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInverterCommonFault.setStatus("current")


class _EAcInputVoltageLow_Type(Integer32):
    """Custom type eAcInputVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAcInputVoltageLow_Type.__name__ = "Integer32"
_EAcInputVoltageLow_Object = MibScalar
eAcInputVoltageLow = _EAcInputVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 214),
    _EAcInputVoltageLow_Type()
)
eAcInputVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAcInputVoltageLow.setStatus("current")


class _EAcInputVoltageHigh_Type(Integer32):
    """Custom type eAcInputVoltageHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAcInputVoltageHigh_Type.__name__ = "Integer32"
_EAcInputVoltageHigh_Object = MibScalar
eAcInputVoltageHigh = _EAcInputVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 215),
    _EAcInputVoltageHigh_Type()
)
eAcInputVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAcInputVoltageHigh.setStatus("current")


class _EAcInputFreqLow_Type(Integer32):
    """Custom type eAcInputFreqLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAcInputFreqLow_Type.__name__ = "Integer32"
_EAcInputFreqLow_Object = MibScalar
eAcInputFreqLow = _EAcInputFreqLow_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 216),
    _EAcInputFreqLow_Type()
)
eAcInputFreqLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAcInputFreqLow.setStatus("current")


class _EAcInputFreqHigh_Type(Integer32):
    """Custom type eAcInputFreqHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAcInputFreqHigh_Type.__name__ = "Integer32"
_EAcInputFreqHigh_Object = MibScalar
eAcInputFreqHigh = _EAcInputFreqHigh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 217),
    _EAcInputFreqHigh_Type()
)
eAcInputFreqHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAcInputFreqHigh.setStatus("current")


class _EBypassMode_Type(Integer32):
    """Custom type eBypassMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBypassMode_Type.__name__ = "Integer32"
_EBypassMode_Object = MibScalar
eBypassMode = _EBypassMode_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 218),
    _EBypassMode_Type()
)
eBypassMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBypassMode.setStatus("current")


class _EFaultShutDown_Type(Integer32):
    """Custom type eFaultShutDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EFaultShutDown_Type.__name__ = "Integer32"
_EFaultShutDown_Object = MibScalar
eFaultShutDown = _EFaultShutDown_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 219),
    _EFaultShutDown_Type()
)
eFaultShutDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFaultShutDown.setStatus("current")


class _EModuleCellUnbalancedMod8_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod8_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod8_Object = MibScalar
eModuleCellUnbalancedMod8 = _EModuleCellUnbalancedMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 220),
    _EModuleCellUnbalancedMod8_Type()
)
eModuleCellUnbalancedMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod8.setStatus("current")


class _EModuleCellUnbalancedMod9_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod9_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod9_Object = MibScalar
eModuleCellUnbalancedMod9 = _EModuleCellUnbalancedMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 221),
    _EModuleCellUnbalancedMod9_Type()
)
eModuleCellUnbalancedMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod9.setStatus("current")


class _EModuleCellUnbalancedMod10_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod10_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod10_Object = MibScalar
eModuleCellUnbalancedMod10 = _EModuleCellUnbalancedMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 222),
    _EModuleCellUnbalancedMod10_Type()
)
eModuleCellUnbalancedMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod10.setStatus("current")


class _EModuleCellUnbalancedMod11_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod11_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod11_Object = MibScalar
eModuleCellUnbalancedMod11 = _EModuleCellUnbalancedMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 223),
    _EModuleCellUnbalancedMod11_Type()
)
eModuleCellUnbalancedMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod11.setStatus("current")


class _EModuleCellUnbalancedMod12_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod12_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod12_Object = MibScalar
eModuleCellUnbalancedMod12 = _EModuleCellUnbalancedMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 224),
    _EModuleCellUnbalancedMod12_Type()
)
eModuleCellUnbalancedMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod12.setStatus("current")


class _EModuleCellUnbalancedMod13_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod13_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod13_Object = MibScalar
eModuleCellUnbalancedMod13 = _EModuleCellUnbalancedMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 225),
    _EModuleCellUnbalancedMod13_Type()
)
eModuleCellUnbalancedMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod13.setStatus("current")


class _EModuleCellUnbalancedMod14_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod14_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod14_Object = MibScalar
eModuleCellUnbalancedMod14 = _EModuleCellUnbalancedMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 226),
    _EModuleCellUnbalancedMod14_Type()
)
eModuleCellUnbalancedMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod14.setStatus("current")


class _EModuleCellUnbalancedMod15_Type(Integer32):
    """Custom type eModuleCellUnbalancedMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModuleCellUnbalancedMod15_Type.__name__ = "Integer32"
_EModuleCellUnbalancedMod15_Object = MibScalar
eModuleCellUnbalancedMod15 = _EModuleCellUnbalancedMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 227),
    _EModuleCellUnbalancedMod15_Type()
)
eModuleCellUnbalancedMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleCellUnbalancedMod15.setStatus("current")


class _EBattUnderVolWarningMod8_Type(Integer32):
    """Custom type eBattUnderVolWarningMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod8_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod8_Object = MibScalar
eBattUnderVolWarningMod8 = _EBattUnderVolWarningMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 228),
    _EBattUnderVolWarningMod8_Type()
)
eBattUnderVolWarningMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod8.setStatus("current")


class _EBattUnderVolWarningMod9_Type(Integer32):
    """Custom type eBattUnderVolWarningMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod9_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod9_Object = MibScalar
eBattUnderVolWarningMod9 = _EBattUnderVolWarningMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 229),
    _EBattUnderVolWarningMod9_Type()
)
eBattUnderVolWarningMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod9.setStatus("current")


class _EBattUnderVolWarningMod10_Type(Integer32):
    """Custom type eBattUnderVolWarningMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod10_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod10_Object = MibScalar
eBattUnderVolWarningMod10 = _EBattUnderVolWarningMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 230),
    _EBattUnderVolWarningMod10_Type()
)
eBattUnderVolWarningMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod10.setStatus("current")


class _EBattUnderVolWarningMod11_Type(Integer32):
    """Custom type eBattUnderVolWarningMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod11_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod11_Object = MibScalar
eBattUnderVolWarningMod11 = _EBattUnderVolWarningMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 231),
    _EBattUnderVolWarningMod11_Type()
)
eBattUnderVolWarningMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod11.setStatus("current")


class _EBattUnderVolWarningMod12_Type(Integer32):
    """Custom type eBattUnderVolWarningMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod12_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod12_Object = MibScalar
eBattUnderVolWarningMod12 = _EBattUnderVolWarningMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 232),
    _EBattUnderVolWarningMod12_Type()
)
eBattUnderVolWarningMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod12.setStatus("current")


class _EBattUnderVolWarningMod13_Type(Integer32):
    """Custom type eBattUnderVolWarningMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod13_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod13_Object = MibScalar
eBattUnderVolWarningMod13 = _EBattUnderVolWarningMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 233),
    _EBattUnderVolWarningMod13_Type()
)
eBattUnderVolWarningMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod13.setStatus("current")


class _EBattUnderVolWarningMod14_Type(Integer32):
    """Custom type eBattUnderVolWarningMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod14_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod14_Object = MibScalar
eBattUnderVolWarningMod14 = _EBattUnderVolWarningMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 234),
    _EBattUnderVolWarningMod14_Type()
)
eBattUnderVolWarningMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod14.setStatus("current")


class _EBattUnderVolWarningMod15_Type(Integer32):
    """Custom type eBattUnderVolWarningMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattUnderVolWarningMod15_Type.__name__ = "Integer32"
_EBattUnderVolWarningMod15_Object = MibScalar
eBattUnderVolWarningMod15 = _EBattUnderVolWarningMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 235),
    _EBattUnderVolWarningMod15_Type()
)
eBattUnderVolWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod15.setStatus("current")


class _EBattOverVolWarningMod8_Type(Integer32):
    """Custom type eBattOverVolWarningMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod8_Type.__name__ = "Integer32"
_EBattOverVolWarningMod8_Object = MibScalar
eBattOverVolWarningMod8 = _EBattOverVolWarningMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 236),
    _EBattOverVolWarningMod8_Type()
)
eBattOverVolWarningMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod8.setStatus("current")


class _EBattOverVolWarningMod9_Type(Integer32):
    """Custom type eBattOverVolWarningMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod9_Type.__name__ = "Integer32"
_EBattOverVolWarningMod9_Object = MibScalar
eBattOverVolWarningMod9 = _EBattOverVolWarningMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 237),
    _EBattOverVolWarningMod9_Type()
)
eBattOverVolWarningMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod9.setStatus("current")


class _EBattOverVolWarningMod10_Type(Integer32):
    """Custom type eBattOverVolWarningMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod10_Type.__name__ = "Integer32"
_EBattOverVolWarningMod10_Object = MibScalar
eBattOverVolWarningMod10 = _EBattOverVolWarningMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 238),
    _EBattOverVolWarningMod10_Type()
)
eBattOverVolWarningMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod10.setStatus("current")


class _EBattOverVolWarningMod11_Type(Integer32):
    """Custom type eBattOverVolWarningMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod11_Type.__name__ = "Integer32"
_EBattOverVolWarningMod11_Object = MibScalar
eBattOverVolWarningMod11 = _EBattOverVolWarningMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 239),
    _EBattOverVolWarningMod11_Type()
)
eBattOverVolWarningMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod11.setStatus("current")


class _EBattOverVolWarningMod12_Type(Integer32):
    """Custom type eBattOverVolWarningMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod12_Type.__name__ = "Integer32"
_EBattOverVolWarningMod12_Object = MibScalar
eBattOverVolWarningMod12 = _EBattOverVolWarningMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 240),
    _EBattOverVolWarningMod12_Type()
)
eBattOverVolWarningMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod12.setStatus("current")


class _EBattOverVolWarningMod13_Type(Integer32):
    """Custom type eBattOverVolWarningMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod13_Type.__name__ = "Integer32"
_EBattOverVolWarningMod13_Object = MibScalar
eBattOverVolWarningMod13 = _EBattOverVolWarningMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 241),
    _EBattOverVolWarningMod13_Type()
)
eBattOverVolWarningMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod13.setStatus("current")


class _EBattOverVolWarningMod14_Type(Integer32):
    """Custom type eBattOverVolWarningMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod14_Type.__name__ = "Integer32"
_EBattOverVolWarningMod14_Object = MibScalar
eBattOverVolWarningMod14 = _EBattOverVolWarningMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 242),
    _EBattOverVolWarningMod14_Type()
)
eBattOverVolWarningMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod14.setStatus("current")


class _EBattOverVolWarningMod15_Type(Integer32):
    """Custom type eBattOverVolWarningMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolWarningMod15_Type.__name__ = "Integer32"
_EBattOverVolWarningMod15_Object = MibScalar
eBattOverVolWarningMod15 = _EBattOverVolWarningMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 243),
    _EBattOverVolWarningMod15_Type()
)
eBattOverVolWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod15.setStatus("current")


class _ECellChgOverTempProtMod8_Type(Integer32):
    """Custom type eCellChgOverTempProtMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod8_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod8_Object = MibScalar
eCellChgOverTempProtMod8 = _ECellChgOverTempProtMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 244),
    _ECellChgOverTempProtMod8_Type()
)
eCellChgOverTempProtMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod8.setStatus("current")


class _ECellChgOverTempProtMod9_Type(Integer32):
    """Custom type eCellChgOverTempProtMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod9_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod9_Object = MibScalar
eCellChgOverTempProtMod9 = _ECellChgOverTempProtMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 245),
    _ECellChgOverTempProtMod9_Type()
)
eCellChgOverTempProtMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod9.setStatus("current")


class _ECellChgOverTempProtMod10_Type(Integer32):
    """Custom type eCellChgOverTempProtMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod10_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod10_Object = MibScalar
eCellChgOverTempProtMod10 = _ECellChgOverTempProtMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 246),
    _ECellChgOverTempProtMod10_Type()
)
eCellChgOverTempProtMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod10.setStatus("current")


class _ECellChgOverTempProtMod11_Type(Integer32):
    """Custom type eCellChgOverTempProtMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod11_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod11_Object = MibScalar
eCellChgOverTempProtMod11 = _ECellChgOverTempProtMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 247),
    _ECellChgOverTempProtMod11_Type()
)
eCellChgOverTempProtMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod11.setStatus("current")


class _ECellChgOverTempProtMod12_Type(Integer32):
    """Custom type eCellChgOverTempProtMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod12_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod12_Object = MibScalar
eCellChgOverTempProtMod12 = _ECellChgOverTempProtMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 248),
    _ECellChgOverTempProtMod12_Type()
)
eCellChgOverTempProtMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod12.setStatus("current")


class _ECellChgOverTempProtMod13_Type(Integer32):
    """Custom type eCellChgOverTempProtMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod13_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod13_Object = MibScalar
eCellChgOverTempProtMod13 = _ECellChgOverTempProtMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 249),
    _ECellChgOverTempProtMod13_Type()
)
eCellChgOverTempProtMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod13.setStatus("current")


class _ECellChgOverTempProtMod14_Type(Integer32):
    """Custom type eCellChgOverTempProtMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod14_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod14_Object = MibScalar
eCellChgOverTempProtMod14 = _ECellChgOverTempProtMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 250),
    _ECellChgOverTempProtMod14_Type()
)
eCellChgOverTempProtMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod14.setStatus("current")


class _ECellChgOverTempProtMod15_Type(Integer32):
    """Custom type eCellChgOverTempProtMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellChgOverTempProtMod15_Type.__name__ = "Integer32"
_ECellChgOverTempProtMod15_Object = MibScalar
eCellChgOverTempProtMod15 = _ECellChgOverTempProtMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 251),
    _ECellChgOverTempProtMod15_Type()
)
eCellChgOverTempProtMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod15.setStatus("current")


class _ECellDisChgOverTempProtMod8_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod8_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod8_Object = MibScalar
eCellDisChgOverTempProtMod8 = _ECellDisChgOverTempProtMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 252),
    _ECellDisChgOverTempProtMod8_Type()
)
eCellDisChgOverTempProtMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod8.setStatus("current")


class _ECellDisChgOverTempProtMod9_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod9_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod9_Object = MibScalar
eCellDisChgOverTempProtMod9 = _ECellDisChgOverTempProtMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 253),
    _ECellDisChgOverTempProtMod9_Type()
)
eCellDisChgOverTempProtMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod9.setStatus("current")


class _ECellDisChgOverTempProtMod10_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod10_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod10_Object = MibScalar
eCellDisChgOverTempProtMod10 = _ECellDisChgOverTempProtMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 254),
    _ECellDisChgOverTempProtMod10_Type()
)
eCellDisChgOverTempProtMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod10.setStatus("current")


class _ECellDisChgOverTempProtMod11_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod11_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod11_Object = MibScalar
eCellDisChgOverTempProtMod11 = _ECellDisChgOverTempProtMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 255),
    _ECellDisChgOverTempProtMod11_Type()
)
eCellDisChgOverTempProtMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod11.setStatus("current")


class _ECellDisChgOverTempProtMod12_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod12_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod12_Object = MibScalar
eCellDisChgOverTempProtMod12 = _ECellDisChgOverTempProtMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 256),
    _ECellDisChgOverTempProtMod12_Type()
)
eCellDisChgOverTempProtMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod12.setStatus("current")


class _ECellDisChgOverTempProtMod13_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod13_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod13_Object = MibScalar
eCellDisChgOverTempProtMod13 = _ECellDisChgOverTempProtMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 257),
    _ECellDisChgOverTempProtMod13_Type()
)
eCellDisChgOverTempProtMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod13.setStatus("current")


class _ECellDisChgOverTempProtMod14_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod14_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod14_Object = MibScalar
eCellDisChgOverTempProtMod14 = _ECellDisChgOverTempProtMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 258),
    _ECellDisChgOverTempProtMod14_Type()
)
eCellDisChgOverTempProtMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod14.setStatus("current")


class _ECellDisChgOverTempProtMod15_Type(Integer32):
    """Custom type eCellDisChgOverTempProtMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellDisChgOverTempProtMod15_Type.__name__ = "Integer32"
_ECellDisChgOverTempProtMod15_Object = MibScalar
eCellDisChgOverTempProtMod15 = _ECellDisChgOverTempProtMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 259),
    _ECellDisChgOverTempProtMod15_Type()
)
eCellDisChgOverTempProtMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod15.setStatus("current")


class _EAnyCellUnderTempProtMod8_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod8_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod8_Object = MibScalar
eAnyCellUnderTempProtMod8 = _EAnyCellUnderTempProtMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 260),
    _EAnyCellUnderTempProtMod8_Type()
)
eAnyCellUnderTempProtMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod8.setStatus("current")


class _EAnyCellUnderTempProtMod9_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod9_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod9_Object = MibScalar
eAnyCellUnderTempProtMod9 = _EAnyCellUnderTempProtMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 261),
    _EAnyCellUnderTempProtMod9_Type()
)
eAnyCellUnderTempProtMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod9.setStatus("current")


class _EAnyCellUnderTempProtMod10_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod10_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod10_Object = MibScalar
eAnyCellUnderTempProtMod10 = _EAnyCellUnderTempProtMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 262),
    _EAnyCellUnderTempProtMod10_Type()
)
eAnyCellUnderTempProtMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod10.setStatus("current")


class _EAnyCellUnderTempProtMod11_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod11_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod11_Object = MibScalar
eAnyCellUnderTempProtMod11 = _EAnyCellUnderTempProtMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 263),
    _EAnyCellUnderTempProtMod11_Type()
)
eAnyCellUnderTempProtMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod11.setStatus("current")


class _EAnyCellUnderTempProtMod12_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod12_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod12_Object = MibScalar
eAnyCellUnderTempProtMod12 = _EAnyCellUnderTempProtMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 264),
    _EAnyCellUnderTempProtMod12_Type()
)
eAnyCellUnderTempProtMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod12.setStatus("current")


class _EAnyCellUnderTempProtMod13_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod13_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod13_Object = MibScalar
eAnyCellUnderTempProtMod13 = _EAnyCellUnderTempProtMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 265),
    _EAnyCellUnderTempProtMod13_Type()
)
eAnyCellUnderTempProtMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod13.setStatus("current")


class _EAnyCellUnderTempProtMod14_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod14_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod14_Object = MibScalar
eAnyCellUnderTempProtMod14 = _EAnyCellUnderTempProtMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 266),
    _EAnyCellUnderTempProtMod14_Type()
)
eAnyCellUnderTempProtMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod14.setStatus("current")


class _EAnyCellUnderTempProtMod15_Type(Integer32):
    """Custom type eAnyCellUnderTempProtMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EAnyCellUnderTempProtMod15_Type.__name__ = "Integer32"
_EAnyCellUnderTempProtMod15_Object = MibScalar
eAnyCellUnderTempProtMod15 = _EAnyCellUnderTempProtMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 267),
    _EAnyCellUnderTempProtMod15_Type()
)
eAnyCellUnderTempProtMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod15.setStatus("current")


class _EBattChgOverCurrWarningMod8_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod8_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod8_Object = MibScalar
eBattChgOverCurrWarningMod8 = _EBattChgOverCurrWarningMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 268),
    _EBattChgOverCurrWarningMod8_Type()
)
eBattChgOverCurrWarningMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod8.setStatus("current")


class _EBattChgOverCurrWarningMod9_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod9_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod9_Object = MibScalar
eBattChgOverCurrWarningMod9 = _EBattChgOverCurrWarningMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 269),
    _EBattChgOverCurrWarningMod9_Type()
)
eBattChgOverCurrWarningMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod9.setStatus("current")


class _EBattChgOverCurrWarningMod10_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod10_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod10_Object = MibScalar
eBattChgOverCurrWarningMod10 = _EBattChgOverCurrWarningMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 270),
    _EBattChgOverCurrWarningMod10_Type()
)
eBattChgOverCurrWarningMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod10.setStatus("current")


class _EBattChgOverCurrWarningMod11_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod11_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod11_Object = MibScalar
eBattChgOverCurrWarningMod11 = _EBattChgOverCurrWarningMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 271),
    _EBattChgOverCurrWarningMod11_Type()
)
eBattChgOverCurrWarningMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod11.setStatus("current")


class _EBattChgOverCurrWarningMod12_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod12_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod12_Object = MibScalar
eBattChgOverCurrWarningMod12 = _EBattChgOverCurrWarningMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 272),
    _EBattChgOverCurrWarningMod12_Type()
)
eBattChgOverCurrWarningMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod12.setStatus("current")


class _EBattChgOverCurrWarningMod13_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod13_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod13_Object = MibScalar
eBattChgOverCurrWarningMod13 = _EBattChgOverCurrWarningMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 273),
    _EBattChgOverCurrWarningMod13_Type()
)
eBattChgOverCurrWarningMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod13.setStatus("current")


class _EBattChgOverCurrWarningMod14_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod14_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod14_Object = MibScalar
eBattChgOverCurrWarningMod14 = _EBattChgOverCurrWarningMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 274),
    _EBattChgOverCurrWarningMod14_Type()
)
eBattChgOverCurrWarningMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod14.setStatus("current")


class _EBattChgOverCurrWarningMod15_Type(Integer32):
    """Custom type eBattChgOverCurrWarningMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattChgOverCurrWarningMod15_Type.__name__ = "Integer32"
_EBattChgOverCurrWarningMod15_Object = MibScalar
eBattChgOverCurrWarningMod15 = _EBattChgOverCurrWarningMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 275),
    _EBattChgOverCurrWarningMod15_Type()
)
eBattChgOverCurrWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod15.setStatus("current")


class _EBattDisChgOverCurrWarnMod8_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod8_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod8_Object = MibScalar
eBattDisChgOverCurrWarnMod8 = _EBattDisChgOverCurrWarnMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 276),
    _EBattDisChgOverCurrWarnMod8_Type()
)
eBattDisChgOverCurrWarnMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod8.setStatus("current")


class _EBattDisChgOverCurrWarnMod9_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod9_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod9_Object = MibScalar
eBattDisChgOverCurrWarnMod9 = _EBattDisChgOverCurrWarnMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 277),
    _EBattDisChgOverCurrWarnMod9_Type()
)
eBattDisChgOverCurrWarnMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod9.setStatus("current")


class _EBattDisChgOverCurrWarnMod10_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod10_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod10_Object = MibScalar
eBattDisChgOverCurrWarnMod10 = _EBattDisChgOverCurrWarnMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 278),
    _EBattDisChgOverCurrWarnMod10_Type()
)
eBattDisChgOverCurrWarnMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod10.setStatus("current")


class _EBattDisChgOverCurrWarnMod11_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod11_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod11_Object = MibScalar
eBattDisChgOverCurrWarnMod11 = _EBattDisChgOverCurrWarnMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 279),
    _EBattDisChgOverCurrWarnMod11_Type()
)
eBattDisChgOverCurrWarnMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod11.setStatus("current")


class _EBattDisChgOverCurrWarnMod12_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod12_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod12_Object = MibScalar
eBattDisChgOverCurrWarnMod12 = _EBattDisChgOverCurrWarnMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 280),
    _EBattDisChgOverCurrWarnMod12_Type()
)
eBattDisChgOverCurrWarnMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod12.setStatus("current")


class _EBattDisChgOverCurrWarnMod13_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod13_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod13_Object = MibScalar
eBattDisChgOverCurrWarnMod13 = _EBattDisChgOverCurrWarnMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 281),
    _EBattDisChgOverCurrWarnMod13_Type()
)
eBattDisChgOverCurrWarnMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod13.setStatus("current")


class _EBattDisChgOverCurrWarnMod14_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod14_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod14_Object = MibScalar
eBattDisChgOverCurrWarnMod14 = _EBattDisChgOverCurrWarnMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 282),
    _EBattDisChgOverCurrWarnMod14_Type()
)
eBattDisChgOverCurrWarnMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod14.setStatus("current")


class _EBattDisChgOverCurrWarnMod15_Type(Integer32):
    """Custom type eBattDisChgOverCurrWarnMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattDisChgOverCurrWarnMod15_Type.__name__ = "Integer32"
_EBattDisChgOverCurrWarnMod15_Object = MibScalar
eBattDisChgOverCurrWarnMod15 = _EBattDisChgOverCurrWarnMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 283),
    _EBattDisChgOverCurrWarnMod15_Type()
)
eBattDisChgOverCurrWarnMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod15.setStatus("current")


class _EBattLowSOCWarningMod8_Type(Integer32):
    """Custom type eBattLowSOCWarningMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod8_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod8_Object = MibScalar
eBattLowSOCWarningMod8 = _EBattLowSOCWarningMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 284),
    _EBattLowSOCWarningMod8_Type()
)
eBattLowSOCWarningMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod8.setStatus("current")


class _EBattLowSOCWarningMod9_Type(Integer32):
    """Custom type eBattLowSOCWarningMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod9_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod9_Object = MibScalar
eBattLowSOCWarningMod9 = _EBattLowSOCWarningMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 285),
    _EBattLowSOCWarningMod9_Type()
)
eBattLowSOCWarningMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod9.setStatus("current")


class _EBattLowSOCWarningMod10_Type(Integer32):
    """Custom type eBattLowSOCWarningMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod10_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod10_Object = MibScalar
eBattLowSOCWarningMod10 = _EBattLowSOCWarningMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 286),
    _EBattLowSOCWarningMod10_Type()
)
eBattLowSOCWarningMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod10.setStatus("current")


class _EBattLowSOCWarningMod11_Type(Integer32):
    """Custom type eBattLowSOCWarningMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod11_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod11_Object = MibScalar
eBattLowSOCWarningMod11 = _EBattLowSOCWarningMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 287),
    _EBattLowSOCWarningMod11_Type()
)
eBattLowSOCWarningMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod11.setStatus("current")


class _EBattLowSOCWarningMod12_Type(Integer32):
    """Custom type eBattLowSOCWarningMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod12_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod12_Object = MibScalar
eBattLowSOCWarningMod12 = _EBattLowSOCWarningMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 288),
    _EBattLowSOCWarningMod12_Type()
)
eBattLowSOCWarningMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod12.setStatus("current")


class _EBattLowSOCWarningMod13_Type(Integer32):
    """Custom type eBattLowSOCWarningMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod13_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod13_Object = MibScalar
eBattLowSOCWarningMod13 = _EBattLowSOCWarningMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 289),
    _EBattLowSOCWarningMod13_Type()
)
eBattLowSOCWarningMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod13.setStatus("current")


class _EBattLowSOCWarningMod14_Type(Integer32):
    """Custom type eBattLowSOCWarningMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod14_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod14_Object = MibScalar
eBattLowSOCWarningMod14 = _EBattLowSOCWarningMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 290),
    _EBattLowSOCWarningMod14_Type()
)
eBattLowSOCWarningMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod14.setStatus("current")


class _EBattLowSOCWarningMod15_Type(Integer32):
    """Custom type eBattLowSOCWarningMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattLowSOCWarningMod15_Type.__name__ = "Integer32"
_EBattLowSOCWarningMod15_Object = MibScalar
eBattLowSOCWarningMod15 = _EBattLowSOCWarningMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 291),
    _EBattLowSOCWarningMod15_Type()
)
eBattLowSOCWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod15.setStatus("current")


class _EBattOverCurrProtectionMod8_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod8_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod8_Object = MibScalar
eBattOverCurrProtectionMod8 = _EBattOverCurrProtectionMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 292),
    _EBattOverCurrProtectionMod8_Type()
)
eBattOverCurrProtectionMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod8.setStatus("current")


class _EBattOverCurrProtectionMod9_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod9_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod9_Object = MibScalar
eBattOverCurrProtectionMod9 = _EBattOverCurrProtectionMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 293),
    _EBattOverCurrProtectionMod9_Type()
)
eBattOverCurrProtectionMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod9.setStatus("current")


class _EBattOverCurrProtectionMod10_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod10_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod10_Object = MibScalar
eBattOverCurrProtectionMod10 = _EBattOverCurrProtectionMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 294),
    _EBattOverCurrProtectionMod10_Type()
)
eBattOverCurrProtectionMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod10.setStatus("current")


class _EBattOverCurrProtectionMod11_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod11_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod11_Object = MibScalar
eBattOverCurrProtectionMod11 = _EBattOverCurrProtectionMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 295),
    _EBattOverCurrProtectionMod11_Type()
)
eBattOverCurrProtectionMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod11.setStatus("current")


class _EBattOverCurrProtectionMod12_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod12_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod12_Object = MibScalar
eBattOverCurrProtectionMod12 = _EBattOverCurrProtectionMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 296),
    _EBattOverCurrProtectionMod12_Type()
)
eBattOverCurrProtectionMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod12.setStatus("current")


class _EBattOverCurrProtectionMod13_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod13_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod13_Object = MibScalar
eBattOverCurrProtectionMod13 = _EBattOverCurrProtectionMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 297),
    _EBattOverCurrProtectionMod13_Type()
)
eBattOverCurrProtectionMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod13.setStatus("current")


class _EBattOverCurrProtectionMod14_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod14_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod14_Object = MibScalar
eBattOverCurrProtectionMod14 = _EBattOverCurrProtectionMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 298),
    _EBattOverCurrProtectionMod14_Type()
)
eBattOverCurrProtectionMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod14.setStatus("current")


class _EBattOverCurrProtectionMod15_Type(Integer32):
    """Custom type eBattOverCurrProtectionMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverCurrProtectionMod15_Type.__name__ = "Integer32"
_EBattOverCurrProtectionMod15_Object = MibScalar
eBattOverCurrProtectionMod15 = _EBattOverCurrProtectionMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 299),
    _EBattOverCurrProtectionMod15_Type()
)
eBattOverCurrProtectionMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod15.setStatus("current")


class _EModule8Isolated_Type(Integer32):
    """Custom type eModule8Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule8Isolated_Type.__name__ = "Integer32"
_EModule8Isolated_Object = MibScalar
eModule8Isolated = _EModule8Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 300),
    _EModule8Isolated_Type()
)
eModule8Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule8Isolated.setStatus("current")


class _EModule9Isolated_Type(Integer32):
    """Custom type eModule9Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule9Isolated_Type.__name__ = "Integer32"
_EModule9Isolated_Object = MibScalar
eModule9Isolated = _EModule9Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 301),
    _EModule9Isolated_Type()
)
eModule9Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule9Isolated.setStatus("current")


class _EModule10Isolated_Type(Integer32):
    """Custom type eModule10Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule10Isolated_Type.__name__ = "Integer32"
_EModule10Isolated_Object = MibScalar
eModule10Isolated = _EModule10Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 302),
    _EModule10Isolated_Type()
)
eModule10Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule10Isolated.setStatus("current")


class _EModule11Isolated_Type(Integer32):
    """Custom type eModule11Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule11Isolated_Type.__name__ = "Integer32"
_EModule11Isolated_Object = MibScalar
eModule11Isolated = _EModule11Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 303),
    _EModule11Isolated_Type()
)
eModule11Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule11Isolated.setStatus("current")


class _EModule12Isolated_Type(Integer32):
    """Custom type eModule12Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule12Isolated_Type.__name__ = "Integer32"
_EModule12Isolated_Object = MibScalar
eModule12Isolated = _EModule12Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 304),
    _EModule12Isolated_Type()
)
eModule12Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule12Isolated.setStatus("current")


class _EModule13Isolated_Type(Integer32):
    """Custom type eModule13Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule13Isolated_Type.__name__ = "Integer32"
_EModule13Isolated_Object = MibScalar
eModule13Isolated = _EModule13Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 305),
    _EModule13Isolated_Type()
)
eModule13Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule13Isolated.setStatus("current")


class _EModule14Isolated_Type(Integer32):
    """Custom type eModule14Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule14Isolated_Type.__name__ = "Integer32"
_EModule14Isolated_Object = MibScalar
eModule14Isolated = _EModule14Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 306),
    _EModule14Isolated_Type()
)
eModule14Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule14Isolated.setStatus("current")


class _EModule15Isolated_Type(Integer32):
    """Custom type eModule15Isolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule15Isolated_Type.__name__ = "Integer32"
_EModule15Isolated_Object = MibScalar
eModule15Isolated = _EModule15Isolated_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 307),
    _EModule15Isolated_Type()
)
eModule15Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule15Isolated.setStatus("current")


class _EModule8CommFailAlarm_Type(Integer32):
    """Custom type eModule8CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule8CommFailAlarm_Type.__name__ = "Integer32"
_EModule8CommFailAlarm_Object = MibScalar
eModule8CommFailAlarm = _EModule8CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 308),
    _EModule8CommFailAlarm_Type()
)
eModule8CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule8CommFailAlarm.setStatus("current")


class _EModule9CommFailAlarm_Type(Integer32):
    """Custom type eModule9CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule9CommFailAlarm_Type.__name__ = "Integer32"
_EModule9CommFailAlarm_Object = MibScalar
eModule9CommFailAlarm = _EModule9CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 309),
    _EModule9CommFailAlarm_Type()
)
eModule9CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule9CommFailAlarm.setStatus("current")


class _EModule10CommFailAlarm_Type(Integer32):
    """Custom type eModule10CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule10CommFailAlarm_Type.__name__ = "Integer32"
_EModule10CommFailAlarm_Object = MibScalar
eModule10CommFailAlarm = _EModule10CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 310),
    _EModule10CommFailAlarm_Type()
)
eModule10CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule10CommFailAlarm.setStatus("current")


class _EModule11CommFailAlarm_Type(Integer32):
    """Custom type eModule11CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule11CommFailAlarm_Type.__name__ = "Integer32"
_EModule11CommFailAlarm_Object = MibScalar
eModule11CommFailAlarm = _EModule11CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 311),
    _EModule11CommFailAlarm_Type()
)
eModule11CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule11CommFailAlarm.setStatus("current")


class _EModule12CommFailAlarm_Type(Integer32):
    """Custom type eModule12CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule12CommFailAlarm_Type.__name__ = "Integer32"
_EModule12CommFailAlarm_Object = MibScalar
eModule12CommFailAlarm = _EModule12CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 312),
    _EModule12CommFailAlarm_Type()
)
eModule12CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule12CommFailAlarm.setStatus("current")


class _EModule13CommFailAlarm_Type(Integer32):
    """Custom type eModule13CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule13CommFailAlarm_Type.__name__ = "Integer32"
_EModule13CommFailAlarm_Object = MibScalar
eModule13CommFailAlarm = _EModule13CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 313),
    _EModule13CommFailAlarm_Type()
)
eModule13CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule13CommFailAlarm.setStatus("current")


class _EModule14CommFailAlarm_Type(Integer32):
    """Custom type eModule14CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule14CommFailAlarm_Type.__name__ = "Integer32"
_EModule14CommFailAlarm_Object = MibScalar
eModule14CommFailAlarm = _EModule14CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 314),
    _EModule14CommFailAlarm_Type()
)
eModule14CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule14CommFailAlarm.setStatus("current")


class _EModule15CommFailAlarm_Type(Integer32):
    """Custom type eModule15CommFailAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EModule15CommFailAlarm_Type.__name__ = "Integer32"
_EModule15CommFailAlarm_Object = MibScalar
eModule15CommFailAlarm = _EModule15CommFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 1, 1, 315),
    _EModule15CommFailAlarm_Type()
)
eModule15CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule15CommFailAlarm.setStatus("current")
_EParameters_ObjectIdentity = ObjectIdentity
eParameters = _EParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2)
)
_ECurrentInfo_ObjectIdentity = ObjectIdentity
eCurrentInfo = _ECurrentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1)
)
_EChargingCurrentModule1_Type = DisplayString
_EChargingCurrentModule1_Object = MibScalar
eChargingCurrentModule1 = _EChargingCurrentModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 1),
    _EChargingCurrentModule1_Type()
)
eChargingCurrentModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule1.setStatus("current")
_EChargingCurrentModule2_Type = DisplayString
_EChargingCurrentModule2_Object = MibScalar
eChargingCurrentModule2 = _EChargingCurrentModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 2),
    _EChargingCurrentModule2_Type()
)
eChargingCurrentModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule2.setStatus("current")
_EChargingCurrentModule3_Type = DisplayString
_EChargingCurrentModule3_Object = MibScalar
eChargingCurrentModule3 = _EChargingCurrentModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 3),
    _EChargingCurrentModule3_Type()
)
eChargingCurrentModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule3.setStatus("current")
_EChargingCurrentModule4_Type = DisplayString
_EChargingCurrentModule4_Object = MibScalar
eChargingCurrentModule4 = _EChargingCurrentModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 4),
    _EChargingCurrentModule4_Type()
)
eChargingCurrentModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule4.setStatus("current")
_EChargingCurrentModule5_Type = DisplayString
_EChargingCurrentModule5_Object = MibScalar
eChargingCurrentModule5 = _EChargingCurrentModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 5),
    _EChargingCurrentModule5_Type()
)
eChargingCurrentModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule5.setStatus("current")
_EChargingCurrentModule6_Type = DisplayString
_EChargingCurrentModule6_Object = MibScalar
eChargingCurrentModule6 = _EChargingCurrentModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 6),
    _EChargingCurrentModule6_Type()
)
eChargingCurrentModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule6.setStatus("current")
_EChargingCurrentModule7_Type = DisplayString
_EChargingCurrentModule7_Object = MibScalar
eChargingCurrentModule7 = _EChargingCurrentModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 7),
    _EChargingCurrentModule7_Type()
)
eChargingCurrentModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule7.setStatus("current")
_EChargingCurrentModule8_Type = DisplayString
_EChargingCurrentModule8_Object = MibScalar
eChargingCurrentModule8 = _EChargingCurrentModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 8),
    _EChargingCurrentModule8_Type()
)
eChargingCurrentModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule8.setStatus("current")
_EChargingCurrentModule9_Type = DisplayString
_EChargingCurrentModule9_Object = MibScalar
eChargingCurrentModule9 = _EChargingCurrentModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 9),
    _EChargingCurrentModule9_Type()
)
eChargingCurrentModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule9.setStatus("current")
_EChargingCurrentModule10_Type = DisplayString
_EChargingCurrentModule10_Object = MibScalar
eChargingCurrentModule10 = _EChargingCurrentModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 10),
    _EChargingCurrentModule10_Type()
)
eChargingCurrentModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule10.setStatus("current")
_EChargingCurrentModule11_Type = DisplayString
_EChargingCurrentModule11_Object = MibScalar
eChargingCurrentModule11 = _EChargingCurrentModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 11),
    _EChargingCurrentModule11_Type()
)
eChargingCurrentModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule11.setStatus("current")
_EChargingCurrentModule12_Type = DisplayString
_EChargingCurrentModule12_Object = MibScalar
eChargingCurrentModule12 = _EChargingCurrentModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 12),
    _EChargingCurrentModule12_Type()
)
eChargingCurrentModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule12.setStatus("current")
_EChargingCurrentModule13_Type = DisplayString
_EChargingCurrentModule13_Object = MibScalar
eChargingCurrentModule13 = _EChargingCurrentModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 13),
    _EChargingCurrentModule13_Type()
)
eChargingCurrentModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule13.setStatus("current")
_EChargingCurrentModule14_Type = DisplayString
_EChargingCurrentModule14_Object = MibScalar
eChargingCurrentModule14 = _EChargingCurrentModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 14),
    _EChargingCurrentModule14_Type()
)
eChargingCurrentModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule14.setStatus("current")
_EChargingCurrentModule15_Type = DisplayString
_EChargingCurrentModule15_Object = MibScalar
eChargingCurrentModule15 = _EChargingCurrentModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 15),
    _EChargingCurrentModule15_Type()
)
eChargingCurrentModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule15.setStatus("current")
_EDischargingCurrentModule1_Type = DisplayString
_EDischargingCurrentModule1_Object = MibScalar
eDischargingCurrentModule1 = _EDischargingCurrentModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 16),
    _EDischargingCurrentModule1_Type()
)
eDischargingCurrentModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule1.setStatus("current")
_EDischargingCurrentModule2_Type = DisplayString
_EDischargingCurrentModule2_Object = MibScalar
eDischargingCurrentModule2 = _EDischargingCurrentModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 17),
    _EDischargingCurrentModule2_Type()
)
eDischargingCurrentModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule2.setStatus("current")
_EDischargingCurrentModule3_Type = DisplayString
_EDischargingCurrentModule3_Object = MibScalar
eDischargingCurrentModule3 = _EDischargingCurrentModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 18),
    _EDischargingCurrentModule3_Type()
)
eDischargingCurrentModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule3.setStatus("current")
_EDischargingCurrentModule4_Type = DisplayString
_EDischargingCurrentModule4_Object = MibScalar
eDischargingCurrentModule4 = _EDischargingCurrentModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 19),
    _EDischargingCurrentModule4_Type()
)
eDischargingCurrentModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule4.setStatus("current")
_EDischargingCurrentModule5_Type = DisplayString
_EDischargingCurrentModule5_Object = MibScalar
eDischargingCurrentModule5 = _EDischargingCurrentModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 20),
    _EDischargingCurrentModule5_Type()
)
eDischargingCurrentModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule5.setStatus("current")
_EDischargingCurrentModule6_Type = DisplayString
_EDischargingCurrentModule6_Object = MibScalar
eDischargingCurrentModule6 = _EDischargingCurrentModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 21),
    _EDischargingCurrentModule6_Type()
)
eDischargingCurrentModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule6.setStatus("current")
_EDischargingCurrentModule7_Type = DisplayString
_EDischargingCurrentModule7_Object = MibScalar
eDischargingCurrentModule7 = _EDischargingCurrentModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 22),
    _EDischargingCurrentModule7_Type()
)
eDischargingCurrentModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule7.setStatus("current")
_EDischargingCurrentModule8_Type = DisplayString
_EDischargingCurrentModule8_Object = MibScalar
eDischargingCurrentModule8 = _EDischargingCurrentModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 23),
    _EDischargingCurrentModule8_Type()
)
eDischargingCurrentModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule8.setStatus("current")
_EDischargingCurrentModule9_Type = DisplayString
_EDischargingCurrentModule9_Object = MibScalar
eDischargingCurrentModule9 = _EDischargingCurrentModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 24),
    _EDischargingCurrentModule9_Type()
)
eDischargingCurrentModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule9.setStatus("current")
_EDischargingCurrentModule10_Type = DisplayString
_EDischargingCurrentModule10_Object = MibScalar
eDischargingCurrentModule10 = _EDischargingCurrentModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 25),
    _EDischargingCurrentModule10_Type()
)
eDischargingCurrentModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule10.setStatus("current")
_EDischargingCurrentModule11_Type = DisplayString
_EDischargingCurrentModule11_Object = MibScalar
eDischargingCurrentModule11 = _EDischargingCurrentModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 26),
    _EDischargingCurrentModule11_Type()
)
eDischargingCurrentModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule11.setStatus("current")
_EDischargingCurrentModule12_Type = DisplayString
_EDischargingCurrentModule12_Object = MibScalar
eDischargingCurrentModule12 = _EDischargingCurrentModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 27),
    _EDischargingCurrentModule12_Type()
)
eDischargingCurrentModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule12.setStatus("current")
_EDischargingCurrentModule13_Type = DisplayString
_EDischargingCurrentModule13_Object = MibScalar
eDischargingCurrentModule13 = _EDischargingCurrentModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 28),
    _EDischargingCurrentModule13_Type()
)
eDischargingCurrentModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule13.setStatus("current")
_EDischargingCurrentModule14_Type = DisplayString
_EDischargingCurrentModule14_Object = MibScalar
eDischargingCurrentModule14 = _EDischargingCurrentModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 29),
    _EDischargingCurrentModule14_Type()
)
eDischargingCurrentModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule14.setStatus("current")
_EDischargingCurrentModule15_Type = DisplayString
_EDischargingCurrentModule15_Object = MibScalar
eDischargingCurrentModule15 = _EDischargingCurrentModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 1, 30),
    _EDischargingCurrentModule15_Type()
)
eDischargingCurrentModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDischargingCurrentModule15.setStatus("current")
_ESOCinfo_ObjectIdentity = ObjectIdentity
eSOCinfo = _ESOCinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2)
)
_ESOCModule1_Type = DisplayString
_ESOCModule1_Object = MibScalar
eSOCModule1 = _ESOCModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 1),
    _ESOCModule1_Type()
)
eSOCModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule1.setStatus("current")
_ESOCModule2_Type = DisplayString
_ESOCModule2_Object = MibScalar
eSOCModule2 = _ESOCModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 2),
    _ESOCModule2_Type()
)
eSOCModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule2.setStatus("current")
_ESOCModule3_Type = DisplayString
_ESOCModule3_Object = MibScalar
eSOCModule3 = _ESOCModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 3),
    _ESOCModule3_Type()
)
eSOCModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule3.setStatus("current")
_ESOCModule4_Type = DisplayString
_ESOCModule4_Object = MibScalar
eSOCModule4 = _ESOCModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 4),
    _ESOCModule4_Type()
)
eSOCModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule4.setStatus("current")
_ESOCModule5_Type = DisplayString
_ESOCModule5_Object = MibScalar
eSOCModule5 = _ESOCModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 5),
    _ESOCModule5_Type()
)
eSOCModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule5.setStatus("current")
_ESOCModule6_Type = DisplayString
_ESOCModule6_Object = MibScalar
eSOCModule6 = _ESOCModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 6),
    _ESOCModule6_Type()
)
eSOCModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule6.setStatus("current")
_ESOCModule7_Type = DisplayString
_ESOCModule7_Object = MibScalar
eSOCModule7 = _ESOCModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 7),
    _ESOCModule7_Type()
)
eSOCModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule7.setStatus("current")
_ESOCModule8_Type = DisplayString
_ESOCModule8_Object = MibScalar
eSOCModule8 = _ESOCModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 8),
    _ESOCModule8_Type()
)
eSOCModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule8.setStatus("current")
_ESOCModule9_Type = DisplayString
_ESOCModule9_Object = MibScalar
eSOCModule9 = _ESOCModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 9),
    _ESOCModule9_Type()
)
eSOCModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule9.setStatus("current")
_ESOCModule10_Type = DisplayString
_ESOCModule10_Object = MibScalar
eSOCModule10 = _ESOCModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 10),
    _ESOCModule10_Type()
)
eSOCModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule10.setStatus("current")
_ESOCModule11_Type = DisplayString
_ESOCModule11_Object = MibScalar
eSOCModule11 = _ESOCModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 11),
    _ESOCModule11_Type()
)
eSOCModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule11.setStatus("current")
_ESOCModule12_Type = DisplayString
_ESOCModule12_Object = MibScalar
eSOCModule12 = _ESOCModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 12),
    _ESOCModule12_Type()
)
eSOCModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule12.setStatus("current")
_ESOCModule13_Type = DisplayString
_ESOCModule13_Object = MibScalar
eSOCModule13 = _ESOCModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 13),
    _ESOCModule13_Type()
)
eSOCModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule13.setStatus("current")
_ESOCModule14_Type = DisplayString
_ESOCModule14_Object = MibScalar
eSOCModule14 = _ESOCModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 14),
    _ESOCModule14_Type()
)
eSOCModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule14.setStatus("current")
_ESOCModule15_Type = DisplayString
_ESOCModule15_Object = MibScalar
eSOCModule15 = _ESOCModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 2, 15),
    _ESOCModule15_Type()
)
eSOCModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule15.setStatus("current")
_ESOHinfo_ObjectIdentity = ObjectIdentity
eSOHinfo = _ESOHinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3)
)
_ESOHModule1_Type = DisplayString
_ESOHModule1_Object = MibScalar
eSOHModule1 = _ESOHModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 1),
    _ESOHModule1_Type()
)
eSOHModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule1.setStatus("current")
_ESOHModule2_Type = DisplayString
_ESOHModule2_Object = MibScalar
eSOHModule2 = _ESOHModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 2),
    _ESOHModule2_Type()
)
eSOHModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule2.setStatus("current")
_ESOHModule3_Type = DisplayString
_ESOHModule3_Object = MibScalar
eSOHModule3 = _ESOHModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 3),
    _ESOHModule3_Type()
)
eSOHModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule3.setStatus("current")
_ESOHModule4_Type = DisplayString
_ESOHModule4_Object = MibScalar
eSOHModule4 = _ESOHModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 4),
    _ESOHModule4_Type()
)
eSOHModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule4.setStatus("current")
_ESOHModule5_Type = DisplayString
_ESOHModule5_Object = MibScalar
eSOHModule5 = _ESOHModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 5),
    _ESOHModule5_Type()
)
eSOHModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule5.setStatus("current")
_ESOHModule6_Type = DisplayString
_ESOHModule6_Object = MibScalar
eSOHModule6 = _ESOHModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 6),
    _ESOHModule6_Type()
)
eSOHModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule6.setStatus("current")
_ESOHModule7_Type = DisplayString
_ESOHModule7_Object = MibScalar
eSOHModule7 = _ESOHModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 7),
    _ESOHModule7_Type()
)
eSOHModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule7.setStatus("current")
_ESOHModule8_Type = DisplayString
_ESOHModule8_Object = MibScalar
eSOHModule8 = _ESOHModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 8),
    _ESOHModule8_Type()
)
eSOHModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule8.setStatus("current")
_ESOHModule9_Type = DisplayString
_ESOHModule9_Object = MibScalar
eSOHModule9 = _ESOHModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 9),
    _ESOHModule9_Type()
)
eSOHModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule9.setStatus("current")
_ESOHModule10_Type = DisplayString
_ESOHModule10_Object = MibScalar
eSOHModule10 = _ESOHModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 10),
    _ESOHModule10_Type()
)
eSOHModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule10.setStatus("current")
_ESOHModule11_Type = DisplayString
_ESOHModule11_Object = MibScalar
eSOHModule11 = _ESOHModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 11),
    _ESOHModule11_Type()
)
eSOHModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule11.setStatus("current")
_ESOHModule12_Type = DisplayString
_ESOHModule12_Object = MibScalar
eSOHModule12 = _ESOHModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 12),
    _ESOHModule12_Type()
)
eSOHModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule12.setStatus("current")
_ESOHModule13_Type = DisplayString
_ESOHModule13_Object = MibScalar
eSOHModule13 = _ESOHModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 13),
    _ESOHModule13_Type()
)
eSOHModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule13.setStatus("current")
_ESOHModule14_Type = DisplayString
_ESOHModule14_Object = MibScalar
eSOHModule14 = _ESOHModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 14),
    _ESOHModule14_Type()
)
eSOHModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule14.setStatus("current")
_ESOHModule15_Type = DisplayString
_ESOHModule15_Object = MibScalar
eSOHModule15 = _ESOHModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 3, 15),
    _ESOHModule15_Type()
)
eSOHModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule15.setStatus("current")
_EBattMaxCurrInfo_ObjectIdentity = ObjectIdentity
eBattMaxCurrInfo = _EBattMaxCurrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4)
)
_EBatteryMaxTempratureModule1_Type = DisplayString
_EBatteryMaxTempratureModule1_Object = MibScalar
eBatteryMaxTempratureModule1 = _EBatteryMaxTempratureModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 1),
    _EBatteryMaxTempratureModule1_Type()
)
eBatteryMaxTempratureModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule1.setStatus("current")
_EBatteryMaxTempratureModule2_Type = DisplayString
_EBatteryMaxTempratureModule2_Object = MibScalar
eBatteryMaxTempratureModule2 = _EBatteryMaxTempratureModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 2),
    _EBatteryMaxTempratureModule2_Type()
)
eBatteryMaxTempratureModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule2.setStatus("current")
_EBatteryMaxTempratureModule3_Type = DisplayString
_EBatteryMaxTempratureModule3_Object = MibScalar
eBatteryMaxTempratureModule3 = _EBatteryMaxTempratureModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 3),
    _EBatteryMaxTempratureModule3_Type()
)
eBatteryMaxTempratureModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule3.setStatus("current")
_EBatteryMaxTempratureModule4_Type = DisplayString
_EBatteryMaxTempratureModule4_Object = MibScalar
eBatteryMaxTempratureModule4 = _EBatteryMaxTempratureModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 4),
    _EBatteryMaxTempratureModule4_Type()
)
eBatteryMaxTempratureModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule4.setStatus("current")
_EBatteryMaxTempratureModule5_Type = DisplayString
_EBatteryMaxTempratureModule5_Object = MibScalar
eBatteryMaxTempratureModule5 = _EBatteryMaxTempratureModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 5),
    _EBatteryMaxTempratureModule5_Type()
)
eBatteryMaxTempratureModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule5.setStatus("current")
_EBatteryMaxTempratureModule6_Type = DisplayString
_EBatteryMaxTempratureModule6_Object = MibScalar
eBatteryMaxTempratureModule6 = _EBatteryMaxTempratureModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 6),
    _EBatteryMaxTempratureModule6_Type()
)
eBatteryMaxTempratureModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule6.setStatus("current")
_EBatteryMaxTempratureModule7_Type = DisplayString
_EBatteryMaxTempratureModule7_Object = MibScalar
eBatteryMaxTempratureModule7 = _EBatteryMaxTempratureModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 7),
    _EBatteryMaxTempratureModule7_Type()
)
eBatteryMaxTempratureModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule7.setStatus("current")
_EBatteryMaxTempratureModule8_Type = DisplayString
_EBatteryMaxTempratureModule8_Object = MibScalar
eBatteryMaxTempratureModule8 = _EBatteryMaxTempratureModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 8),
    _EBatteryMaxTempratureModule8_Type()
)
eBatteryMaxTempratureModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule8.setStatus("current")
_EBatteryMaxTempratureModule9_Type = DisplayString
_EBatteryMaxTempratureModule9_Object = MibScalar
eBatteryMaxTempratureModule9 = _EBatteryMaxTempratureModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 9),
    _EBatteryMaxTempratureModule9_Type()
)
eBatteryMaxTempratureModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule9.setStatus("current")
_EBatteryMaxTempratureModule10_Type = DisplayString
_EBatteryMaxTempratureModule10_Object = MibScalar
eBatteryMaxTempratureModule10 = _EBatteryMaxTempratureModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 10),
    _EBatteryMaxTempratureModule10_Type()
)
eBatteryMaxTempratureModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule10.setStatus("current")
_EBatteryMaxTempratureModule11_Type = DisplayString
_EBatteryMaxTempratureModule11_Object = MibScalar
eBatteryMaxTempratureModule11 = _EBatteryMaxTempratureModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 11),
    _EBatteryMaxTempratureModule11_Type()
)
eBatteryMaxTempratureModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule11.setStatus("current")
_EBatteryMaxTempratureModule12_Type = DisplayString
_EBatteryMaxTempratureModule12_Object = MibScalar
eBatteryMaxTempratureModule12 = _EBatteryMaxTempratureModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 12),
    _EBatteryMaxTempratureModule12_Type()
)
eBatteryMaxTempratureModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule12.setStatus("current")
_EBatteryMaxTempratureModule13_Type = DisplayString
_EBatteryMaxTempratureModule13_Object = MibScalar
eBatteryMaxTempratureModule13 = _EBatteryMaxTempratureModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 13),
    _EBatteryMaxTempratureModule13_Type()
)
eBatteryMaxTempratureModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule13.setStatus("current")
_EBatteryMaxTempratureModule14_Type = DisplayString
_EBatteryMaxTempratureModule14_Object = MibScalar
eBatteryMaxTempratureModule14 = _EBatteryMaxTempratureModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 14),
    _EBatteryMaxTempratureModule14_Type()
)
eBatteryMaxTempratureModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule14.setStatus("current")
_EBatteryMaxTempratureModule15_Type = DisplayString
_EBatteryMaxTempratureModule15_Object = MibScalar
eBatteryMaxTempratureModule15 = _EBatteryMaxTempratureModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 4, 15),
    _EBatteryMaxTempratureModule15_Type()
)
eBatteryMaxTempratureModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempratureModule15.setStatus("current")
_EVoltageInfo_ObjectIdentity = ObjectIdentity
eVoltageInfo = _EVoltageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5)
)
_EModuleVoltageModule1_Type = DisplayString
_EModuleVoltageModule1_Object = MibScalar
eModuleVoltageModule1 = _EModuleVoltageModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 1),
    _EModuleVoltageModule1_Type()
)
eModuleVoltageModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule1.setStatus("current")
_EModuleVoltageModule2_Type = DisplayString
_EModuleVoltageModule2_Object = MibScalar
eModuleVoltageModule2 = _EModuleVoltageModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 2),
    _EModuleVoltageModule2_Type()
)
eModuleVoltageModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule2.setStatus("current")
_EModuleVoltageModule3_Type = DisplayString
_EModuleVoltageModule3_Object = MibScalar
eModuleVoltageModule3 = _EModuleVoltageModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 3),
    _EModuleVoltageModule3_Type()
)
eModuleVoltageModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule3.setStatus("current")
_EModuleVoltageModule4_Type = DisplayString
_EModuleVoltageModule4_Object = MibScalar
eModuleVoltageModule4 = _EModuleVoltageModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 4),
    _EModuleVoltageModule4_Type()
)
eModuleVoltageModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule4.setStatus("current")
_EModuleVoltageModule5_Type = DisplayString
_EModuleVoltageModule5_Object = MibScalar
eModuleVoltageModule5 = _EModuleVoltageModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 5),
    _EModuleVoltageModule5_Type()
)
eModuleVoltageModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule5.setStatus("current")
_EModuleVoltageModule6_Type = DisplayString
_EModuleVoltageModule6_Object = MibScalar
eModuleVoltageModule6 = _EModuleVoltageModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 6),
    _EModuleVoltageModule6_Type()
)
eModuleVoltageModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule6.setStatus("current")
_EModuleVoltageModule7_Type = DisplayString
_EModuleVoltageModule7_Object = MibScalar
eModuleVoltageModule7 = _EModuleVoltageModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 7),
    _EModuleVoltageModule7_Type()
)
eModuleVoltageModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule7.setStatus("current")
_EModuleVoltageModule8_Type = DisplayString
_EModuleVoltageModule8_Object = MibScalar
eModuleVoltageModule8 = _EModuleVoltageModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 8),
    _EModuleVoltageModule8_Type()
)
eModuleVoltageModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule8.setStatus("current")
_EModuleVoltageModule9_Type = DisplayString
_EModuleVoltageModule9_Object = MibScalar
eModuleVoltageModule9 = _EModuleVoltageModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 9),
    _EModuleVoltageModule9_Type()
)
eModuleVoltageModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule9.setStatus("current")
_EModuleVoltageModule10_Type = DisplayString
_EModuleVoltageModule10_Object = MibScalar
eModuleVoltageModule10 = _EModuleVoltageModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 10),
    _EModuleVoltageModule10_Type()
)
eModuleVoltageModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule10.setStatus("current")
_EModuleVoltageModule11_Type = DisplayString
_EModuleVoltageModule11_Object = MibScalar
eModuleVoltageModule11 = _EModuleVoltageModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 11),
    _EModuleVoltageModule11_Type()
)
eModuleVoltageModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule11.setStatus("current")
_EModuleVoltageModule12_Type = DisplayString
_EModuleVoltageModule12_Object = MibScalar
eModuleVoltageModule12 = _EModuleVoltageModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 12),
    _EModuleVoltageModule12_Type()
)
eModuleVoltageModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule12.setStatus("current")
_EModuleVoltageModule13_Type = DisplayString
_EModuleVoltageModule13_Object = MibScalar
eModuleVoltageModule13 = _EModuleVoltageModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 13),
    _EModuleVoltageModule13_Type()
)
eModuleVoltageModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule13.setStatus("current")
_EModuleVoltageModule14_Type = DisplayString
_EModuleVoltageModule14_Object = MibScalar
eModuleVoltageModule14 = _EModuleVoltageModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 14),
    _EModuleVoltageModule14_Type()
)
eModuleVoltageModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule14.setStatus("current")
_EModuleVoltageModule15_Type = DisplayString
_EModuleVoltageModule15_Object = MibScalar
eModuleVoltageModule15 = _EModuleVoltageModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 5, 15),
    _EModuleVoltageModule15_Type()
)
eModuleVoltageModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule15.setStatus("current")
_ESystemInfo_ObjectIdentity = ObjectIdentity
eSystemInfo = _ESystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6)
)
_EManufacturerName_Type = DisplayString
_EManufacturerName_Object = MibScalar
eManufacturerName = _EManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6, 1),
    _EManufacturerName_Type()
)
eManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eManufacturerName.setStatus("current")
_EPartNo_Type = DisplayString
_EPartNo_Object = MibScalar
ePartNo = _EPartNo_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6, 2),
    _EPartNo_Type()
)
ePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePartNo.setStatus("current")
_ESrNo_Type = DisplayString
_ESrNo_Object = MibScalar
eSrNo = _ESrNo_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6, 3),
    _ESrNo_Type()
)
eSrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSrNo.setStatus("current")
_EDesignCapacity_Type = DisplayString
_EDesignCapacity_Object = MibScalar
eDesignCapacity = _EDesignCapacity_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6, 4),
    _EDesignCapacity_Type()
)
eDesignCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDesignCapacity.setStatus("current")
_ENumberOfInstalledModules_Type = DisplayString
_ENumberOfInstalledModules_Object = MibScalar
eNumberOfInstalledModules = _ENumberOfInstalledModules_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6, 5),
    _ENumberOfInstalledModules_Type()
)
eNumberOfInstalledModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNumberOfInstalledModules.setStatus("current")
_ENumberOfActiveModules_Type = DisplayString
_ENumberOfActiveModules_Object = MibScalar
eNumberOfActiveModules = _ENumberOfActiveModules_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 6, 6),
    _ENumberOfActiveModules_Type()
)
eNumberOfActiveModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNumberOfActiveModules.setStatus("current")
_EMaxChargeCurrInfo_ObjectIdentity = ObjectIdentity
eMaxChargeCurrInfo = _EMaxChargeCurrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 7)
)
_EModuleMaxChargeCurrentLimit_Type = DisplayString
_EModuleMaxChargeCurrentLimit_Object = MibScalar
eModuleMaxChargeCurrentLimit = _EModuleMaxChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 7, 1),
    _EModuleMaxChargeCurrentLimit_Type()
)
eModuleMaxChargeCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleMaxChargeCurrentLimit.setStatus("current")
_EInstMaxModuleCurrent_ObjectIdentity = ObjectIdentity
eInstMaxModuleCurrent = _EInstMaxModuleCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 8)
)
_EInstantaneousMaxModuleCurrent_Type = DisplayString
_EInstantaneousMaxModuleCurrent_Object = MibScalar
eInstantaneousMaxModuleCurrent = _EInstantaneousMaxModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 8, 1),
    _EInstantaneousMaxModuleCurrent_Type()
)
eInstantaneousMaxModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInstantaneousMaxModuleCurrent.setStatus("current")
_EMaxDischargeCurrInfo_ObjectIdentity = ObjectIdentity
eMaxDischargeCurrInfo = _EMaxDischargeCurrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 9)
)
_EMaxDischargeCurrentOfAModule_Type = DisplayString
_EMaxDischargeCurrentOfAModule_Object = MibScalar
eMaxDischargeCurrentOfAModule = _EMaxDischargeCurrentOfAModule_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 9, 1),
    _EMaxDischargeCurrentOfAModule_Type()
)
eMaxDischargeCurrentOfAModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMaxDischargeCurrentOfAModule.setStatus("current")
_EAHinfo_ObjectIdentity = ObjectIdentity
eAHinfo = _EAHinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 10)
)
_EREMAININGAHofTheBANK_Type = DisplayString
_EREMAININGAHofTheBANK_Object = MibScalar
eREMAININGAHofTheBANK = _EREMAININGAHofTheBANK_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 10, 1),
    _EREMAININGAHofTheBANK_Type()
)
eREMAININGAHofTheBANK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eREMAININGAHofTheBANK.setStatus("current")
_ECumulativeBatteryChargeAH_Type = DisplayString
_ECumulativeBatteryChargeAH_Object = MibScalar
eCumulativeBatteryChargeAH = _ECumulativeBatteryChargeAH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 10, 2),
    _ECumulativeBatteryChargeAH_Type()
)
eCumulativeBatteryChargeAH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCumulativeBatteryChargeAH.setStatus("current")
_EACEMch1Info_ObjectIdentity = ObjectIdentity
eACEMch1Info = _EACEMch1Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 11)
)
_EPowerKWMeter1_Type = DisplayString
_EPowerKWMeter1_Object = MibScalar
ePowerKWMeter1 = _EPowerKWMeter1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 11, 1),
    _EPowerKWMeter1_Type()
)
ePowerKWMeter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter1.setStatus("current")
_EEnergyKWHMeter1_Type = DisplayString
_EEnergyKWHMeter1_Object = MibScalar
eEnergyKWHMeter1 = _EEnergyKWHMeter1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 11, 2),
    _EEnergyKWHMeter1_Type()
)
eEnergyKWHMeter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter1.setStatus("current")
_EACEMch2Info_ObjectIdentity = ObjectIdentity
eACEMch2Info = _EACEMch2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 12)
)
_EPowerKWMeter2_Type = DisplayString
_EPowerKWMeter2_Object = MibScalar
ePowerKWMeter2 = _EPowerKWMeter2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 12, 1),
    _EPowerKWMeter2_Type()
)
ePowerKWMeter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter2.setStatus("current")
_EEnergyKWHMeter2_Type = DisplayString
_EEnergyKWHMeter2_Object = MibScalar
eEnergyKWHMeter2 = _EEnergyKWHMeter2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 12, 2),
    _EEnergyKWHMeter2_Type()
)
eEnergyKWHMeter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter2.setStatus("current")
_EACEMch3Info_ObjectIdentity = ObjectIdentity
eACEMch3Info = _EACEMch3Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 13)
)
_EPowerKWMeter3_Type = DisplayString
_EPowerKWMeter3_Object = MibScalar
ePowerKWMeter3 = _EPowerKWMeter3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 13, 1),
    _EPowerKWMeter3_Type()
)
ePowerKWMeter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter3.setStatus("current")
_EEnergyKWHMeter3_Type = DisplayString
_EEnergyKWHMeter3_Object = MibScalar
eEnergyKWHMeter3 = _EEnergyKWHMeter3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 13, 2),
    _EEnergyKWHMeter3_Type()
)
eEnergyKWHMeter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter3.setStatus("current")
_EACEMch4Info_ObjectIdentity = ObjectIdentity
eACEMch4Info = _EACEMch4Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 14)
)
_EPowerKWMeter4_Type = DisplayString
_EPowerKWMeter4_Object = MibScalar
ePowerKWMeter4 = _EPowerKWMeter4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 14, 1),
    _EPowerKWMeter4_Type()
)
ePowerKWMeter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter4.setStatus("current")
_EEnergyKWHMeter4_Type = DisplayString
_EEnergyKWHMeter4_Object = MibScalar
eEnergyKWHMeter4 = _EEnergyKWHMeter4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 14, 2),
    _EEnergyKWHMeter4_Type()
)
eEnergyKWHMeter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter4.setStatus("current")
_ESMPSinfo_ObjectIdentity = ObjectIdentity
eSMPSinfo = _ESMPSinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15)
)
_EDCVoltage_Type = DisplayString
_EDCVoltage_Object = MibScalar
eDCVoltage = _EDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 1),
    _EDCVoltage_Type()
)
eDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCVoltage.setStatus("current")
_EDCCurrent_Type = DisplayString
_EDCCurrent_Object = MibScalar
eDCCurrent = _EDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 2),
    _EDCCurrent_Type()
)
eDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCCurrent.setStatus("current")
_EDCKWH_Type = DisplayString
_EDCKWH_Object = MibScalar
eDCKWH = _EDCKWH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 3),
    _EDCKWH_Type()
)
eDCKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCKWH.setStatus("current")
_ELoadcurrent_Type = DisplayString
_ELoadcurrent_Object = MibScalar
eLoadcurrent = _ELoadcurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 4),
    _ELoadcurrent_Type()
)
eLoadcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadcurrent.setStatus("current")
_EBatteryCurrent_Type = DisplayString
_EBatteryCurrent_Object = MibScalar
eBatteryCurrent = _EBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 5),
    _EBatteryCurrent_Type()
)
eBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCurrent.setStatus("current")
_ENoOfRectifiersPoweredUp_Type = DisplayString
_ENoOfRectifiersPoweredUp_Object = MibScalar
eNoOfRectifiersPoweredUp = _ENoOfRectifiersPoweredUp_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 6),
    _ENoOfRectifiersPoweredUp_Type()
)
eNoOfRectifiersPoweredUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNoOfRectifiersPoweredUp.setStatus("current")
_ESMPSManufacturerName_Type = DisplayString
_ESMPSManufacturerName_Object = MibScalar
eSMPSManufacturerName = _ESMPSManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 7),
    _ESMPSManufacturerName_Type()
)
eSMPSManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMPSManufacturerName.setStatus("current")
_EControllerModel_Type = DisplayString
_EControllerModel_Object = MibScalar
eControllerModel = _EControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 8),
    _EControllerModel_Type()
)
eControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eControllerModel.setStatus("current")
_EFirmwareVersion_Type = DisplayString
_EFirmwareVersion_Object = MibScalar
eFirmwareVersion = _EFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 9),
    _EFirmwareVersion_Type()
)
eFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirmwareVersion.setStatus("current")
_ESMPSPartNo_Type = DisplayString
_ESMPSPartNo_Object = MibScalar
eSMPSPartNo = _ESMPSPartNo_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 10),
    _ESMPSPartNo_Type()
)
eSMPSPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMPSPartNo.setStatus("current")
_EInputLineAVoltage_Type = DisplayString
_EInputLineAVoltage_Object = MibScalar
eInputLineAVoltage = _EInputLineAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 11),
    _EInputLineAVoltage_Type()
)
eInputLineAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineAVoltage.setStatus("current")
_EInputLineBVoltage_Type = DisplayString
_EInputLineBVoltage_Object = MibScalar
eInputLineBVoltage = _EInputLineBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 12),
    _EInputLineBVoltage_Type()
)
eInputLineBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineBVoltage.setStatus("current")
_EInputLineCVoltage_Type = DisplayString
_EInputLineCVoltage_Object = MibScalar
eInputLineCVoltage = _EInputLineCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 13),
    _EInputLineCVoltage_Type()
)
eInputLineCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineCVoltage.setStatus("current")
_EInputLineACurrent_Type = DisplayString
_EInputLineACurrent_Object = MibScalar
eInputLineACurrent = _EInputLineACurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 14),
    _EInputLineACurrent_Type()
)
eInputLineACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineACurrent.setStatus("current")
_EInputLineBCurrent_Type = DisplayString
_EInputLineBCurrent_Object = MibScalar
eInputLineBCurrent = _EInputLineBCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 15),
    _EInputLineBCurrent_Type()
)
eInputLineBCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineBCurrent.setStatus("current")
_EInputLineCCurrent_Type = DisplayString
_EInputLineCCurrent_Object = MibScalar
eInputLineCCurrent = _EInputLineCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 16),
    _EInputLineCCurrent_Type()
)
eInputLineCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineCCurrent.setStatus("current")
_ETemperature1_Type = DisplayString
_ETemperature1_Object = MibScalar
eTemperature1 = _ETemperature1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 17),
    _ETemperature1_Type()
)
eTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperature1.setStatus("current")
_ETemperature2_Type = DisplayString
_ETemperature2_Object = MibScalar
eTemperature2 = _ETemperature2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 18),
    _ETemperature2_Type()
)
eTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperature2.setStatus("current")
_EMainsCumulativeKWh_Type = DisplayString
_EMainsCumulativeKWh_Object = MibScalar
eMainsCumulativeKWh = _EMainsCumulativeKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 19),
    _EMainsCumulativeKWh_Type()
)
eMainsCumulativeKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsCumulativeKWh.setStatus("current")
_EMainsCumulativeRunHrs_Type = DisplayString
_EMainsCumulativeRunHrs_Object = MibScalar
eMainsCumulativeRunHrs = _EMainsCumulativeRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 20),
    _EMainsCumulativeRunHrs_Type()
)
eMainsCumulativeRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsCumulativeRunHrs.setStatus("current")
_EBatteryCumulativeKWh_Type = DisplayString
_EBatteryCumulativeKWh_Object = MibScalar
eBatteryCumulativeKWh = _EBatteryCumulativeKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 21),
    _EBatteryCumulativeKWh_Type()
)
eBatteryCumulativeKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCumulativeKWh.setStatus("current")
_EBatteryCumulativeRunHrs_Type = DisplayString
_EBatteryCumulativeRunHrs_Object = MibScalar
eBatteryCumulativeRunHrs = _EBatteryCumulativeRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 22),
    _EBatteryCumulativeRunHrs_Type()
)
eBatteryCumulativeRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCumulativeRunHrs.setStatus("current")
_EBatteryDischargeCycle_Type = DisplayString
_EBatteryDischargeCycle_Object = MibScalar
eBatteryDischargeCycle = _EBatteryDischargeCycle_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 23),
    _EBatteryDischargeCycle_Type()
)
eBatteryDischargeCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryDischargeCycle.setStatus("current")
_EDCOutputPower_Type = DisplayString
_EDCOutputPower_Object = MibScalar
eDCOutputPower = _EDCOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 24),
    _EDCOutputPower_Type()
)
eDCOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCOutputPower.setStatus("current")
_ELoadCumulativeKWh_Type = DisplayString
_ELoadCumulativeKWh_Object = MibScalar
eLoadCumulativeKWh = _ELoadCumulativeKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 15, 25),
    _ELoadCumulativeKWh_Type()
)
eLoadCumulativeKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadCumulativeKWh.setStatus("current")
_ESettingInfo_ObjectIdentity = ObjectIdentity
eSettingInfo = _ESettingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16)
)
_EFloatVoltage_Type = DisplayString
_EFloatVoltage_Object = MibScalar
eFloatVoltage = _EFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 1),
    _EFloatVoltage_Type()
)
eFloatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFloatVoltage.setStatus("current")
_EBoostVoltage_Type = DisplayString
_EBoostVoltage_Object = MibScalar
eBoostVoltage = _EBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 2),
    _EBoostVoltage_Type()
)
eBoostVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBoostVoltage.setStatus("current")
_EChargeCurrentLimit_Type = DisplayString
_EChargeCurrentLimit_Object = MibScalar
eChargeCurrentLimit = _EChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 3),
    _EChargeCurrentLimit_Type()
)
eChargeCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargeCurrentLimit.setStatus("current")
_ELLVDVoltage_Type = DisplayString
_ELLVDVoltage_Object = MibScalar
eLLVDVoltage = _ELLVDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 4),
    _ELLVDVoltage_Type()
)
eLLVDVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLLVDVoltage.setStatus("current")
_EBLVDVoltage_Type = DisplayString
_EBLVDVoltage_Object = MibScalar
eBLVDVoltage = _EBLVDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 5),
    _EBLVDVoltage_Type()
)
eBLVDVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBLVDVoltage.setStatus("current")
_EAmbientHighTempThreshold_Type = DisplayString
_EAmbientHighTempThreshold_Object = MibScalar
eAmbientHighTempThreshold = _EAmbientHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 6),
    _EAmbientHighTempThreshold_Type()
)
eAmbientHighTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAmbientHighTempThreshold.setStatus("current")
_EOverloadAlarmThreshold_Type = DisplayString
_EOverloadAlarmThreshold_Object = MibScalar
eOverloadAlarmThreshold = _EOverloadAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 7),
    _EOverloadAlarmThreshold_Type()
)
eOverloadAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eOverloadAlarmThreshold.setStatus("current")
_EIPAddress_Type = DisplayString
_EIPAddress_Object = MibScalar
eIPAddress = _EIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 8),
    _EIPAddress_Type()
)
eIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eIPAddress.setStatus("current")
_ESAFTBatteryReset_Type = DisplayString
_ESAFTBatteryReset_Object = MibScalar
eSAFTBatteryReset = _ESAFTBatteryReset_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 16, 9),
    _ESAFTBatteryReset_Type()
)
eSAFTBatteryReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSAFTBatteryReset.setStatus("current")
_EDGinfo_ObjectIdentity = ObjectIdentity
eDGinfo = _EDGinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17)
)
_EDGLubeOilPressure_Type = DisplayString
_EDGLubeOilPressure_Object = MibScalar
eDGLubeOilPressure = _EDGLubeOilPressure_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 1),
    _EDGLubeOilPressure_Type()
)
eDGLubeOilPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGLubeOilPressure.setStatus("current")
_EChargingAlternatorVoltageDC_Type = DisplayString
_EChargingAlternatorVoltageDC_Object = MibScalar
eChargingAlternatorVoltageDC = _EChargingAlternatorVoltageDC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 2),
    _EChargingAlternatorVoltageDC_Type()
)
eChargingAlternatorVoltageDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingAlternatorVoltageDC.setStatus("current")
_EDGKWh_Type = DisplayString
_EDGKWh_Object = MibScalar
eDGKWh = _EDGKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 3),
    _EDGKWh_Type()
)
eDGKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGKWh.setStatus("current")
_ESEBKWh_Type = DisplayString
_ESEBKWh_Object = MibScalar
eSEBKWh = _ESEBKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 4),
    _ESEBKWh_Type()
)
eSEBKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSEBKWh.setStatus("current")
_EDGRunHrs_Type = DisplayString
_EDGRunHrs_Object = MibScalar
eDGRunHrs = _EDGRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 5),
    _EDGRunHrs_Type()
)
eDGRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGRunHrs.setStatus("current")
_EMainsRKw_Type = DisplayString
_EMainsRKw_Object = MibScalar
eMainsRKw = _EMainsRKw_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 6),
    _EMainsRKw_Type()
)
eMainsRKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsRKw.setStatus("current")
_EMainsYKw_Type = DisplayString
_EMainsYKw_Object = MibScalar
eMainsYKw = _EMainsYKw_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 7),
    _EMainsYKw_Type()
)
eMainsYKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsYKw.setStatus("current")
_EMainsBKw_Type = DisplayString
_EMainsBKw_Object = MibScalar
eMainsBKw = _EMainsBKw_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 8),
    _EMainsBKw_Type()
)
eMainsBKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsBKw.setStatus("current")
_EDGRKw_Type = DisplayString
_EDGRKw_Object = MibScalar
eDGRKw = _EDGRKw_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 9),
    _EDGRKw_Type()
)
eDGRKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGRKw.setStatus("current")
_EDGYKw_Type = DisplayString
_EDGYKw_Object = MibScalar
eDGYKw = _EDGYKw_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 10),
    _EDGYKw_Type()
)
eDGYKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGYKw.setStatus("current")
_EDGBKw_Type = DisplayString
_EDGBKw_Object = MibScalar
eDGBKw = _EDGBKw_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 11),
    _EDGBKw_Type()
)
eDGBKw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGBKw.setStatus("current")
_EDGFuelLevelLtr_Type = DisplayString
_EDGFuelLevelLtr_Object = MibScalar
eDGFuelLevelLtr = _EDGFuelLevelLtr_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 17, 12),
    _EDGFuelLevelLtr_Type()
)
eDGFuelLevelLtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGFuelLevelLtr.setStatus("current")
_EPACinfo_ObjectIdentity = ObjectIdentity
ePACinfo = _EPACinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 18)
)
_ESupplyAirTemperature_Type = DisplayString
_ESupplyAirTemperature_Object = MibScalar
eSupplyAirTemperature = _ESupplyAirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 18, 1),
    _ESupplyAirTemperature_Type()
)
eSupplyAirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSupplyAirTemperature.setStatus("current")
_EReturnAirTemperature_Type = DisplayString
_EReturnAirTemperature_Object = MibScalar
eReturnAirTemperature = _EReturnAirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 18, 2),
    _EReturnAirTemperature_Type()
)
eReturnAirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eReturnAirTemperature.setStatus("current")
_EReturnAirRelativeHumidity_Type = DisplayString
_EReturnAirRelativeHumidity_Object = MibScalar
eReturnAirRelativeHumidity = _EReturnAirRelativeHumidity_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 18, 3),
    _EReturnAirRelativeHumidity_Type()
)
eReturnAirRelativeHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eReturnAirRelativeHumidity.setStatus("current")
_ECHWControlValveOutput_Type = DisplayString
_ECHWControlValveOutput_Object = MibScalar
eCHWControlValveOutput = _ECHWControlValveOutput_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 18, 4),
    _ECHWControlValveOutput_Type()
)
eCHWControlValveOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCHWControlValveOutput.setStatus("current")
_EPACUnitRunHours_Type = DisplayString
_EPACUnitRunHours_Object = MibScalar
ePACUnitRunHours = _EPACUnitRunHours_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 18, 5),
    _EPACUnitRunHours_Type()
)
ePACUnitRunHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePACUnitRunHours.setStatus("current")
_ESpareDetails_ObjectIdentity = ObjectIdentity
eSpareDetails = _ESpareDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19)
)
_ESpareMeas1_Type = DisplayString
_ESpareMeas1_Object = MibScalar
eSpareMeas1 = _ESpareMeas1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 1),
    _ESpareMeas1_Type()
)
eSpareMeas1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas1.setStatus("current")
_ESpareMeas2_Type = DisplayString
_ESpareMeas2_Object = MibScalar
eSpareMeas2 = _ESpareMeas2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 2),
    _ESpareMeas2_Type()
)
eSpareMeas2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas2.setStatus("current")
_ESpareMeas3_Type = DisplayString
_ESpareMeas3_Object = MibScalar
eSpareMeas3 = _ESpareMeas3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 3),
    _ESpareMeas3_Type()
)
eSpareMeas3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas3.setStatus("current")
_ESpareMeas4_Type = DisplayString
_ESpareMeas4_Object = MibScalar
eSpareMeas4 = _ESpareMeas4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 4),
    _ESpareMeas4_Type()
)
eSpareMeas4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas4.setStatus("current")
_ESpareMeas5_Type = DisplayString
_ESpareMeas5_Object = MibScalar
eSpareMeas5 = _ESpareMeas5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 5),
    _ESpareMeas5_Type()
)
eSpareMeas5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas5.setStatus("current")
_ESpareMeas6_Type = DisplayString
_ESpareMeas6_Object = MibScalar
eSpareMeas6 = _ESpareMeas6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 6),
    _ESpareMeas6_Type()
)
eSpareMeas6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas6.setStatus("current")
_ESpareMeas7_Type = DisplayString
_ESpareMeas7_Object = MibScalar
eSpareMeas7 = _ESpareMeas7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 7),
    _ESpareMeas7_Type()
)
eSpareMeas7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas7.setStatus("current")
_ESpareMeas8_Type = DisplayString
_ESpareMeas8_Object = MibScalar
eSpareMeas8 = _ESpareMeas8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 8),
    _ESpareMeas8_Type()
)
eSpareMeas8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas8.setStatus("current")
_ESpareMeas9_Type = DisplayString
_ESpareMeas9_Object = MibScalar
eSpareMeas9 = _ESpareMeas9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 9),
    _ESpareMeas9_Type()
)
eSpareMeas9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas9.setStatus("current")
_ESpareMeas10_Type = DisplayString
_ESpareMeas10_Object = MibScalar
eSpareMeas10 = _ESpareMeas10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 19, 10),
    _ESpareMeas10_Type()
)
eSpareMeas10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareMeas10.setStatus("current")
_EInverterInfo_ObjectIdentity = ObjectIdentity
eInverterInfo = _EInverterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 20)
)
_EAcOutputVoltage_Type = DisplayString
_EAcOutputVoltage_Object = MibScalar
eAcOutputVoltage = _EAcOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 20, 1),
    _EAcOutputVoltage_Type()
)
eAcOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAcOutputVoltage.setStatus("current")
_EAcOutputCurrent_Type = DisplayString
_EAcOutputCurrent_Object = MibScalar
eAcOutputCurrent = _EAcOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 20, 2),
    _EAcOutputCurrent_Type()
)
eAcOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAcOutputCurrent.setStatus("current")
_EDcInputVoltage_Type = DisplayString
_EDcInputVoltage_Object = MibScalar
eDcInputVoltage = _EDcInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 20, 3),
    _EDcInputVoltage_Type()
)
eDcInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDcInputVoltage.setStatus("current")
_ETemperature_Type = DisplayString
_ETemperature_Object = MibScalar
eTemperature = _ETemperature_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 20, 4),
    _ETemperature_Type()
)
eTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperature.setStatus("current")
_EVRLAinfo_ObjectIdentity = ObjectIdentity
eVRLAinfo = _EVRLAinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21)
)
_EVRLAAHrating_Type = DisplayString
_EVRLAAHrating_Object = MibScalar
eVRLAAHrating = _EVRLAAHrating_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21, 1),
    _EVRLAAHrating_Type()
)
eVRLAAHrating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVRLAAHrating.setStatus("current")
_EVRLAFloatVoltage_Type = DisplayString
_EVRLAFloatVoltage_Object = MibScalar
eVRLAFloatVoltage = _EVRLAFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21, 2),
    _EVRLAFloatVoltage_Type()
)
eVRLAFloatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVRLAFloatVoltage.setStatus("current")
_EVRLABoostVoltage_Type = DisplayString
_EVRLABoostVoltage_Object = MibScalar
eVRLABoostVoltage = _EVRLABoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21, 3),
    _EVRLABoostVoltage_Type()
)
eVRLABoostVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVRLABoostVoltage.setStatus("current")
_EVRLAChargeCurrentLimit_Type = DisplayString
_EVRLAChargeCurrentLimit_Object = MibScalar
eVRLAChargeCurrentLimit = _EVRLAChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21, 4),
    _EVRLAChargeCurrentLimit_Type()
)
eVRLAChargeCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVRLAChargeCurrentLimit.setStatus("current")
_EVRLASOC_Type = DisplayString
_EVRLASOC_Object = MibScalar
eVRLASOC = _EVRLASOC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21, 5),
    _EVRLASOC_Type()
)
eVRLASOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVRLASOC.setStatus("current")


class _EModeSelectionStatus_Type(Integer32):
    """Custom type eModeSelectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lib", 0),
          ("vrla", 1))
    )


_EModeSelectionStatus_Type.__name__ = "Integer32"
_EModeSelectionStatus_Object = MibScalar
eModeSelectionStatus = _EModeSelectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 3, 2, 21, 6),
    _EModeSelectionStatus_Type()
)
eModeSelectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModeSelectionStatus.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11)
)
_Internaltraps_ObjectIdentity = ObjectIdentity
internaltraps = _Internaltraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1)
)
_Internalparams_ObjectIdentity = ObjectIdentity
internalparams = _Internalparams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 2)
)
_ESystemResetCause_Type = Integer32
_ESystemResetCause_Object = MibScalar
eSystemResetCause = _ESystemResetCause_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 2, 1),
    _ESystemResetCause_Type()
)
eSystemResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSystemResetCause.setStatus("current")
_EPeriodicTrap_Type = Integer32
_EPeriodicTrap_Object = MibScalar
ePeriodicTrap = _EPeriodicTrap_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 2, 2),
    _EPeriodicTrap_Type()
)
ePeriodicTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePeriodicTrap.setStatus("current")
_EGenericTrap_Type = Integer32
_EGenericTrap_Object = MibScalar
eGenericTrap = _EGenericTrap_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 2, 3),
    _EGenericTrap_Type()
)
eGenericTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGenericTrap.setStatus("current")
_Devicestatus_ObjectIdentity = ObjectIdentity
devicestatus = _Devicestatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 3)
)


class _ECommFailPCtoSMPS_Type(Integer32):
    """Custom type eCommFailPCtoSMPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("communicationOK", 0),
          ("noCommunication", 1))
    )


_ECommFailPCtoSMPS_Type.__name__ = "Integer32"
_ECommFailPCtoSMPS_Object = MibScalar
eCommFailPCtoSMPS = _ECommFailPCtoSMPS_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 3, 1),
    _ECommFailPCtoSMPS_Type()
)
eCommFailPCtoSMPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailPCtoSMPS.setStatus("current")


class _ECommFailACEM_Type(Integer32):
    """Custom type eCommFailACEM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("communicationOK", 0),
          ("noCommunication", 1))
    )


_ECommFailACEM_Type.__name__ = "Integer32"
_ECommFailACEM_Object = MibScalar
eCommFailACEM = _ECommFailACEM_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 3, 2),
    _ECommFailACEM_Type()
)
eCommFailACEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailACEM.setStatus("current")


class _ECommFailInverter_Type(Integer32):
    """Custom type eCommFailInverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("communicationOK", 0),
          ("noCommunication", 1))
    )


_ECommFailInverter_Type.__name__ = "Integer32"
_ECommFailInverter_Object = MibScalar
eCommFailInverter = _ECommFailInverter_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 3, 3),
    _ECommFailInverter_Type()
)
eCommFailInverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailInverter.setStatus("current")


class _ECommFailDGController_Type(Integer32):
    """Custom type eCommFailDGController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("communicationOK", 0),
          ("noCommunication", 1))
    )


_ECommFailDGController_Type.__name__ = "Integer32"
_ECommFailDGController_Object = MibScalar
eCommFailDGController = _ECommFailDGController_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 3, 4),
    _ECommFailDGController_Type()
)
eCommFailDGController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailDGController.setStatus("current")


class _ECommFailPAC_Type(Integer32):
    """Custom type eCommFailPAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("communicationOK", 0),
          ("noCommunication", 1))
    )


_ECommFailPAC_Type.__name__ = "Integer32"
_ECommFailPAC_Object = MibScalar
eCommFailPAC = _ECommFailPAC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 3, 5),
    _ECommFailPAC_Type()
)
eCommFailPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailPAC.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 12)
)


class _CTrapResendFlag_Type(Integer32):
    """Custom type cTrapResendFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CTrapResendFlag_Type.__name__ = "Integer32"
_CTrapResendFlag_Object = MibScalar
cTrapResendFlag = _CTrapResendFlag_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 12, 1),
    _CTrapResendFlag_Type()
)
cTrapResendFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTrapResendFlag.setStatus("current")

# Managed Objects groups


# Notification objects

tpCellOverVolProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 1)
)
tpCellOverVolProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod1.setStatus(
        "current"
    )

tpCellOverVolProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 2)
)
tpCellOverVolProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod2.setStatus(
        "current"
    )

tpCellOverVolProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 3)
)
tpCellOverVolProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod3.setStatus(
        "current"
    )

tpCellOverVolProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 4)
)
tpCellOverVolProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod4.setStatus(
        "current"
    )

tpCellOverVolProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 5)
)
tpCellOverVolProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod5.setStatus(
        "current"
    )

tpCellOverVolProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 6)
)
tpCellOverVolProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod6.setStatus(
        "current"
    )

tpCellOverVolProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 7)
)
tpCellOverVolProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellOverVolProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod7.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 8)
)
tpCellUnderVolProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod1.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 9)
)
tpCellUnderVolProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod2.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 10)
)
tpCellUnderVolProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod3.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 11)
)
tpCellUnderVolProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod4.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 12)
)
tpCellUnderVolProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod5.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 13)
)
tpCellUnderVolProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod6.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 14)
)
tpCellUnderVolProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellUnderVolProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod7.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 15)
)
tpModuleCellUnbalancedMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod1"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod1.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 16)
)
tpModuleCellUnbalancedMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod2"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod2.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 17)
)
tpModuleCellUnbalancedMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod3"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod3.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 18)
)
tpModuleCellUnbalancedMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod4"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod4.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 19)
)
tpModuleCellUnbalancedMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod5"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod5.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 20)
)
tpModuleCellUnbalancedMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod6"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod6.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 21)
)
tpModuleCellUnbalancedMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod7"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod7.setStatus(
        "current"
    )

tpBattUnderVolWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 22)
)
tpBattUnderVolWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod1.setStatus(
        "current"
    )

tpBattUnderVolWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 23)
)
tpBattUnderVolWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod2.setStatus(
        "current"
    )

tpBattUnderVolWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 24)
)
tpBattUnderVolWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod3.setStatus(
        "current"
    )

tpBattUnderVolWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 25)
)
tpBattUnderVolWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod4.setStatus(
        "current"
    )

tpBattUnderVolWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 26)
)
tpBattUnderVolWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod5.setStatus(
        "current"
    )

tpBattUnderVolWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 27)
)
tpBattUnderVolWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod6.setStatus(
        "current"
    )

tpBattUnderVolWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 28)
)
tpBattUnderVolWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod7.setStatus(
        "current"
    )

tpBattOverVolWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 29)
)
tpBattOverVolWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod1.setStatus(
        "current"
    )

tpBattOverVolWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 30)
)
tpBattOverVolWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod2.setStatus(
        "current"
    )

tpBattOverVolWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 31)
)
tpBattOverVolWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod3.setStatus(
        "current"
    )

tpBattOverVolWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 32)
)
tpBattOverVolWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod4.setStatus(
        "current"
    )

tpBattOverVolWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 33)
)
tpBattOverVolWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod5.setStatus(
        "current"
    )

tpBattOverVolWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 34)
)
tpBattOverVolWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod6.setStatus(
        "current"
    )

tpBattOverVolWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 35)
)
tpBattOverVolWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod7.setStatus(
        "current"
    )

tpCellChgOverTempProtMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 36)
)
tpCellChgOverTempProtMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod1"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod1.setStatus(
        "current"
    )

tpCellChgOverTempProtMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 37)
)
tpCellChgOverTempProtMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod2"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod2.setStatus(
        "current"
    )

tpCellChgOverTempProtMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 38)
)
tpCellChgOverTempProtMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod3"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod3.setStatus(
        "current"
    )

tpCellChgOverTempProtMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 39)
)
tpCellChgOverTempProtMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod4"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod4.setStatus(
        "current"
    )

tpCellChgOverTempProtMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 40)
)
tpCellChgOverTempProtMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod5"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod5.setStatus(
        "current"
    )

tpCellChgOverTempProtMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 41)
)
tpCellChgOverTempProtMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod6"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod6.setStatus(
        "current"
    )

tpCellChgOverTempProtMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 42)
)
tpCellChgOverTempProtMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod7"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod7.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 43)
)
tpCellDisChgOverTempProtMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod1"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod1.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 44)
)
tpCellDisChgOverTempProtMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod2"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod2.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 45)
)
tpCellDisChgOverTempProtMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod3"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod3.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 46)
)
tpCellDisChgOverTempProtMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod4"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod4.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 47)
)
tpCellDisChgOverTempProtMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod5"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod5.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 48)
)
tpCellDisChgOverTempProtMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod6"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod6.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 49)
)
tpCellDisChgOverTempProtMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod7"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod7.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 50)
)
tpAnyCellUnderTempProtMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod1"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod1.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 51)
)
tpAnyCellUnderTempProtMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod2"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod2.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 52)
)
tpAnyCellUnderTempProtMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod3"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod3.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 53)
)
tpAnyCellUnderTempProtMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod4"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod4.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 54)
)
tpAnyCellUnderTempProtMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod5"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod5.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 55)
)
tpAnyCellUnderTempProtMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod6"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod6.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 56)
)
tpAnyCellUnderTempProtMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod7"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod7.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 57)
)
tpBattChgOverCurrWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod1.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 58)
)
tpBattChgOverCurrWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod2.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 59)
)
tpBattChgOverCurrWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod3.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 60)
)
tpBattChgOverCurrWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod4.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 61)
)
tpBattChgOverCurrWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod5.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 62)
)
tpBattChgOverCurrWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod6.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 63)
)
tpBattChgOverCurrWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod7.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 64)
)
tpBattDisChgOverCurrWarnMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod1"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod1.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 65)
)
tpBattDisChgOverCurrWarnMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod2"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod2.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 66)
)
tpBattDisChgOverCurrWarnMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod3"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod3.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 67)
)
tpBattDisChgOverCurrWarnMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod4"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod4.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 68)
)
tpBattDisChgOverCurrWarnMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod5"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod5.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 69)
)
tpBattDisChgOverCurrWarnMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod6"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod6.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 70)
)
tpBattDisChgOverCurrWarnMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod7"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod7.setStatus(
        "current"
    )

tpBattLowSOCWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 71)
)
tpBattLowSOCWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod1.setStatus(
        "current"
    )

tpBattLowSOCWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 72)
)
tpBattLowSOCWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod2.setStatus(
        "current"
    )

tpBattLowSOCWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 73)
)
tpBattLowSOCWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod3.setStatus(
        "current"
    )

tpBattLowSOCWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 74)
)
tpBattLowSOCWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod4.setStatus(
        "current"
    )

tpBattLowSOCWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 75)
)
tpBattLowSOCWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod5.setStatus(
        "current"
    )

tpBattLowSOCWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 76)
)
tpBattLowSOCWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod6.setStatus(
        "current"
    )

tpBattLowSOCWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 77)
)
tpBattLowSOCWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod7.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 78)
)
tpBattOverCurrProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod1.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 79)
)
tpBattOverCurrProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod2.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 80)
)
tpBattOverCurrProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod3.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 81)
)
tpBattOverCurrProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod4.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 82)
)
tpBattOverCurrProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod5.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 83)
)
tpBattOverCurrProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod6.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 84)
)
tpBattOverCurrProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod7.setStatus(
        "current"
    )

tpBattOverVolProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 85)
)
tpBattOverVolProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod1.setStatus(
        "current"
    )

tpBattOverVolProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 86)
)
tpBattOverVolProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod2.setStatus(
        "current"
    )

tpBattOverVolProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 87)
)
tpBattOverVolProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod3.setStatus(
        "current"
    )

tpBattOverVolProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 88)
)
tpBattOverVolProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod4.setStatus(
        "current"
    )

tpBattOverVolProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 89)
)
tpBattOverVolProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod5.setStatus(
        "current"
    )

tpBattOverVolProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 90)
)
tpBattOverVolProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod6.setStatus(
        "current"
    )

tpBattOverVolProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 91)
)
tpBattOverVolProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod7.setStatus(
        "current"
    )

tpBattBankVolAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 92)
)
tpBattBankVolAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattBankVolAlarm"))
)
if mibBuilder.loadTexts:
    tpBattBankVolAlarm.setStatus(
        "current"
    )

tpBattUnderVolProtAnyModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 93)
)
tpBattUnderVolProtAnyModule.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolProtAnyModule"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolProtAnyModule.setStatus(
        "current"
    )

tpModule1Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 94)
)
tpModule1Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule1Isolated"))
)
if mibBuilder.loadTexts:
    tpModule1Isolated.setStatus(
        "current"
    )

tpModule2Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 95)
)
tpModule2Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule2Isolated"))
)
if mibBuilder.loadTexts:
    tpModule2Isolated.setStatus(
        "current"
    )

tpModule3Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 96)
)
tpModule3Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule3Isolated"))
)
if mibBuilder.loadTexts:
    tpModule3Isolated.setStatus(
        "current"
    )

tpModule4Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 97)
)
tpModule4Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule4Isolated"))
)
if mibBuilder.loadTexts:
    tpModule4Isolated.setStatus(
        "current"
    )

tpModule5Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 98)
)
tpModule5Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule5Isolated"))
)
if mibBuilder.loadTexts:
    tpModule5Isolated.setStatus(
        "current"
    )

tpModule6Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 99)
)
tpModule6Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule6Isolated"))
)
if mibBuilder.loadTexts:
    tpModule6Isolated.setStatus(
        "current"
    )

tpModule7Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 100)
)
tpModule7Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule7Isolated"))
)
if mibBuilder.loadTexts:
    tpModule7Isolated.setStatus(
        "current"
    )

tpBatteryBanklevel1lowVolAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 101)
)
tpBatteryBanklevel1lowVolAL.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBatteryBanklevel1lowVolAL"))
)
if mibBuilder.loadTexts:
    tpBatteryBanklevel1lowVolAL.setStatus(
        "current"
    )

tpBatteryBanklevel2lowVolAL = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 102)
)
tpBatteryBanklevel2lowVolAL.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBatteryBanklevel2lowVolAL"))
)
if mibBuilder.loadTexts:
    tpBatteryBanklevel2lowVolAL.setStatus(
        "current"
    )

tpBatteryBankhighTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 103)
)
tpBatteryBankhighTempAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBatteryBankhighTempAlarm"))
)
if mibBuilder.loadTexts:
    tpBatteryBankhighTempAlarm.setStatus(
        "current"
    )

tpBatteryBanklowTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 104)
)
tpBatteryBanklowTempAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBatteryBanklowTempAlarm"))
)
if mibBuilder.loadTexts:
    tpBatteryBanklowTempAlarm.setStatus(
        "current"
    )

tpAnymoduleCurrhighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 106)
)
tpAnymoduleCurrhighAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnymoduleCurrhighAlarm"))
)
if mibBuilder.loadTexts:
    tpAnymoduleCurrhighAlarm.setStatus(
        "current"
    )

tpSOCBelowLvl1ThresAlAnyMod = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 107)
)
tpSOCBelowLvl1ThresAlAnyMod.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eSOCBelowLvl1ThresAlAnyMod"))
)
if mibBuilder.loadTexts:
    tpSOCBelowLvl1ThresAlAnyMod.setStatus(
        "current"
    )

tpSystemfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 108)
)
tpSystemfail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eSystemfail"))
)
if mibBuilder.loadTexts:
    tpSystemfail.setStatus(
        "current"
    )

tpMasterCBMSControllerFailAl = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 109)
)
tpMasterCBMSControllerFailAl.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMasterCBMSControllerFailAl"))
)
if mibBuilder.loadTexts:
    tpMasterCBMSControllerFailAl.setStatus(
        "current"
    )

tpCellIsGoingOvTemp_1stLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 110)
)
tpCellIsGoingOvTemp_1stLevel.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellIsGoingOvTemp-1stLevel"))
)
if mibBuilder.loadTexts:
    tpCellIsGoingOvTemp_1stLevel.setStatus(
        "current"
    )

tpCellIsGoingOvChg1_stLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 111)
)
tpCellIsGoingOvChg1_stLevel.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellIsGoingOvChg1-stLevel"))
)
if mibBuilder.loadTexts:
    tpCellIsGoingOvChg1_stLevel.setStatus(
        "current"
    )

tpCellIsGoingOvChg2_ndLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 112)
)
tpCellIsGoingOvChg2_ndLevel.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellIsGoingOvChg2-ndLevel"))
)
if mibBuilder.loadTexts:
    tpCellIsGoingOvChg2_ndLevel.setStatus(
        "current"
    )

tpCellIsGoingunderVol = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 113)
)
tpCellIsGoingunderVol.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellIsGoingunderVol"))
)
if mibBuilder.loadTexts:
    tpCellIsGoingunderVol.setStatus(
        "current"
    )

tpLowSOC = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 114)
)
tpLowSOC.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eLowSOC"))
)
if mibBuilder.loadTexts:
    tpLowSOC.setStatus(
        "current"
    )

tpAmosfetisgoingoverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 115)
)
tpAmosfetisgoingoverTemp.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAmosfetisgoingoverTemp"))
)
if mibBuilder.loadTexts:
    tpAmosfetisgoingoverTemp.setStatus(
        "current"
    )

tpHeaterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 116)
)
tpHeaterFailure.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHeaterFailure"))
)
if mibBuilder.loadTexts:
    tpHeaterFailure.setStatus(
        "current"
    )

tpLowSOH = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 117)
)
tpLowSOH.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eLowSOH"))
)
if mibBuilder.loadTexts:
    tpLowSOH.setStatus(
        "current"
    )

tpUnbalancecell = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 118)
)
tpUnbalancecell.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eUnbalancecell"))
)
if mibBuilder.loadTexts:
    tpUnbalancecell.setStatus(
        "current"
    )

tpMosfetTempoutofRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 119)
)
tpMosfetTempoutofRange.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetTempoutofRange"))
)
if mibBuilder.loadTexts:
    tpMosfetTempoutofRange.setStatus(
        "current"
    )

tpEmergencyAlarmModule1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 120)
)
tpEmergencyAlarmModule1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule1"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule1.setStatus(
        "current"
    )

tpCellTempoutofRangeModule1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 121)
)
tpCellTempoutofRangeModule1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule1"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule1.setStatus(
        "current"
    )

tpHighBatterysupplyModule1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 122)
)
tpHighBatterysupplyModule1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule1"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule1.setStatus(
        "current"
    )

tpMosfetisoverTempModule1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 123)
)
tpMosfetisoverTempModule1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule1"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule1.setStatus(
        "current"
    )

tpAutotestFailureModule1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 124)
)
tpAutotestFailureModule1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule1"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule1.setStatus(
        "current"
    )

tpEmergencyAlarmModule2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 125)
)
tpEmergencyAlarmModule2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule2"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule2.setStatus(
        "current"
    )

tpCellTempoutofRangeModule2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 126)
)
tpCellTempoutofRangeModule2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule2"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule2.setStatus(
        "current"
    )

tpHighBatterysupplyModule2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 127)
)
tpHighBatterysupplyModule2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule2"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule2.setStatus(
        "current"
    )

tpMosfetisoverTempModule2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 128)
)
tpMosfetisoverTempModule2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule2"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule2.setStatus(
        "current"
    )

tpAutotestFailureModule2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 129)
)
tpAutotestFailureModule2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule2"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule2.setStatus(
        "current"
    )

tpEmergencyAlarmModule3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 130)
)
tpEmergencyAlarmModule3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule3"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule3.setStatus(
        "current"
    )

tpCellTempoutofRangeModule3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 131)
)
tpCellTempoutofRangeModule3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule3"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule3.setStatus(
        "current"
    )

tpHighBatterysupplyModule3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 132)
)
tpHighBatterysupplyModule3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule3"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule3.setStatus(
        "current"
    )

tpMosfetisoverTempModule3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 133)
)
tpMosfetisoverTempModule3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule3"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule3.setStatus(
        "current"
    )

tpAutotestFailureModule3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 134)
)
tpAutotestFailureModule3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule3"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule3.setStatus(
        "current"
    )

tpEmergencyAlarmModule4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 135)
)
tpEmergencyAlarmModule4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule4"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule4.setStatus(
        "current"
    )

tpCellTempoutofRangeModule4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 136)
)
tpCellTempoutofRangeModule4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule4"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule4.setStatus(
        "current"
    )

tpHighBatterysupplyModule4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 137)
)
tpHighBatterysupplyModule4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule4"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule4.setStatus(
        "current"
    )

tpMosfetisoverTempModule4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 138)
)
tpMosfetisoverTempModule4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule4"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule4.setStatus(
        "current"
    )

tpAutotestFailureModule4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 139)
)
tpAutotestFailureModule4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule4"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule4.setStatus(
        "current"
    )

tpEmergencyAlarmModule5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 140)
)
tpEmergencyAlarmModule5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule5"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule5.setStatus(
        "current"
    )

tpCellTempoutofRangeModule5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 141)
)
tpCellTempoutofRangeModule5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule5"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule5.setStatus(
        "current"
    )

tpHighBatterysupplyModule5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 142)
)
tpHighBatterysupplyModule5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule5"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule5.setStatus(
        "current"
    )

tpMosfetisoverTempModule5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 143)
)
tpMosfetisoverTempModule5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule5"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule5.setStatus(
        "current"
    )

tpAutotestFailureModule5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 144)
)
tpAutotestFailureModule5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule5"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule5.setStatus(
        "current"
    )

tpEmergencyAlarmModule6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 145)
)
tpEmergencyAlarmModule6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule6"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule6.setStatus(
        "current"
    )

tpCellTempoutofRangeModule6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 146)
)
tpCellTempoutofRangeModule6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule6"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule6.setStatus(
        "current"
    )

tpHighBatterysupplyModule6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 147)
)
tpHighBatterysupplyModule6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule6"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule6.setStatus(
        "current"
    )

tpMosfetisoverTempModule6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 148)
)
tpMosfetisoverTempModule6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule6"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule6.setStatus(
        "current"
    )

tpAutotestFailureModule6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 149)
)
tpAutotestFailureModule6.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule6"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule6.setStatus(
        "current"
    )

tpEmergencyAlarmModule7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 150)
)
tpEmergencyAlarmModule7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEmergencyAlarmModule7"))
)
if mibBuilder.loadTexts:
    tpEmergencyAlarmModule7.setStatus(
        "current"
    )

tpCellTempoutofRangeModule7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 151)
)
tpCellTempoutofRangeModule7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellTempoutofRangeModule7"))
)
if mibBuilder.loadTexts:
    tpCellTempoutofRangeModule7.setStatus(
        "current"
    )

tpHighBatterysupplyModule7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 152)
)
tpHighBatterysupplyModule7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eHighBatterysupplyModule7"))
)
if mibBuilder.loadTexts:
    tpHighBatterysupplyModule7.setStatus(
        "current"
    )

tpMosfetisoverTempModule7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 153)
)
tpMosfetisoverTempModule7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eMosfetisoverTempModule7"))
)
if mibBuilder.loadTexts:
    tpMosfetisoverTempModule7.setStatus(
        "current"
    )

tpAutotestFailureModule7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 154)
)
tpAutotestFailureModule7.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAutotestFailureModule7"))
)
if mibBuilder.loadTexts:
    tpAutotestFailureModule7.setStatus(
        "current"
    )

tpACPowerfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 155)
)
tpACPowerfail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eACPowerfail"))
)
if mibBuilder.loadTexts:
    tpACPowerfail.setStatus(
        "current"
    )

tpACDBIncomerTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 156)
)
tpACDBIncomerTrip.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eACDBIncomerTrip"))
)
if mibBuilder.loadTexts:
    tpACDBIncomerTrip.setStatus(
        "current"
    )

tpRectifierModule1Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 157)
)
tpRectifierModule1Fail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eRectifierModule1Fail"))
)
if mibBuilder.loadTexts:
    tpRectifierModule1Fail.setStatus(
        "current"
    )

tpRectifierModule2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 158)
)
tpRectifierModule2Fail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eRectifierModule2Fail"))
)
if mibBuilder.loadTexts:
    tpRectifierModule2Fail.setStatus(
        "current"
    )

tpRectifierModule3Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 159)
)
tpRectifierModule3Fail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eRectifierModule3Fail"))
)
if mibBuilder.loadTexts:
    tpRectifierModule3Fail.setStatus(
        "current"
    )

tpRectifierModule4Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 160)
)
tpRectifierModule4Fail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eRectifierModule4Fail"))
)
if mibBuilder.loadTexts:
    tpRectifierModule4Fail.setStatus(
        "current"
    )

tpLoadFusetrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 161)
)
tpLoadFusetrip.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eLoadFusetrip"))
)
if mibBuilder.loadTexts:
    tpLoadFusetrip.setStatus(
        "current"
    )

tpLLVDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 162)
)
tpLLVDAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eLLVDAlarm"))
)
if mibBuilder.loadTexts:
    tpLLVDAlarm.setStatus(
        "current"
    )

tpBLVDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 163)
)
tpBLVDAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBLVDAlarm"))
)
if mibBuilder.loadTexts:
    tpBLVDAlarm.setStatus(
        "current"
    )

tpBatteryfuseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 164)
)
tpBatteryfuseFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBatteryfuseFail"))
)
if mibBuilder.loadTexts:
    tpBatteryfuseFail.setStatus(
        "current"
    )

tpBatteryonLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 165)
)
tpBatteryonLoad.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBatteryonLoad"))
)
if mibBuilder.loadTexts:
    tpBatteryonLoad.setStatus(
        "current"
    )

tpTopDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 166)
)
tpTopDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eTopDoorOpen"))
)
if mibBuilder.loadTexts:
    tpTopDoorOpen.setStatus(
        "current"
    )

tpBottomDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 167)
)
tpBottomDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBottomDoorOpen"))
)
if mibBuilder.loadTexts:
    tpBottomDoorOpen.setStatus(
        "current"
    )

tpFireAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 168)
)
tpFireAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eFireAlarm"))
)
if mibBuilder.loadTexts:
    tpFireAlarm.setStatus(
        "current"
    )

tpShelterDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 169)
)
tpShelterDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eShelterDoorOpen"))
)
if mibBuilder.loadTexts:
    tpShelterDoorOpen.setStatus(
        "current"
    )

tpEquipmentDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 170)
)
tpEquipmentDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eEquipmentDoorOpen"))
)
if mibBuilder.loadTexts:
    tpEquipmentDoorOpen.setStatus(
        "current"
    )

tpDGFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 171)
)
tpDGFailToStart.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGFailToStart"))
)
if mibBuilder.loadTexts:
    tpDGFailToStart.setStatus(
        "current"
    )

tpDGCanopyTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 172)
)
tpDGCanopyTempHigh.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGCanopyTempHigh"))
)
if mibBuilder.loadTexts:
    tpDGCanopyTempHigh.setStatus(
        "current"
    )

tpDGLowFuelLevelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 173)
)
tpDGLowFuelLevelWarning.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGLowFuelLevelWarning"))
)
if mibBuilder.loadTexts:
    tpDGLowFuelLevelWarning.setStatus(
        "current"
    )

tpDGLowFuelLevelTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 174)
)
tpDGLowFuelLevelTrip.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGLowFuelLevelTrip"))
)
if mibBuilder.loadTexts:
    tpDGLowFuelLevelTrip.setStatus(
        "current"
    )

tpDGUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 175)
)
tpDGUnderFrequency.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGUnderFrequency"))
)
if mibBuilder.loadTexts:
    tpDGUnderFrequency.setStatus(
        "current"
    )

tpDGCommonFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 176)
)
tpDGCommonFault.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGCommonFault"))
)
if mibBuilder.loadTexts:
    tpDGCommonFault.setStatus(
        "current"
    )

tpDGOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 177)
)
tpDGOverload.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGOverload"))
)
if mibBuilder.loadTexts:
    tpDGOverload.setStatus(
        "current"
    )

tpLoadOnDG = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 178)
)
tpLoadOnDG.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eLoadOnDG"))
)
if mibBuilder.loadTexts:
    tpLoadOnDG.setStatus(
        "current"
    )

tpDGEngineOverSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 179)
)
tpDGEngineOverSpeed.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGEngineOverSpeed"))
)
if mibBuilder.loadTexts:
    tpDGEngineOverSpeed.setStatus(
        "current"
    )

tpDGIdleRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 180)
)
tpDGIdleRunning.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGIdleRunning"))
)
if mibBuilder.loadTexts:
    tpDGIdleRunning.setStatus(
        "current"
    )

tpDGInManual = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 181)
)
tpDGInManual.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGInManual"))
)
if mibBuilder.loadTexts:
    tpDGInManual.setStatus(
        "current"
    )

tpDGBatteryChargerFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 182)
)
tpDGBatteryChargerFaulty.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGBatteryChargerFaulty"))
)
if mibBuilder.loadTexts:
    tpDGBatteryChargerFaulty.setStatus(
        "current"
    )

tpDGCanopyDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 183)
)
tpDGCanopyDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGCanopyDoorOpen"))
)
if mibBuilder.loadTexts:
    tpDGCanopyDoorOpen.setStatus(
        "current"
    )

tpDGLLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 184)
)
tpDGLLOP.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGLLOP"))
)
if mibBuilder.loadTexts:
    tpDGLLOP.setStatus(
        "current"
    )

tpDGReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 185)
)
tpDGReserve.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDGReserve"))
)
if mibBuilder.loadTexts:
    tpDGReserve.setStatus(
        "current"
    )

tpShelterTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 186)
)
tpShelterTempHigh.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eShelterTempHigh"))
)
if mibBuilder.loadTexts:
    tpShelterTempHigh.setStatus(
        "current"
    )

tpPACFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 187)
)
tpPACFault.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "ePACFault"))
)
if mibBuilder.loadTexts:
    tpPACFault.setStatus(
        "current"
    )

tpPACRunStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 188)
)
tpPACRunStatus.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "ePACRunStatus"))
)
if mibBuilder.loadTexts:
    tpPACRunStatus.setStatus(
        "current"
    )

tpPACTripStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 189)
)
tpPACTripStatus.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "ePACTripStatus"))
)
if mibBuilder.loadTexts:
    tpPACTripStatus.setStatus(
        "current"
    )

tpDiffPressureFilterStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 190)
)
tpDiffPressureFilterStatus.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eDiffPressureFilterStatus"))
)
if mibBuilder.loadTexts:
    tpDiffPressureFilterStatus.setStatus(
        "current"
    )

tpCommFail_BMSToPC = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 191)
)
tpCommFail_BMSToPC.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCommFail-BMSToPC"))
)
if mibBuilder.loadTexts:
    tpCommFail_BMSToPC.setStatus(
        "current"
    )

tpAuxillaryEvent1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 194)
)
tpAuxillaryEvent1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAuxillaryEvent1"))
)
if mibBuilder.loadTexts:
    tpAuxillaryEvent1.setStatus(
        "current"
    )

tpAuxillaryEvent2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 195)
)
tpAuxillaryEvent2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAuxillaryEvent2"))
)
if mibBuilder.loadTexts:
    tpAuxillaryEvent2.setStatus(
        "current"
    )

tpAuxillaryEvent3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 196)
)
tpAuxillaryEvent3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAuxillaryEvent3"))
)
if mibBuilder.loadTexts:
    tpAuxillaryEvent3.setStatus(
        "current"
    )

tpAuxillaryEvent4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 197)
)
tpAuxillaryEvent4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAuxillaryEvent4"))
)
if mibBuilder.loadTexts:
    tpAuxillaryEvent4.setStatus(
        "current"
    )

tpAuxillaryEvent5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 198)
)
tpAuxillaryEvent5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAuxillaryEvent5"))
)
if mibBuilder.loadTexts:
    tpAuxillaryEvent5.setStatus(
        "current"
    )

tpInverterFail1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 199)
)
tpInverterFail1.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eInverterFail1"))
)
if mibBuilder.loadTexts:
    tpInverterFail1.setStatus(
        "current"
    )

tpInverterFail2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 200)
)
tpInverterFail2.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eInverterFail2"))
)
if mibBuilder.loadTexts:
    tpInverterFail2.setStatus(
        "current"
    )

tpSPARE3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 201)
)
tpSPARE3.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eSPARE3"))
)
if mibBuilder.loadTexts:
    tpSPARE3.setStatus(
        "current"
    )

tpSPARE4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 202)
)
tpSPARE4.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eSPARE4"))
)
if mibBuilder.loadTexts:
    tpSPARE4.setStatus(
        "current"
    )

tpSPARE5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 203)
)
tpSPARE5.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eSPARE5"))
)
if mibBuilder.loadTexts:
    tpSPARE5.setStatus(
        "current"
    )

tpModule1CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 204)
)
tpModule1CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule1CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule1CommFailAlarm.setStatus(
        "current"
    )

tpModule2CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 205)
)
tpModule2CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule2CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule2CommFailAlarm.setStatus(
        "current"
    )

tpModule3CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 206)
)
tpModule3CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule3CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule3CommFailAlarm.setStatus(
        "current"
    )

tpModule4CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 207)
)
tpModule4CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule4CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule4CommFailAlarm.setStatus(
        "current"
    )

tpModule5CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 208)
)
tpModule5CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule5CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule5CommFailAlarm.setStatus(
        "current"
    )

tpModule6CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 209)
)
tpModule6CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule6CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule6CommFailAlarm.setStatus(
        "current"
    )

tpModule7CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 210)
)
tpModule7CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule7CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule7CommFailAlarm.setStatus(
        "current"
    )

tpInverterOutputShort = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 211)
)
tpInverterOutputShort.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eInverterOutputShort"))
)
if mibBuilder.loadTexts:
    tpInverterOutputShort.setStatus(
        "current"
    )

tpInverterOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 212)
)
tpInverterOutputOverload.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eInverterOutputOverload"))
)
if mibBuilder.loadTexts:
    tpInverterOutputOverload.setStatus(
        "current"
    )

tpInverterCommonFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 213)
)
tpInverterCommonFault.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eInverterCommonFault"))
)
if mibBuilder.loadTexts:
    tpInverterCommonFault.setStatus(
        "current"
    )

tpAcInputVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 214)
)
tpAcInputVoltageLow.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAcInputVoltageLow"))
)
if mibBuilder.loadTexts:
    tpAcInputVoltageLow.setStatus(
        "current"
    )

tpAcInputVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 215)
)
tpAcInputVoltageHigh.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAcInputVoltageHigh"))
)
if mibBuilder.loadTexts:
    tpAcInputVoltageHigh.setStatus(
        "current"
    )

tpAcInputFreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 216)
)
tpAcInputFreqLow.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAcInputFreqLow"))
)
if mibBuilder.loadTexts:
    tpAcInputFreqLow.setStatus(
        "current"
    )

tpAcInputFreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 217)
)
tpAcInputFreqHigh.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAcInputFreqHigh"))
)
if mibBuilder.loadTexts:
    tpAcInputFreqHigh.setStatus(
        "current"
    )

tpBypassMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 218)
)
tpBypassMode.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBypassMode"))
)
if mibBuilder.loadTexts:
    tpBypassMode.setStatus(
        "current"
    )

tpFaultShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 219)
)
tpFaultShutDown.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eFaultShutDown"))
)
if mibBuilder.loadTexts:
    tpFaultShutDown.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 220)
)
tpModuleCellUnbalancedMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod8"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod8.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 221)
)
tpModuleCellUnbalancedMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod9"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod9.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 222)
)
tpModuleCellUnbalancedMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod10"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod10.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 223)
)
tpModuleCellUnbalancedMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod11"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod11.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 224)
)
tpModuleCellUnbalancedMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod12"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod12.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 225)
)
tpModuleCellUnbalancedMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod13"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod13.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 226)
)
tpModuleCellUnbalancedMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod14"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod14.setStatus(
        "current"
    )

tpModuleCellUnbalancedMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 227)
)
tpModuleCellUnbalancedMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModuleCellUnbalancedMod15"))
)
if mibBuilder.loadTexts:
    tpModuleCellUnbalancedMod15.setStatus(
        "current"
    )

tpBattUnderVolWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 228)
)
tpBattUnderVolWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod8.setStatus(
        "current"
    )

tpBattUnderVolWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 229)
)
tpBattUnderVolWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod9.setStatus(
        "current"
    )

tpBattUnderVolWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 230)
)
tpBattUnderVolWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod10.setStatus(
        "current"
    )

tpBattUnderVolWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 231)
)
tpBattUnderVolWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod11.setStatus(
        "current"
    )

tpBattUnderVolWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 232)
)
tpBattUnderVolWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod12.setStatus(
        "current"
    )

tpBattUnderVolWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 233)
)
tpBattUnderVolWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod13.setStatus(
        "current"
    )

tpBattUnderVolWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 234)
)
tpBattUnderVolWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod14.setStatus(
        "current"
    )

tpBattUnderVolWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 235)
)
tpBattUnderVolWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattUnderVolWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod15.setStatus(
        "current"
    )

tpBattOverVolWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 236)
)
tpBattOverVolWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod8.setStatus(
        "current"
    )

tpBattOverVolWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 237)
)
tpBattOverVolWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod9.setStatus(
        "current"
    )

tpBattOverVolWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 238)
)
tpBattOverVolWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod10.setStatus(
        "current"
    )

tpBattOverVolWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 239)
)
tpBattOverVolWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod11.setStatus(
        "current"
    )

tpBattOverVolWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 240)
)
tpBattOverVolWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod12.setStatus(
        "current"
    )

tpBattOverVolWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 241)
)
tpBattOverVolWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod13.setStatus(
        "current"
    )

tpBattOverVolWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 242)
)
tpBattOverVolWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod14.setStatus(
        "current"
    )

tpBattOverVolWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 243)
)
tpBattOverVolWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverVolWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod15.setStatus(
        "current"
    )

tpCellChgOverTempProtMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 244)
)
tpCellChgOverTempProtMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod8"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod8.setStatus(
        "current"
    )

tpCellChgOverTempProtMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 245)
)
tpCellChgOverTempProtMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod9"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod9.setStatus(
        "current"
    )

tpCellChgOverTempProtMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 246)
)
tpCellChgOverTempProtMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod10"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod10.setStatus(
        "current"
    )

tpCellChgOverTempProtMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 247)
)
tpCellChgOverTempProtMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod11"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod11.setStatus(
        "current"
    )

tpCellChgOverTempProtMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 248)
)
tpCellChgOverTempProtMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod12"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod12.setStatus(
        "current"
    )

tpCellChgOverTempProtMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 249)
)
tpCellChgOverTempProtMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod13"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod13.setStatus(
        "current"
    )

tpCellChgOverTempProtMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 250)
)
tpCellChgOverTempProtMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod14"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod14.setStatus(
        "current"
    )

tpCellChgOverTempProtMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 251)
)
tpCellChgOverTempProtMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellChgOverTempProtMod15"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod15.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 252)
)
tpCellDisChgOverTempProtMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod8"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod8.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 253)
)
tpCellDisChgOverTempProtMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod9"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod9.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 254)
)
tpCellDisChgOverTempProtMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod10"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod10.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 255)
)
tpCellDisChgOverTempProtMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod11"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod11.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 256)
)
tpCellDisChgOverTempProtMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod12"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod12.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 257)
)
tpCellDisChgOverTempProtMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod13"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod13.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 258)
)
tpCellDisChgOverTempProtMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod14"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod14.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 259)
)
tpCellDisChgOverTempProtMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCellDisChgOverTempProtMod15"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod15.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 260)
)
tpAnyCellUnderTempProtMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod8"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod8.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 261)
)
tpAnyCellUnderTempProtMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod9"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod9.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 262)
)
tpAnyCellUnderTempProtMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod10"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod10.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 263)
)
tpAnyCellUnderTempProtMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod11"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod11.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 264)
)
tpAnyCellUnderTempProtMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod12"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod12.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 265)
)
tpAnyCellUnderTempProtMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod13"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod13.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 266)
)
tpAnyCellUnderTempProtMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod14"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod14.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 267)
)
tpAnyCellUnderTempProtMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eAnyCellUnderTempProtMod15"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod15.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 268)
)
tpBattChgOverCurrWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod8.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 269)
)
tpBattChgOverCurrWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod9.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 270)
)
tpBattChgOverCurrWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod10.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 271)
)
tpBattChgOverCurrWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod11.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 272)
)
tpBattChgOverCurrWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod12.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 273)
)
tpBattChgOverCurrWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod13.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 274)
)
tpBattChgOverCurrWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod14.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 275)
)
tpBattChgOverCurrWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattChgOverCurrWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod15.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 276)
)
tpBattDisChgOverCurrWarnMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod8"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod8.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 277)
)
tpBattDisChgOverCurrWarnMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod9"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod9.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 278)
)
tpBattDisChgOverCurrWarnMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod10"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod10.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 279)
)
tpBattDisChgOverCurrWarnMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod11"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod11.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 280)
)
tpBattDisChgOverCurrWarnMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod12"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod12.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 281)
)
tpBattDisChgOverCurrWarnMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod13"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod13.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 282)
)
tpBattDisChgOverCurrWarnMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod14"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod14.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 283)
)
tpBattDisChgOverCurrWarnMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattDisChgOverCurrWarnMod15"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod15.setStatus(
        "current"
    )

tpBattLowSOCWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 284)
)
tpBattLowSOCWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod8.setStatus(
        "current"
    )

tpBattLowSOCWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 285)
)
tpBattLowSOCWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod9.setStatus(
        "current"
    )

tpBattLowSOCWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 286)
)
tpBattLowSOCWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod10.setStatus(
        "current"
    )

tpBattLowSOCWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 287)
)
tpBattLowSOCWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod11.setStatus(
        "current"
    )

tpBattLowSOCWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 288)
)
tpBattLowSOCWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod12.setStatus(
        "current"
    )

tpBattLowSOCWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 289)
)
tpBattLowSOCWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod13.setStatus(
        "current"
    )

tpBattLowSOCWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 290)
)
tpBattLowSOCWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod14.setStatus(
        "current"
    )

tpBattLowSOCWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 291)
)
tpBattLowSOCWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattLowSOCWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod15.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 292)
)
tpBattOverCurrProtectionMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod8"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod8.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 293)
)
tpBattOverCurrProtectionMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod9"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod9.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 294)
)
tpBattOverCurrProtectionMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod10"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod10.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 295)
)
tpBattOverCurrProtectionMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod11"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod11.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 296)
)
tpBattOverCurrProtectionMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod12"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod12.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 297)
)
tpBattOverCurrProtectionMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod13"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod13.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 298)
)
tpBattOverCurrProtectionMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod14"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod14.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 299)
)
tpBattOverCurrProtectionMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eBattOverCurrProtectionMod15"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod15.setStatus(
        "current"
    )

tpModule8Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 300)
)
tpModule8Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule8Isolated"))
)
if mibBuilder.loadTexts:
    tpModule8Isolated.setStatus(
        "current"
    )

tpModule9Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 301)
)
tpModule9Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule9Isolated"))
)
if mibBuilder.loadTexts:
    tpModule9Isolated.setStatus(
        "current"
    )

tpModule10Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 302)
)
tpModule10Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule10Isolated"))
)
if mibBuilder.loadTexts:
    tpModule10Isolated.setStatus(
        "current"
    )

tpModule11Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 303)
)
tpModule11Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule11Isolated"))
)
if mibBuilder.loadTexts:
    tpModule11Isolated.setStatus(
        "current"
    )

tpModule12Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 304)
)
tpModule12Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule12Isolated"))
)
if mibBuilder.loadTexts:
    tpModule12Isolated.setStatus(
        "current"
    )

tpModule13Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 305)
)
tpModule13Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule13Isolated"))
)
if mibBuilder.loadTexts:
    tpModule13Isolated.setStatus(
        "current"
    )

tpModule14Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 306)
)
tpModule14Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule14Isolated"))
)
if mibBuilder.loadTexts:
    tpModule14Isolated.setStatus(
        "current"
    )

tpModule15Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 307)
)
tpModule15Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule15Isolated"))
)
if mibBuilder.loadTexts:
    tpModule15Isolated.setStatus(
        "current"
    )

tpModule8CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 308)
)
tpModule8CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule8CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule8CommFailAlarm.setStatus(
        "current"
    )

tpModule9CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 309)
)
tpModule9CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule9CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule9CommFailAlarm.setStatus(
        "current"
    )

tpModule10CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 310)
)
tpModule10CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule10CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule10CommFailAlarm.setStatus(
        "current"
    )

tpModule11CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 311)
)
tpModule11CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule11CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule11CommFailAlarm.setStatus(
        "current"
    )

tpModule12CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 312)
)
tpModule12CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule12CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule12CommFailAlarm.setStatus(
        "current"
    )

tpModule13CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 313)
)
tpModule13CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule13CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule13CommFailAlarm.setStatus(
        "current"
    )

tpModule14CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 314)
)
tpModule14CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule14CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule14CommFailAlarm.setStatus(
        "current"
    )

tpModule15CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 10, 315)
)
tpModule15CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eModule15CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule15CommFailAlarm.setStatus(
        "current"
    )

tpSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 1)
)
tpSystemReset.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eSystemResetCause"))
)
if mibBuilder.loadTexts:
    tpSystemReset.setStatus(
        "current"
    )

tpPeriodicTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 3)
)
tpPeriodicTrap.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "ePeriodicTrap"))
)
if mibBuilder.loadTexts:
    tpPeriodicTrap.setStatus(
        "current"
    )

tpGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 5)
)
tpGenericTrap.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eGenericTrap"))
)
if mibBuilder.loadTexts:
    tpGenericTrap.setStatus(
        "current"
    )

tpCommFailPCtoSMPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 7)
)
tpCommFailPCtoSMPS.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCommFailPCtoSMPS"))
)
if mibBuilder.loadTexts:
    tpCommFailPCtoSMPS.setStatus(
        "current"
    )

tpCommFailACEM = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 8)
)
tpCommFailACEM.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCommFailACEM"))
)
if mibBuilder.loadTexts:
    tpCommFailACEM.setStatus(
        "current"
    )

tpCommFailInverter = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 9)
)
tpCommFailInverter.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCommFailInverter"))
)
if mibBuilder.loadTexts:
    tpCommFailInverter.setStatus(
        "current"
    )

tpCommFailDGController = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 10)
)
tpCommFailDGController.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCommFailDGController"))
)
if mibBuilder.loadTexts:
    tpCommFailDGController.setStatus(
        "current"
    )

tpCommFailPAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 1, 11, 1, 11)
)
tpCommFailPAC.setObjects(
      *(("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB", "eCommFailPAC"))
)
if mibBuilder.loadTexts:
    tpCommFailPAC.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELTAPOWERSOLUTIONS-GBMSMALLPICOCELLDGC-MIB",
    **{"DPSUsmAuthPrivProtocol": DPSUsmAuthPrivProtocol,
       "deltapowersolutions": deltapowersolutions,
       "products": products,
       "root": root,
       "setup": setup,
       "ipv4TrapTable": ipv4TrapTable,
       "ipv4TrapEntry": ipv4TrapEntry,
       "ipv4TrapReceiverNumber": ipv4TrapReceiverNumber,
       "ipv4TrapEnabled": ipv4TrapEnabled,
       "ipv4TrapReceiverIPAddress": ipv4TrapReceiverIPAddress,
       "ipv4TrapCommunity": ipv4TrapCommunity,
       "siteid": siteid,
       "ipv6TrapTable": ipv6TrapTable,
       "ipv6TrapEntry": ipv6TrapEntry,
       "ipv6TrapReceiverNumber": ipv6TrapReceiverNumber,
       "ipv6TrapEnabled": ipv6TrapEnabled,
       "ipv6TrapReceiverIPv6Address": ipv6TrapReceiverIPv6Address,
       "ipv6TrapCommunity": ipv6TrapCommunity,
       "monitoring": monitoring,
       "eAlarms": eAlarms,
       "eAlarmsGp": eAlarmsGp,
       "eCellOverVolProtectionMod1": eCellOverVolProtectionMod1,
       "eCellOverVolProtectionMod2": eCellOverVolProtectionMod2,
       "eCellOverVolProtectionMod3": eCellOverVolProtectionMod3,
       "eCellOverVolProtectionMod4": eCellOverVolProtectionMod4,
       "eCellOverVolProtectionMod5": eCellOverVolProtectionMod5,
       "eCellOverVolProtectionMod6": eCellOverVolProtectionMod6,
       "eCellOverVolProtectionMod7": eCellOverVolProtectionMod7,
       "eCellUnderVolProtectionMod1": eCellUnderVolProtectionMod1,
       "eCellUnderVolProtectionMod2": eCellUnderVolProtectionMod2,
       "eCellUnderVolProtectionMod3": eCellUnderVolProtectionMod3,
       "eCellUnderVolProtectionMod4": eCellUnderVolProtectionMod4,
       "eCellUnderVolProtectionMod5": eCellUnderVolProtectionMod5,
       "eCellUnderVolProtectionMod6": eCellUnderVolProtectionMod6,
       "eCellUnderVolProtectionMod7": eCellUnderVolProtectionMod7,
       "eModuleCellUnbalancedMod1": eModuleCellUnbalancedMod1,
       "eModuleCellUnbalancedMod2": eModuleCellUnbalancedMod2,
       "eModuleCellUnbalancedMod3": eModuleCellUnbalancedMod3,
       "eModuleCellUnbalancedMod4": eModuleCellUnbalancedMod4,
       "eModuleCellUnbalancedMod5": eModuleCellUnbalancedMod5,
       "eModuleCellUnbalancedMod6": eModuleCellUnbalancedMod6,
       "eModuleCellUnbalancedMod7": eModuleCellUnbalancedMod7,
       "eBattUnderVolWarningMod1": eBattUnderVolWarningMod1,
       "eBattUnderVolWarningMod2": eBattUnderVolWarningMod2,
       "eBattUnderVolWarningMod3": eBattUnderVolWarningMod3,
       "eBattUnderVolWarningMod4": eBattUnderVolWarningMod4,
       "eBattUnderVolWarningMod5": eBattUnderVolWarningMod5,
       "eBattUnderVolWarningMod6": eBattUnderVolWarningMod6,
       "eBattUnderVolWarningMod7": eBattUnderVolWarningMod7,
       "eBattOverVolWarningMod1": eBattOverVolWarningMod1,
       "eBattOverVolWarningMod2": eBattOverVolWarningMod2,
       "eBattOverVolWarningMod3": eBattOverVolWarningMod3,
       "eBattOverVolWarningMod4": eBattOverVolWarningMod4,
       "eBattOverVolWarningMod5": eBattOverVolWarningMod5,
       "eBattOverVolWarningMod6": eBattOverVolWarningMod6,
       "eBattOverVolWarningMod7": eBattOverVolWarningMod7,
       "eCellChgOverTempProtMod1": eCellChgOverTempProtMod1,
       "eCellChgOverTempProtMod2": eCellChgOverTempProtMod2,
       "eCellChgOverTempProtMod3": eCellChgOverTempProtMod3,
       "eCellChgOverTempProtMod4": eCellChgOverTempProtMod4,
       "eCellChgOverTempProtMod5": eCellChgOverTempProtMod5,
       "eCellChgOverTempProtMod6": eCellChgOverTempProtMod6,
       "eCellChgOverTempProtMod7": eCellChgOverTempProtMod7,
       "eCellDisChgOverTempProtMod1": eCellDisChgOverTempProtMod1,
       "eCellDisChgOverTempProtMod2": eCellDisChgOverTempProtMod2,
       "eCellDisChgOverTempProtMod3": eCellDisChgOverTempProtMod3,
       "eCellDisChgOverTempProtMod4": eCellDisChgOverTempProtMod4,
       "eCellDisChgOverTempProtMod5": eCellDisChgOverTempProtMod5,
       "eCellDisChgOverTempProtMod6": eCellDisChgOverTempProtMod6,
       "eCellDisChgOverTempProtMod7": eCellDisChgOverTempProtMod7,
       "eAnyCellUnderTempProtMod1": eAnyCellUnderTempProtMod1,
       "eAnyCellUnderTempProtMod2": eAnyCellUnderTempProtMod2,
       "eAnyCellUnderTempProtMod3": eAnyCellUnderTempProtMod3,
       "eAnyCellUnderTempProtMod4": eAnyCellUnderTempProtMod4,
       "eAnyCellUnderTempProtMod5": eAnyCellUnderTempProtMod5,
       "eAnyCellUnderTempProtMod6": eAnyCellUnderTempProtMod6,
       "eAnyCellUnderTempProtMod7": eAnyCellUnderTempProtMod7,
       "eBattChgOverCurrWarningMod1": eBattChgOverCurrWarningMod1,
       "eBattChgOverCurrWarningMod2": eBattChgOverCurrWarningMod2,
       "eBattChgOverCurrWarningMod3": eBattChgOverCurrWarningMod3,
       "eBattChgOverCurrWarningMod4": eBattChgOverCurrWarningMod4,
       "eBattChgOverCurrWarningMod5": eBattChgOverCurrWarningMod5,
       "eBattChgOverCurrWarningMod6": eBattChgOverCurrWarningMod6,
       "eBattChgOverCurrWarningMod7": eBattChgOverCurrWarningMod7,
       "eBattDisChgOverCurrWarnMod1": eBattDisChgOverCurrWarnMod1,
       "eBattDisChgOverCurrWarnMod2": eBattDisChgOverCurrWarnMod2,
       "eBattDisChgOverCurrWarnMod3": eBattDisChgOverCurrWarnMod3,
       "eBattDisChgOverCurrWarnMod4": eBattDisChgOverCurrWarnMod4,
       "eBattDisChgOverCurrWarnMod5": eBattDisChgOverCurrWarnMod5,
       "eBattDisChgOverCurrWarnMod6": eBattDisChgOverCurrWarnMod6,
       "eBattDisChgOverCurrWarnMod7": eBattDisChgOverCurrWarnMod7,
       "eBattLowSOCWarningMod1": eBattLowSOCWarningMod1,
       "eBattLowSOCWarningMod2": eBattLowSOCWarningMod2,
       "eBattLowSOCWarningMod3": eBattLowSOCWarningMod3,
       "eBattLowSOCWarningMod4": eBattLowSOCWarningMod4,
       "eBattLowSOCWarningMod5": eBattLowSOCWarningMod5,
       "eBattLowSOCWarningMod6": eBattLowSOCWarningMod6,
       "eBattLowSOCWarningMod7": eBattLowSOCWarningMod7,
       "eBattOverCurrProtectionMod1": eBattOverCurrProtectionMod1,
       "eBattOverCurrProtectionMod2": eBattOverCurrProtectionMod2,
       "eBattOverCurrProtectionMod3": eBattOverCurrProtectionMod3,
       "eBattOverCurrProtectionMod4": eBattOverCurrProtectionMod4,
       "eBattOverCurrProtectionMod5": eBattOverCurrProtectionMod5,
       "eBattOverCurrProtectionMod6": eBattOverCurrProtectionMod6,
       "eBattOverCurrProtectionMod7": eBattOverCurrProtectionMod7,
       "eBattOverVolProtectionMod1": eBattOverVolProtectionMod1,
       "eBattOverVolProtectionMod2": eBattOverVolProtectionMod2,
       "eBattOverVolProtectionMod3": eBattOverVolProtectionMod3,
       "eBattOverVolProtectionMod4": eBattOverVolProtectionMod4,
       "eBattOverVolProtectionMod5": eBattOverVolProtectionMod5,
       "eBattOverVolProtectionMod6": eBattOverVolProtectionMod6,
       "eBattOverVolProtectionMod7": eBattOverVolProtectionMod7,
       "eBattBankVolAlarm": eBattBankVolAlarm,
       "eBattUnderVolProtAnyModule": eBattUnderVolProtAnyModule,
       "eModule1Isolated": eModule1Isolated,
       "eModule2Isolated": eModule2Isolated,
       "eModule3Isolated": eModule3Isolated,
       "eModule4Isolated": eModule4Isolated,
       "eModule5Isolated": eModule5Isolated,
       "eModule6Isolated": eModule6Isolated,
       "eModule7Isolated": eModule7Isolated,
       "eBatteryBanklevel1lowVolAL": eBatteryBanklevel1lowVolAL,
       "eBatteryBanklevel2lowVolAL": eBatteryBanklevel2lowVolAL,
       "eBatteryBankhighTempAlarm": eBatteryBankhighTempAlarm,
       "eBatteryBanklowTempAlarm": eBatteryBanklowTempAlarm,
       "eAnymoduleCurrhighAlarm": eAnymoduleCurrhighAlarm,
       "eSOCBelowLvl1ThresAlAnyMod": eSOCBelowLvl1ThresAlAnyMod,
       "eSystemfail": eSystemfail,
       "eMasterCBMSControllerFailAl": eMasterCBMSControllerFailAl,
       "eCellIsGoingOvTemp-1stLevel": eCellIsGoingOvTemp_1stLevel,
       "eCellIsGoingOvChg1-stLevel": eCellIsGoingOvChg1_stLevel,
       "eCellIsGoingOvChg2-ndLevel": eCellIsGoingOvChg2_ndLevel,
       "eCellIsGoingunderVol": eCellIsGoingunderVol,
       "eLowSOC": eLowSOC,
       "eAmosfetisgoingoverTemp": eAmosfetisgoingoverTemp,
       "eHeaterFailure": eHeaterFailure,
       "eLowSOH": eLowSOH,
       "eUnbalancecell": eUnbalancecell,
       "eMosfetTempoutofRange": eMosfetTempoutofRange,
       "eEmergencyAlarmModule1": eEmergencyAlarmModule1,
       "eCellTempoutofRangeModule1": eCellTempoutofRangeModule1,
       "eHighBatterysupplyModule1": eHighBatterysupplyModule1,
       "eMosfetisoverTempModule1": eMosfetisoverTempModule1,
       "eAutotestFailureModule1": eAutotestFailureModule1,
       "eEmergencyAlarmModule2": eEmergencyAlarmModule2,
       "eCellTempoutofRangeModule2": eCellTempoutofRangeModule2,
       "eHighBatterysupplyModule2": eHighBatterysupplyModule2,
       "eMosfetisoverTempModule2": eMosfetisoverTempModule2,
       "eAutotestFailureModule2": eAutotestFailureModule2,
       "eEmergencyAlarmModule3": eEmergencyAlarmModule3,
       "eCellTempoutofRangeModule3": eCellTempoutofRangeModule3,
       "eHighBatterysupplyModule3": eHighBatterysupplyModule3,
       "eMosfetisoverTempModule3": eMosfetisoverTempModule3,
       "eAutotestFailureModule3": eAutotestFailureModule3,
       "eEmergencyAlarmModule4": eEmergencyAlarmModule4,
       "eCellTempoutofRangeModule4": eCellTempoutofRangeModule4,
       "eHighBatterysupplyModule4": eHighBatterysupplyModule4,
       "eMosfetisoverTempModule4": eMosfetisoverTempModule4,
       "eAutotestFailureModule4": eAutotestFailureModule4,
       "eEmergencyAlarmModule5": eEmergencyAlarmModule5,
       "eCellTempoutofRangeModule5": eCellTempoutofRangeModule5,
       "eHighBatterysupplyModule5": eHighBatterysupplyModule5,
       "eMosfetisoverTempModule5": eMosfetisoverTempModule5,
       "eAutotestFailureModule5": eAutotestFailureModule5,
       "eEmergencyAlarmModule6": eEmergencyAlarmModule6,
       "eCellTempoutofRangeModule6": eCellTempoutofRangeModule6,
       "eHighBatterysupplyModule6": eHighBatterysupplyModule6,
       "eMosfetisoverTempModule6": eMosfetisoverTempModule6,
       "eAutotestFailureModule6": eAutotestFailureModule6,
       "eEmergencyAlarmModule7": eEmergencyAlarmModule7,
       "eCellTempoutofRangeModule7": eCellTempoutofRangeModule7,
       "eHighBatterysupplyModule7": eHighBatterysupplyModule7,
       "eMosfetisoverTempModule7": eMosfetisoverTempModule7,
       "eAutotestFailureModule7": eAutotestFailureModule7,
       "eACPowerfail": eACPowerfail,
       "eACDBIncomerTrip": eACDBIncomerTrip,
       "eRectifierModule1Fail": eRectifierModule1Fail,
       "eRectifierModule2Fail": eRectifierModule2Fail,
       "eRectifierModule3Fail": eRectifierModule3Fail,
       "eRectifierModule4Fail": eRectifierModule4Fail,
       "eLoadFusetrip": eLoadFusetrip,
       "eLLVDAlarm": eLLVDAlarm,
       "eBLVDAlarm": eBLVDAlarm,
       "eBatteryfuseFail": eBatteryfuseFail,
       "eBatteryonLoad": eBatteryonLoad,
       "eTopDoorOpen": eTopDoorOpen,
       "eBottomDoorOpen": eBottomDoorOpen,
       "eFireAlarm": eFireAlarm,
       "eShelterDoorOpen": eShelterDoorOpen,
       "eEquipmentDoorOpen": eEquipmentDoorOpen,
       "eDGFailToStart": eDGFailToStart,
       "eDGCanopyTempHigh": eDGCanopyTempHigh,
       "eDGLowFuelLevelWarning": eDGLowFuelLevelWarning,
       "eDGLowFuelLevelTrip": eDGLowFuelLevelTrip,
       "eDGUnderFrequency": eDGUnderFrequency,
       "eDGCommonFault": eDGCommonFault,
       "eDGOverload": eDGOverload,
       "eLoadOnDG": eLoadOnDG,
       "eDGEngineOverSpeed": eDGEngineOverSpeed,
       "eDGIdleRunning": eDGIdleRunning,
       "eDGInManual": eDGInManual,
       "eDGBatteryChargerFaulty": eDGBatteryChargerFaulty,
       "eDGCanopyDoorOpen": eDGCanopyDoorOpen,
       "eDGLLOP": eDGLLOP,
       "eDGReserve": eDGReserve,
       "eShelterTempHigh": eShelterTempHigh,
       "ePACFault": ePACFault,
       "ePACRunStatus": ePACRunStatus,
       "ePACTripStatus": ePACTripStatus,
       "eDiffPressureFilterStatus": eDiffPressureFilterStatus,
       "eCommFail-BMSToPC": eCommFail_BMSToPC,
       "eAuxillaryEvent1": eAuxillaryEvent1,
       "eAuxillaryEvent2": eAuxillaryEvent2,
       "eAuxillaryEvent3": eAuxillaryEvent3,
       "eAuxillaryEvent4": eAuxillaryEvent4,
       "eAuxillaryEvent5": eAuxillaryEvent5,
       "eInverterFail1": eInverterFail1,
       "eInverterFail2": eInverterFail2,
       "eSPARE3": eSPARE3,
       "eSPARE4": eSPARE4,
       "eSPARE5": eSPARE5,
       "eModule1CommFailAlarm": eModule1CommFailAlarm,
       "eModule2CommFailAlarm": eModule2CommFailAlarm,
       "eModule3CommFailAlarm": eModule3CommFailAlarm,
       "eModule4CommFailAlarm": eModule4CommFailAlarm,
       "eModule5CommFailAlarm": eModule5CommFailAlarm,
       "eModule6CommFailAlarm": eModule6CommFailAlarm,
       "eModule7CommFailAlarm": eModule7CommFailAlarm,
       "eInverterOutputShort": eInverterOutputShort,
       "eInverterOutputOverload": eInverterOutputOverload,
       "eInverterCommonFault": eInverterCommonFault,
       "eAcInputVoltageLow": eAcInputVoltageLow,
       "eAcInputVoltageHigh": eAcInputVoltageHigh,
       "eAcInputFreqLow": eAcInputFreqLow,
       "eAcInputFreqHigh": eAcInputFreqHigh,
       "eBypassMode": eBypassMode,
       "eFaultShutDown": eFaultShutDown,
       "eModuleCellUnbalancedMod8": eModuleCellUnbalancedMod8,
       "eModuleCellUnbalancedMod9": eModuleCellUnbalancedMod9,
       "eModuleCellUnbalancedMod10": eModuleCellUnbalancedMod10,
       "eModuleCellUnbalancedMod11": eModuleCellUnbalancedMod11,
       "eModuleCellUnbalancedMod12": eModuleCellUnbalancedMod12,
       "eModuleCellUnbalancedMod13": eModuleCellUnbalancedMod13,
       "eModuleCellUnbalancedMod14": eModuleCellUnbalancedMod14,
       "eModuleCellUnbalancedMod15": eModuleCellUnbalancedMod15,
       "eBattUnderVolWarningMod8": eBattUnderVolWarningMod8,
       "eBattUnderVolWarningMod9": eBattUnderVolWarningMod9,
       "eBattUnderVolWarningMod10": eBattUnderVolWarningMod10,
       "eBattUnderVolWarningMod11": eBattUnderVolWarningMod11,
       "eBattUnderVolWarningMod12": eBattUnderVolWarningMod12,
       "eBattUnderVolWarningMod13": eBattUnderVolWarningMod13,
       "eBattUnderVolWarningMod14": eBattUnderVolWarningMod14,
       "eBattUnderVolWarningMod15": eBattUnderVolWarningMod15,
       "eBattOverVolWarningMod8": eBattOverVolWarningMod8,
       "eBattOverVolWarningMod9": eBattOverVolWarningMod9,
       "eBattOverVolWarningMod10": eBattOverVolWarningMod10,
       "eBattOverVolWarningMod11": eBattOverVolWarningMod11,
       "eBattOverVolWarningMod12": eBattOverVolWarningMod12,
       "eBattOverVolWarningMod13": eBattOverVolWarningMod13,
       "eBattOverVolWarningMod14": eBattOverVolWarningMod14,
       "eBattOverVolWarningMod15": eBattOverVolWarningMod15,
       "eCellChgOverTempProtMod8": eCellChgOverTempProtMod8,
       "eCellChgOverTempProtMod9": eCellChgOverTempProtMod9,
       "eCellChgOverTempProtMod10": eCellChgOverTempProtMod10,
       "eCellChgOverTempProtMod11": eCellChgOverTempProtMod11,
       "eCellChgOverTempProtMod12": eCellChgOverTempProtMod12,
       "eCellChgOverTempProtMod13": eCellChgOverTempProtMod13,
       "eCellChgOverTempProtMod14": eCellChgOverTempProtMod14,
       "eCellChgOverTempProtMod15": eCellChgOverTempProtMod15,
       "eCellDisChgOverTempProtMod8": eCellDisChgOverTempProtMod8,
       "eCellDisChgOverTempProtMod9": eCellDisChgOverTempProtMod9,
       "eCellDisChgOverTempProtMod10": eCellDisChgOverTempProtMod10,
       "eCellDisChgOverTempProtMod11": eCellDisChgOverTempProtMod11,
       "eCellDisChgOverTempProtMod12": eCellDisChgOverTempProtMod12,
       "eCellDisChgOverTempProtMod13": eCellDisChgOverTempProtMod13,
       "eCellDisChgOverTempProtMod14": eCellDisChgOverTempProtMod14,
       "eCellDisChgOverTempProtMod15": eCellDisChgOverTempProtMod15,
       "eAnyCellUnderTempProtMod8": eAnyCellUnderTempProtMod8,
       "eAnyCellUnderTempProtMod9": eAnyCellUnderTempProtMod9,
       "eAnyCellUnderTempProtMod10": eAnyCellUnderTempProtMod10,
       "eAnyCellUnderTempProtMod11": eAnyCellUnderTempProtMod11,
       "eAnyCellUnderTempProtMod12": eAnyCellUnderTempProtMod12,
       "eAnyCellUnderTempProtMod13": eAnyCellUnderTempProtMod13,
       "eAnyCellUnderTempProtMod14": eAnyCellUnderTempProtMod14,
       "eAnyCellUnderTempProtMod15": eAnyCellUnderTempProtMod15,
       "eBattChgOverCurrWarningMod8": eBattChgOverCurrWarningMod8,
       "eBattChgOverCurrWarningMod9": eBattChgOverCurrWarningMod9,
       "eBattChgOverCurrWarningMod10": eBattChgOverCurrWarningMod10,
       "eBattChgOverCurrWarningMod11": eBattChgOverCurrWarningMod11,
       "eBattChgOverCurrWarningMod12": eBattChgOverCurrWarningMod12,
       "eBattChgOverCurrWarningMod13": eBattChgOverCurrWarningMod13,
       "eBattChgOverCurrWarningMod14": eBattChgOverCurrWarningMod14,
       "eBattChgOverCurrWarningMod15": eBattChgOverCurrWarningMod15,
       "eBattDisChgOverCurrWarnMod8": eBattDisChgOverCurrWarnMod8,
       "eBattDisChgOverCurrWarnMod9": eBattDisChgOverCurrWarnMod9,
       "eBattDisChgOverCurrWarnMod10": eBattDisChgOverCurrWarnMod10,
       "eBattDisChgOverCurrWarnMod11": eBattDisChgOverCurrWarnMod11,
       "eBattDisChgOverCurrWarnMod12": eBattDisChgOverCurrWarnMod12,
       "eBattDisChgOverCurrWarnMod13": eBattDisChgOverCurrWarnMod13,
       "eBattDisChgOverCurrWarnMod14": eBattDisChgOverCurrWarnMod14,
       "eBattDisChgOverCurrWarnMod15": eBattDisChgOverCurrWarnMod15,
       "eBattLowSOCWarningMod8": eBattLowSOCWarningMod8,
       "eBattLowSOCWarningMod9": eBattLowSOCWarningMod9,
       "eBattLowSOCWarningMod10": eBattLowSOCWarningMod10,
       "eBattLowSOCWarningMod11": eBattLowSOCWarningMod11,
       "eBattLowSOCWarningMod12": eBattLowSOCWarningMod12,
       "eBattLowSOCWarningMod13": eBattLowSOCWarningMod13,
       "eBattLowSOCWarningMod14": eBattLowSOCWarningMod14,
       "eBattLowSOCWarningMod15": eBattLowSOCWarningMod15,
       "eBattOverCurrProtectionMod8": eBattOverCurrProtectionMod8,
       "eBattOverCurrProtectionMod9": eBattOverCurrProtectionMod9,
       "eBattOverCurrProtectionMod10": eBattOverCurrProtectionMod10,
       "eBattOverCurrProtectionMod11": eBattOverCurrProtectionMod11,
       "eBattOverCurrProtectionMod12": eBattOverCurrProtectionMod12,
       "eBattOverCurrProtectionMod13": eBattOverCurrProtectionMod13,
       "eBattOverCurrProtectionMod14": eBattOverCurrProtectionMod14,
       "eBattOverCurrProtectionMod15": eBattOverCurrProtectionMod15,
       "eModule8Isolated": eModule8Isolated,
       "eModule9Isolated": eModule9Isolated,
       "eModule10Isolated": eModule10Isolated,
       "eModule11Isolated": eModule11Isolated,
       "eModule12Isolated": eModule12Isolated,
       "eModule13Isolated": eModule13Isolated,
       "eModule14Isolated": eModule14Isolated,
       "eModule15Isolated": eModule15Isolated,
       "eModule8CommFailAlarm": eModule8CommFailAlarm,
       "eModule9CommFailAlarm": eModule9CommFailAlarm,
       "eModule10CommFailAlarm": eModule10CommFailAlarm,
       "eModule11CommFailAlarm": eModule11CommFailAlarm,
       "eModule12CommFailAlarm": eModule12CommFailAlarm,
       "eModule13CommFailAlarm": eModule13CommFailAlarm,
       "eModule14CommFailAlarm": eModule14CommFailAlarm,
       "eModule15CommFailAlarm": eModule15CommFailAlarm,
       "eParameters": eParameters,
       "eCurrentInfo": eCurrentInfo,
       "eChargingCurrentModule1": eChargingCurrentModule1,
       "eChargingCurrentModule2": eChargingCurrentModule2,
       "eChargingCurrentModule3": eChargingCurrentModule3,
       "eChargingCurrentModule4": eChargingCurrentModule4,
       "eChargingCurrentModule5": eChargingCurrentModule5,
       "eChargingCurrentModule6": eChargingCurrentModule6,
       "eChargingCurrentModule7": eChargingCurrentModule7,
       "eChargingCurrentModule8": eChargingCurrentModule8,
       "eChargingCurrentModule9": eChargingCurrentModule9,
       "eChargingCurrentModule10": eChargingCurrentModule10,
       "eChargingCurrentModule11": eChargingCurrentModule11,
       "eChargingCurrentModule12": eChargingCurrentModule12,
       "eChargingCurrentModule13": eChargingCurrentModule13,
       "eChargingCurrentModule14": eChargingCurrentModule14,
       "eChargingCurrentModule15": eChargingCurrentModule15,
       "eDischargingCurrentModule1": eDischargingCurrentModule1,
       "eDischargingCurrentModule2": eDischargingCurrentModule2,
       "eDischargingCurrentModule3": eDischargingCurrentModule3,
       "eDischargingCurrentModule4": eDischargingCurrentModule4,
       "eDischargingCurrentModule5": eDischargingCurrentModule5,
       "eDischargingCurrentModule6": eDischargingCurrentModule6,
       "eDischargingCurrentModule7": eDischargingCurrentModule7,
       "eDischargingCurrentModule8": eDischargingCurrentModule8,
       "eDischargingCurrentModule9": eDischargingCurrentModule9,
       "eDischargingCurrentModule10": eDischargingCurrentModule10,
       "eDischargingCurrentModule11": eDischargingCurrentModule11,
       "eDischargingCurrentModule12": eDischargingCurrentModule12,
       "eDischargingCurrentModule13": eDischargingCurrentModule13,
       "eDischargingCurrentModule14": eDischargingCurrentModule14,
       "eDischargingCurrentModule15": eDischargingCurrentModule15,
       "eSOCinfo": eSOCinfo,
       "eSOCModule1": eSOCModule1,
       "eSOCModule2": eSOCModule2,
       "eSOCModule3": eSOCModule3,
       "eSOCModule4": eSOCModule4,
       "eSOCModule5": eSOCModule5,
       "eSOCModule6": eSOCModule6,
       "eSOCModule7": eSOCModule7,
       "eSOCModule8": eSOCModule8,
       "eSOCModule9": eSOCModule9,
       "eSOCModule10": eSOCModule10,
       "eSOCModule11": eSOCModule11,
       "eSOCModule12": eSOCModule12,
       "eSOCModule13": eSOCModule13,
       "eSOCModule14": eSOCModule14,
       "eSOCModule15": eSOCModule15,
       "eSOHinfo": eSOHinfo,
       "eSOHModule1": eSOHModule1,
       "eSOHModule2": eSOHModule2,
       "eSOHModule3": eSOHModule3,
       "eSOHModule4": eSOHModule4,
       "eSOHModule5": eSOHModule5,
       "eSOHModule6": eSOHModule6,
       "eSOHModule7": eSOHModule7,
       "eSOHModule8": eSOHModule8,
       "eSOHModule9": eSOHModule9,
       "eSOHModule10": eSOHModule10,
       "eSOHModule11": eSOHModule11,
       "eSOHModule12": eSOHModule12,
       "eSOHModule13": eSOHModule13,
       "eSOHModule14": eSOHModule14,
       "eSOHModule15": eSOHModule15,
       "eBattMaxCurrInfo": eBattMaxCurrInfo,
       "eBatteryMaxTempratureModule1": eBatteryMaxTempratureModule1,
       "eBatteryMaxTempratureModule2": eBatteryMaxTempratureModule2,
       "eBatteryMaxTempratureModule3": eBatteryMaxTempratureModule3,
       "eBatteryMaxTempratureModule4": eBatteryMaxTempratureModule4,
       "eBatteryMaxTempratureModule5": eBatteryMaxTempratureModule5,
       "eBatteryMaxTempratureModule6": eBatteryMaxTempratureModule6,
       "eBatteryMaxTempratureModule7": eBatteryMaxTempratureModule7,
       "eBatteryMaxTempratureModule8": eBatteryMaxTempratureModule8,
       "eBatteryMaxTempratureModule9": eBatteryMaxTempratureModule9,
       "eBatteryMaxTempratureModule10": eBatteryMaxTempratureModule10,
       "eBatteryMaxTempratureModule11": eBatteryMaxTempratureModule11,
       "eBatteryMaxTempratureModule12": eBatteryMaxTempratureModule12,
       "eBatteryMaxTempratureModule13": eBatteryMaxTempratureModule13,
       "eBatteryMaxTempratureModule14": eBatteryMaxTempratureModule14,
       "eBatteryMaxTempratureModule15": eBatteryMaxTempratureModule15,
       "eVoltageInfo": eVoltageInfo,
       "eModuleVoltageModule1": eModuleVoltageModule1,
       "eModuleVoltageModule2": eModuleVoltageModule2,
       "eModuleVoltageModule3": eModuleVoltageModule3,
       "eModuleVoltageModule4": eModuleVoltageModule4,
       "eModuleVoltageModule5": eModuleVoltageModule5,
       "eModuleVoltageModule6": eModuleVoltageModule6,
       "eModuleVoltageModule7": eModuleVoltageModule7,
       "eModuleVoltageModule8": eModuleVoltageModule8,
       "eModuleVoltageModule9": eModuleVoltageModule9,
       "eModuleVoltageModule10": eModuleVoltageModule10,
       "eModuleVoltageModule11": eModuleVoltageModule11,
       "eModuleVoltageModule12": eModuleVoltageModule12,
       "eModuleVoltageModule13": eModuleVoltageModule13,
       "eModuleVoltageModule14": eModuleVoltageModule14,
       "eModuleVoltageModule15": eModuleVoltageModule15,
       "eSystemInfo": eSystemInfo,
       "eManufacturerName": eManufacturerName,
       "ePartNo": ePartNo,
       "eSrNo": eSrNo,
       "eDesignCapacity": eDesignCapacity,
       "eNumberOfInstalledModules": eNumberOfInstalledModules,
       "eNumberOfActiveModules": eNumberOfActiveModules,
       "eMaxChargeCurrInfo": eMaxChargeCurrInfo,
       "eModuleMaxChargeCurrentLimit": eModuleMaxChargeCurrentLimit,
       "eInstMaxModuleCurrent": eInstMaxModuleCurrent,
       "eInstantaneousMaxModuleCurrent": eInstantaneousMaxModuleCurrent,
       "eMaxDischargeCurrInfo": eMaxDischargeCurrInfo,
       "eMaxDischargeCurrentOfAModule": eMaxDischargeCurrentOfAModule,
       "eAHinfo": eAHinfo,
       "eREMAININGAHofTheBANK": eREMAININGAHofTheBANK,
       "eCumulativeBatteryChargeAH": eCumulativeBatteryChargeAH,
       "eACEMch1Info": eACEMch1Info,
       "ePowerKWMeter1": ePowerKWMeter1,
       "eEnergyKWHMeter1": eEnergyKWHMeter1,
       "eACEMch2Info": eACEMch2Info,
       "ePowerKWMeter2": ePowerKWMeter2,
       "eEnergyKWHMeter2": eEnergyKWHMeter2,
       "eACEMch3Info": eACEMch3Info,
       "ePowerKWMeter3": ePowerKWMeter3,
       "eEnergyKWHMeter3": eEnergyKWHMeter3,
       "eACEMch4Info": eACEMch4Info,
       "ePowerKWMeter4": ePowerKWMeter4,
       "eEnergyKWHMeter4": eEnergyKWHMeter4,
       "eSMPSinfo": eSMPSinfo,
       "eDCVoltage": eDCVoltage,
       "eDCCurrent": eDCCurrent,
       "eDCKWH": eDCKWH,
       "eLoadcurrent": eLoadcurrent,
       "eBatteryCurrent": eBatteryCurrent,
       "eNoOfRectifiersPoweredUp": eNoOfRectifiersPoweredUp,
       "eSMPSManufacturerName": eSMPSManufacturerName,
       "eControllerModel": eControllerModel,
       "eFirmwareVersion": eFirmwareVersion,
       "eSMPSPartNo": eSMPSPartNo,
       "eInputLineAVoltage": eInputLineAVoltage,
       "eInputLineBVoltage": eInputLineBVoltage,
       "eInputLineCVoltage": eInputLineCVoltage,
       "eInputLineACurrent": eInputLineACurrent,
       "eInputLineBCurrent": eInputLineBCurrent,
       "eInputLineCCurrent": eInputLineCCurrent,
       "eTemperature1": eTemperature1,
       "eTemperature2": eTemperature2,
       "eMainsCumulativeKWh": eMainsCumulativeKWh,
       "eMainsCumulativeRunHrs": eMainsCumulativeRunHrs,
       "eBatteryCumulativeKWh": eBatteryCumulativeKWh,
       "eBatteryCumulativeRunHrs": eBatteryCumulativeRunHrs,
       "eBatteryDischargeCycle": eBatteryDischargeCycle,
       "eDCOutputPower": eDCOutputPower,
       "eLoadCumulativeKWh": eLoadCumulativeKWh,
       "eSettingInfo": eSettingInfo,
       "eFloatVoltage": eFloatVoltage,
       "eBoostVoltage": eBoostVoltage,
       "eChargeCurrentLimit": eChargeCurrentLimit,
       "eLLVDVoltage": eLLVDVoltage,
       "eBLVDVoltage": eBLVDVoltage,
       "eAmbientHighTempThreshold": eAmbientHighTempThreshold,
       "eOverloadAlarmThreshold": eOverloadAlarmThreshold,
       "eIPAddress": eIPAddress,
       "eSAFTBatteryReset": eSAFTBatteryReset,
       "eDGinfo": eDGinfo,
       "eDGLubeOilPressure": eDGLubeOilPressure,
       "eChargingAlternatorVoltageDC": eChargingAlternatorVoltageDC,
       "eDGKWh": eDGKWh,
       "eSEBKWh": eSEBKWh,
       "eDGRunHrs": eDGRunHrs,
       "eMainsRKw": eMainsRKw,
       "eMainsYKw": eMainsYKw,
       "eMainsBKw": eMainsBKw,
       "eDGRKw": eDGRKw,
       "eDGYKw": eDGYKw,
       "eDGBKw": eDGBKw,
       "eDGFuelLevelLtr": eDGFuelLevelLtr,
       "ePACinfo": ePACinfo,
       "eSupplyAirTemperature": eSupplyAirTemperature,
       "eReturnAirTemperature": eReturnAirTemperature,
       "eReturnAirRelativeHumidity": eReturnAirRelativeHumidity,
       "eCHWControlValveOutput": eCHWControlValveOutput,
       "ePACUnitRunHours": ePACUnitRunHours,
       "eSpareDetails": eSpareDetails,
       "eSpareMeas1": eSpareMeas1,
       "eSpareMeas2": eSpareMeas2,
       "eSpareMeas3": eSpareMeas3,
       "eSpareMeas4": eSpareMeas4,
       "eSpareMeas5": eSpareMeas5,
       "eSpareMeas6": eSpareMeas6,
       "eSpareMeas7": eSpareMeas7,
       "eSpareMeas8": eSpareMeas8,
       "eSpareMeas9": eSpareMeas9,
       "eSpareMeas10": eSpareMeas10,
       "eInverterInfo": eInverterInfo,
       "eAcOutputVoltage": eAcOutputVoltage,
       "eAcOutputCurrent": eAcOutputCurrent,
       "eDcInputVoltage": eDcInputVoltage,
       "eTemperature": eTemperature,
       "eVRLAinfo": eVRLAinfo,
       "eVRLAAHrating": eVRLAAHrating,
       "eVRLAFloatVoltage": eVRLAFloatVoltage,
       "eVRLABoostVoltage": eVRLABoostVoltage,
       "eVRLAChargeCurrentLimit": eVRLAChargeCurrentLimit,
       "eVRLASOC": eVRLASOC,
       "eModeSelectionStatus": eModeSelectionStatus,
       "trapNotifications": trapNotifications,
       "tpCellOverVolProtectionMod1": tpCellOverVolProtectionMod1,
       "tpCellOverVolProtectionMod2": tpCellOverVolProtectionMod2,
       "tpCellOverVolProtectionMod3": tpCellOverVolProtectionMod3,
       "tpCellOverVolProtectionMod4": tpCellOverVolProtectionMod4,
       "tpCellOverVolProtectionMod5": tpCellOverVolProtectionMod5,
       "tpCellOverVolProtectionMod6": tpCellOverVolProtectionMod6,
       "tpCellOverVolProtectionMod7": tpCellOverVolProtectionMod7,
       "tpCellUnderVolProtectionMod1": tpCellUnderVolProtectionMod1,
       "tpCellUnderVolProtectionMod2": tpCellUnderVolProtectionMod2,
       "tpCellUnderVolProtectionMod3": tpCellUnderVolProtectionMod3,
       "tpCellUnderVolProtectionMod4": tpCellUnderVolProtectionMod4,
       "tpCellUnderVolProtectionMod5": tpCellUnderVolProtectionMod5,
       "tpCellUnderVolProtectionMod6": tpCellUnderVolProtectionMod6,
       "tpCellUnderVolProtectionMod7": tpCellUnderVolProtectionMod7,
       "tpModuleCellUnbalancedMod1": tpModuleCellUnbalancedMod1,
       "tpModuleCellUnbalancedMod2": tpModuleCellUnbalancedMod2,
       "tpModuleCellUnbalancedMod3": tpModuleCellUnbalancedMod3,
       "tpModuleCellUnbalancedMod4": tpModuleCellUnbalancedMod4,
       "tpModuleCellUnbalancedMod5": tpModuleCellUnbalancedMod5,
       "tpModuleCellUnbalancedMod6": tpModuleCellUnbalancedMod6,
       "tpModuleCellUnbalancedMod7": tpModuleCellUnbalancedMod7,
       "tpBattUnderVolWarningMod1": tpBattUnderVolWarningMod1,
       "tpBattUnderVolWarningMod2": tpBattUnderVolWarningMod2,
       "tpBattUnderVolWarningMod3": tpBattUnderVolWarningMod3,
       "tpBattUnderVolWarningMod4": tpBattUnderVolWarningMod4,
       "tpBattUnderVolWarningMod5": tpBattUnderVolWarningMod5,
       "tpBattUnderVolWarningMod6": tpBattUnderVolWarningMod6,
       "tpBattUnderVolWarningMod7": tpBattUnderVolWarningMod7,
       "tpBattOverVolWarningMod1": tpBattOverVolWarningMod1,
       "tpBattOverVolWarningMod2": tpBattOverVolWarningMod2,
       "tpBattOverVolWarningMod3": tpBattOverVolWarningMod3,
       "tpBattOverVolWarningMod4": tpBattOverVolWarningMod4,
       "tpBattOverVolWarningMod5": tpBattOverVolWarningMod5,
       "tpBattOverVolWarningMod6": tpBattOverVolWarningMod6,
       "tpBattOverVolWarningMod7": tpBattOverVolWarningMod7,
       "tpCellChgOverTempProtMod1": tpCellChgOverTempProtMod1,
       "tpCellChgOverTempProtMod2": tpCellChgOverTempProtMod2,
       "tpCellChgOverTempProtMod3": tpCellChgOverTempProtMod3,
       "tpCellChgOverTempProtMod4": tpCellChgOverTempProtMod4,
       "tpCellChgOverTempProtMod5": tpCellChgOverTempProtMod5,
       "tpCellChgOverTempProtMod6": tpCellChgOverTempProtMod6,
       "tpCellChgOverTempProtMod7": tpCellChgOverTempProtMod7,
       "tpCellDisChgOverTempProtMod1": tpCellDisChgOverTempProtMod1,
       "tpCellDisChgOverTempProtMod2": tpCellDisChgOverTempProtMod2,
       "tpCellDisChgOverTempProtMod3": tpCellDisChgOverTempProtMod3,
       "tpCellDisChgOverTempProtMod4": tpCellDisChgOverTempProtMod4,
       "tpCellDisChgOverTempProtMod5": tpCellDisChgOverTempProtMod5,
       "tpCellDisChgOverTempProtMod6": tpCellDisChgOverTempProtMod6,
       "tpCellDisChgOverTempProtMod7": tpCellDisChgOverTempProtMod7,
       "tpAnyCellUnderTempProtMod1": tpAnyCellUnderTempProtMod1,
       "tpAnyCellUnderTempProtMod2": tpAnyCellUnderTempProtMod2,
       "tpAnyCellUnderTempProtMod3": tpAnyCellUnderTempProtMod3,
       "tpAnyCellUnderTempProtMod4": tpAnyCellUnderTempProtMod4,
       "tpAnyCellUnderTempProtMod5": tpAnyCellUnderTempProtMod5,
       "tpAnyCellUnderTempProtMod6": tpAnyCellUnderTempProtMod6,
       "tpAnyCellUnderTempProtMod7": tpAnyCellUnderTempProtMod7,
       "tpBattChgOverCurrWarningMod1": tpBattChgOverCurrWarningMod1,
       "tpBattChgOverCurrWarningMod2": tpBattChgOverCurrWarningMod2,
       "tpBattChgOverCurrWarningMod3": tpBattChgOverCurrWarningMod3,
       "tpBattChgOverCurrWarningMod4": tpBattChgOverCurrWarningMod4,
       "tpBattChgOverCurrWarningMod5": tpBattChgOverCurrWarningMod5,
       "tpBattChgOverCurrWarningMod6": tpBattChgOverCurrWarningMod6,
       "tpBattChgOverCurrWarningMod7": tpBattChgOverCurrWarningMod7,
       "tpBattDisChgOverCurrWarnMod1": tpBattDisChgOverCurrWarnMod1,
       "tpBattDisChgOverCurrWarnMod2": tpBattDisChgOverCurrWarnMod2,
       "tpBattDisChgOverCurrWarnMod3": tpBattDisChgOverCurrWarnMod3,
       "tpBattDisChgOverCurrWarnMod4": tpBattDisChgOverCurrWarnMod4,
       "tpBattDisChgOverCurrWarnMod5": tpBattDisChgOverCurrWarnMod5,
       "tpBattDisChgOverCurrWarnMod6": tpBattDisChgOverCurrWarnMod6,
       "tpBattDisChgOverCurrWarnMod7": tpBattDisChgOverCurrWarnMod7,
       "tpBattLowSOCWarningMod1": tpBattLowSOCWarningMod1,
       "tpBattLowSOCWarningMod2": tpBattLowSOCWarningMod2,
       "tpBattLowSOCWarningMod3": tpBattLowSOCWarningMod3,
       "tpBattLowSOCWarningMod4": tpBattLowSOCWarningMod4,
       "tpBattLowSOCWarningMod5": tpBattLowSOCWarningMod5,
       "tpBattLowSOCWarningMod6": tpBattLowSOCWarningMod6,
       "tpBattLowSOCWarningMod7": tpBattLowSOCWarningMod7,
       "tpBattOverCurrProtectionMod1": tpBattOverCurrProtectionMod1,
       "tpBattOverCurrProtectionMod2": tpBattOverCurrProtectionMod2,
       "tpBattOverCurrProtectionMod3": tpBattOverCurrProtectionMod3,
       "tpBattOverCurrProtectionMod4": tpBattOverCurrProtectionMod4,
       "tpBattOverCurrProtectionMod5": tpBattOverCurrProtectionMod5,
       "tpBattOverCurrProtectionMod6": tpBattOverCurrProtectionMod6,
       "tpBattOverCurrProtectionMod7": tpBattOverCurrProtectionMod7,
       "tpBattOverVolProtectionMod1": tpBattOverVolProtectionMod1,
       "tpBattOverVolProtectionMod2": tpBattOverVolProtectionMod2,
       "tpBattOverVolProtectionMod3": tpBattOverVolProtectionMod3,
       "tpBattOverVolProtectionMod4": tpBattOverVolProtectionMod4,
       "tpBattOverVolProtectionMod5": tpBattOverVolProtectionMod5,
       "tpBattOverVolProtectionMod6": tpBattOverVolProtectionMod6,
       "tpBattOverVolProtectionMod7": tpBattOverVolProtectionMod7,
       "tpBattBankVolAlarm": tpBattBankVolAlarm,
       "tpBattUnderVolProtAnyModule": tpBattUnderVolProtAnyModule,
       "tpModule1Isolated": tpModule1Isolated,
       "tpModule2Isolated": tpModule2Isolated,
       "tpModule3Isolated": tpModule3Isolated,
       "tpModule4Isolated": tpModule4Isolated,
       "tpModule5Isolated": tpModule5Isolated,
       "tpModule6Isolated": tpModule6Isolated,
       "tpModule7Isolated": tpModule7Isolated,
       "tpBatteryBanklevel1lowVolAL": tpBatteryBanklevel1lowVolAL,
       "tpBatteryBanklevel2lowVolAL": tpBatteryBanklevel2lowVolAL,
       "tpBatteryBankhighTempAlarm": tpBatteryBankhighTempAlarm,
       "tpBatteryBanklowTempAlarm": tpBatteryBanklowTempAlarm,
       "tpAnymoduleCurrhighAlarm": tpAnymoduleCurrhighAlarm,
       "tpSOCBelowLvl1ThresAlAnyMod": tpSOCBelowLvl1ThresAlAnyMod,
       "tpSystemfail": tpSystemfail,
       "tpMasterCBMSControllerFailAl": tpMasterCBMSControllerFailAl,
       "tpCellIsGoingOvTemp-1stLevel": tpCellIsGoingOvTemp_1stLevel,
       "tpCellIsGoingOvChg1-stLevel": tpCellIsGoingOvChg1_stLevel,
       "tpCellIsGoingOvChg2-ndLevel": tpCellIsGoingOvChg2_ndLevel,
       "tpCellIsGoingunderVol": tpCellIsGoingunderVol,
       "tpLowSOC": tpLowSOC,
       "tpAmosfetisgoingoverTemp": tpAmosfetisgoingoverTemp,
       "tpHeaterFailure": tpHeaterFailure,
       "tpLowSOH": tpLowSOH,
       "tpUnbalancecell": tpUnbalancecell,
       "tpMosfetTempoutofRange": tpMosfetTempoutofRange,
       "tpEmergencyAlarmModule1": tpEmergencyAlarmModule1,
       "tpCellTempoutofRangeModule1": tpCellTempoutofRangeModule1,
       "tpHighBatterysupplyModule1": tpHighBatterysupplyModule1,
       "tpMosfetisoverTempModule1": tpMosfetisoverTempModule1,
       "tpAutotestFailureModule1": tpAutotestFailureModule1,
       "tpEmergencyAlarmModule2": tpEmergencyAlarmModule2,
       "tpCellTempoutofRangeModule2": tpCellTempoutofRangeModule2,
       "tpHighBatterysupplyModule2": tpHighBatterysupplyModule2,
       "tpMosfetisoverTempModule2": tpMosfetisoverTempModule2,
       "tpAutotestFailureModule2": tpAutotestFailureModule2,
       "tpEmergencyAlarmModule3": tpEmergencyAlarmModule3,
       "tpCellTempoutofRangeModule3": tpCellTempoutofRangeModule3,
       "tpHighBatterysupplyModule3": tpHighBatterysupplyModule3,
       "tpMosfetisoverTempModule3": tpMosfetisoverTempModule3,
       "tpAutotestFailureModule3": tpAutotestFailureModule3,
       "tpEmergencyAlarmModule4": tpEmergencyAlarmModule4,
       "tpCellTempoutofRangeModule4": tpCellTempoutofRangeModule4,
       "tpHighBatterysupplyModule4": tpHighBatterysupplyModule4,
       "tpMosfetisoverTempModule4": tpMosfetisoverTempModule4,
       "tpAutotestFailureModule4": tpAutotestFailureModule4,
       "tpEmergencyAlarmModule5": tpEmergencyAlarmModule5,
       "tpCellTempoutofRangeModule5": tpCellTempoutofRangeModule5,
       "tpHighBatterysupplyModule5": tpHighBatterysupplyModule5,
       "tpMosfetisoverTempModule5": tpMosfetisoverTempModule5,
       "tpAutotestFailureModule5": tpAutotestFailureModule5,
       "tpEmergencyAlarmModule6": tpEmergencyAlarmModule6,
       "tpCellTempoutofRangeModule6": tpCellTempoutofRangeModule6,
       "tpHighBatterysupplyModule6": tpHighBatterysupplyModule6,
       "tpMosfetisoverTempModule6": tpMosfetisoverTempModule6,
       "tpAutotestFailureModule6": tpAutotestFailureModule6,
       "tpEmergencyAlarmModule7": tpEmergencyAlarmModule7,
       "tpCellTempoutofRangeModule7": tpCellTempoutofRangeModule7,
       "tpHighBatterysupplyModule7": tpHighBatterysupplyModule7,
       "tpMosfetisoverTempModule7": tpMosfetisoverTempModule7,
       "tpAutotestFailureModule7": tpAutotestFailureModule7,
       "tpACPowerfail": tpACPowerfail,
       "tpACDBIncomerTrip": tpACDBIncomerTrip,
       "tpRectifierModule1Fail": tpRectifierModule1Fail,
       "tpRectifierModule2Fail": tpRectifierModule2Fail,
       "tpRectifierModule3Fail": tpRectifierModule3Fail,
       "tpRectifierModule4Fail": tpRectifierModule4Fail,
       "tpLoadFusetrip": tpLoadFusetrip,
       "tpLLVDAlarm": tpLLVDAlarm,
       "tpBLVDAlarm": tpBLVDAlarm,
       "tpBatteryfuseFail": tpBatteryfuseFail,
       "tpBatteryonLoad": tpBatteryonLoad,
       "tpTopDoorOpen": tpTopDoorOpen,
       "tpBottomDoorOpen": tpBottomDoorOpen,
       "tpFireAlarm": tpFireAlarm,
       "tpShelterDoorOpen": tpShelterDoorOpen,
       "tpEquipmentDoorOpen": tpEquipmentDoorOpen,
       "tpDGFailToStart": tpDGFailToStart,
       "tpDGCanopyTempHigh": tpDGCanopyTempHigh,
       "tpDGLowFuelLevelWarning": tpDGLowFuelLevelWarning,
       "tpDGLowFuelLevelTrip": tpDGLowFuelLevelTrip,
       "tpDGUnderFrequency": tpDGUnderFrequency,
       "tpDGCommonFault": tpDGCommonFault,
       "tpDGOverload": tpDGOverload,
       "tpLoadOnDG": tpLoadOnDG,
       "tpDGEngineOverSpeed": tpDGEngineOverSpeed,
       "tpDGIdleRunning": tpDGIdleRunning,
       "tpDGInManual": tpDGInManual,
       "tpDGBatteryChargerFaulty": tpDGBatteryChargerFaulty,
       "tpDGCanopyDoorOpen": tpDGCanopyDoorOpen,
       "tpDGLLOP": tpDGLLOP,
       "tpDGReserve": tpDGReserve,
       "tpShelterTempHigh": tpShelterTempHigh,
       "tpPACFault": tpPACFault,
       "tpPACRunStatus": tpPACRunStatus,
       "tpPACTripStatus": tpPACTripStatus,
       "tpDiffPressureFilterStatus": tpDiffPressureFilterStatus,
       "tpCommFail-BMSToPC": tpCommFail_BMSToPC,
       "tpAuxillaryEvent1": tpAuxillaryEvent1,
       "tpAuxillaryEvent2": tpAuxillaryEvent2,
       "tpAuxillaryEvent3": tpAuxillaryEvent3,
       "tpAuxillaryEvent4": tpAuxillaryEvent4,
       "tpAuxillaryEvent5": tpAuxillaryEvent5,
       "tpInverterFail1": tpInverterFail1,
       "tpInverterFail2": tpInverterFail2,
       "tpSPARE3": tpSPARE3,
       "tpSPARE4": tpSPARE4,
       "tpSPARE5": tpSPARE5,
       "tpModule1CommFailAlarm": tpModule1CommFailAlarm,
       "tpModule2CommFailAlarm": tpModule2CommFailAlarm,
       "tpModule3CommFailAlarm": tpModule3CommFailAlarm,
       "tpModule4CommFailAlarm": tpModule4CommFailAlarm,
       "tpModule5CommFailAlarm": tpModule5CommFailAlarm,
       "tpModule6CommFailAlarm": tpModule6CommFailAlarm,
       "tpModule7CommFailAlarm": tpModule7CommFailAlarm,
       "tpInverterOutputShort": tpInverterOutputShort,
       "tpInverterOutputOverload": tpInverterOutputOverload,
       "tpInverterCommonFault": tpInverterCommonFault,
       "tpAcInputVoltageLow": tpAcInputVoltageLow,
       "tpAcInputVoltageHigh": tpAcInputVoltageHigh,
       "tpAcInputFreqLow": tpAcInputFreqLow,
       "tpAcInputFreqHigh": tpAcInputFreqHigh,
       "tpBypassMode": tpBypassMode,
       "tpFaultShutDown": tpFaultShutDown,
       "tpModuleCellUnbalancedMod8": tpModuleCellUnbalancedMod8,
       "tpModuleCellUnbalancedMod9": tpModuleCellUnbalancedMod9,
       "tpModuleCellUnbalancedMod10": tpModuleCellUnbalancedMod10,
       "tpModuleCellUnbalancedMod11": tpModuleCellUnbalancedMod11,
       "tpModuleCellUnbalancedMod12": tpModuleCellUnbalancedMod12,
       "tpModuleCellUnbalancedMod13": tpModuleCellUnbalancedMod13,
       "tpModuleCellUnbalancedMod14": tpModuleCellUnbalancedMod14,
       "tpModuleCellUnbalancedMod15": tpModuleCellUnbalancedMod15,
       "tpBattUnderVolWarningMod8": tpBattUnderVolWarningMod8,
       "tpBattUnderVolWarningMod9": tpBattUnderVolWarningMod9,
       "tpBattUnderVolWarningMod10": tpBattUnderVolWarningMod10,
       "tpBattUnderVolWarningMod11": tpBattUnderVolWarningMod11,
       "tpBattUnderVolWarningMod12": tpBattUnderVolWarningMod12,
       "tpBattUnderVolWarningMod13": tpBattUnderVolWarningMod13,
       "tpBattUnderVolWarningMod14": tpBattUnderVolWarningMod14,
       "tpBattUnderVolWarningMod15": tpBattUnderVolWarningMod15,
       "tpBattOverVolWarningMod8": tpBattOverVolWarningMod8,
       "tpBattOverVolWarningMod9": tpBattOverVolWarningMod9,
       "tpBattOverVolWarningMod10": tpBattOverVolWarningMod10,
       "tpBattOverVolWarningMod11": tpBattOverVolWarningMod11,
       "tpBattOverVolWarningMod12": tpBattOverVolWarningMod12,
       "tpBattOverVolWarningMod13": tpBattOverVolWarningMod13,
       "tpBattOverVolWarningMod14": tpBattOverVolWarningMod14,
       "tpBattOverVolWarningMod15": tpBattOverVolWarningMod15,
       "tpCellChgOverTempProtMod8": tpCellChgOverTempProtMod8,
       "tpCellChgOverTempProtMod9": tpCellChgOverTempProtMod9,
       "tpCellChgOverTempProtMod10": tpCellChgOverTempProtMod10,
       "tpCellChgOverTempProtMod11": tpCellChgOverTempProtMod11,
       "tpCellChgOverTempProtMod12": tpCellChgOverTempProtMod12,
       "tpCellChgOverTempProtMod13": tpCellChgOverTempProtMod13,
       "tpCellChgOverTempProtMod14": tpCellChgOverTempProtMod14,
       "tpCellChgOverTempProtMod15": tpCellChgOverTempProtMod15,
       "tpCellDisChgOverTempProtMod8": tpCellDisChgOverTempProtMod8,
       "tpCellDisChgOverTempProtMod9": tpCellDisChgOverTempProtMod9,
       "tpCellDisChgOverTempProtMod10": tpCellDisChgOverTempProtMod10,
       "tpCellDisChgOverTempProtMod11": tpCellDisChgOverTempProtMod11,
       "tpCellDisChgOverTempProtMod12": tpCellDisChgOverTempProtMod12,
       "tpCellDisChgOverTempProtMod13": tpCellDisChgOverTempProtMod13,
       "tpCellDisChgOverTempProtMod14": tpCellDisChgOverTempProtMod14,
       "tpCellDisChgOverTempProtMod15": tpCellDisChgOverTempProtMod15,
       "tpAnyCellUnderTempProtMod8": tpAnyCellUnderTempProtMod8,
       "tpAnyCellUnderTempProtMod9": tpAnyCellUnderTempProtMod9,
       "tpAnyCellUnderTempProtMod10": tpAnyCellUnderTempProtMod10,
       "tpAnyCellUnderTempProtMod11": tpAnyCellUnderTempProtMod11,
       "tpAnyCellUnderTempProtMod12": tpAnyCellUnderTempProtMod12,
       "tpAnyCellUnderTempProtMod13": tpAnyCellUnderTempProtMod13,
       "tpAnyCellUnderTempProtMod14": tpAnyCellUnderTempProtMod14,
       "tpAnyCellUnderTempProtMod15": tpAnyCellUnderTempProtMod15,
       "tpBattChgOverCurrWarningMod8": tpBattChgOverCurrWarningMod8,
       "tpBattChgOverCurrWarningMod9": tpBattChgOverCurrWarningMod9,
       "tpBattChgOverCurrWarningMod10": tpBattChgOverCurrWarningMod10,
       "tpBattChgOverCurrWarningMod11": tpBattChgOverCurrWarningMod11,
       "tpBattChgOverCurrWarningMod12": tpBattChgOverCurrWarningMod12,
       "tpBattChgOverCurrWarningMod13": tpBattChgOverCurrWarningMod13,
       "tpBattChgOverCurrWarningMod14": tpBattChgOverCurrWarningMod14,
       "tpBattChgOverCurrWarningMod15": tpBattChgOverCurrWarningMod15,
       "tpBattDisChgOverCurrWarnMod8": tpBattDisChgOverCurrWarnMod8,
       "tpBattDisChgOverCurrWarnMod9": tpBattDisChgOverCurrWarnMod9,
       "tpBattDisChgOverCurrWarnMod10": tpBattDisChgOverCurrWarnMod10,
       "tpBattDisChgOverCurrWarnMod11": tpBattDisChgOverCurrWarnMod11,
       "tpBattDisChgOverCurrWarnMod12": tpBattDisChgOverCurrWarnMod12,
       "tpBattDisChgOverCurrWarnMod13": tpBattDisChgOverCurrWarnMod13,
       "tpBattDisChgOverCurrWarnMod14": tpBattDisChgOverCurrWarnMod14,
       "tpBattDisChgOverCurrWarnMod15": tpBattDisChgOverCurrWarnMod15,
       "tpBattLowSOCWarningMod8": tpBattLowSOCWarningMod8,
       "tpBattLowSOCWarningMod9": tpBattLowSOCWarningMod9,
       "tpBattLowSOCWarningMod10": tpBattLowSOCWarningMod10,
       "tpBattLowSOCWarningMod11": tpBattLowSOCWarningMod11,
       "tpBattLowSOCWarningMod12": tpBattLowSOCWarningMod12,
       "tpBattLowSOCWarningMod13": tpBattLowSOCWarningMod13,
       "tpBattLowSOCWarningMod14": tpBattLowSOCWarningMod14,
       "tpBattLowSOCWarningMod15": tpBattLowSOCWarningMod15,
       "tpBattOverCurrProtectionMod8": tpBattOverCurrProtectionMod8,
       "tpBattOverCurrProtectionMod9": tpBattOverCurrProtectionMod9,
       "tpBattOverCurrProtectionMod10": tpBattOverCurrProtectionMod10,
       "tpBattOverCurrProtectionMod11": tpBattOverCurrProtectionMod11,
       "tpBattOverCurrProtectionMod12": tpBattOverCurrProtectionMod12,
       "tpBattOverCurrProtectionMod13": tpBattOverCurrProtectionMod13,
       "tpBattOverCurrProtectionMod14": tpBattOverCurrProtectionMod14,
       "tpBattOverCurrProtectionMod15": tpBattOverCurrProtectionMod15,
       "tpModule8Isolated": tpModule8Isolated,
       "tpModule9Isolated": tpModule9Isolated,
       "tpModule10Isolated": tpModule10Isolated,
       "tpModule11Isolated": tpModule11Isolated,
       "tpModule12Isolated": tpModule12Isolated,
       "tpModule13Isolated": tpModule13Isolated,
       "tpModule14Isolated": tpModule14Isolated,
       "tpModule15Isolated": tpModule15Isolated,
       "tpModule8CommFailAlarm": tpModule8CommFailAlarm,
       "tpModule9CommFailAlarm": tpModule9CommFailAlarm,
       "tpModule10CommFailAlarm": tpModule10CommFailAlarm,
       "tpModule11CommFailAlarm": tpModule11CommFailAlarm,
       "tpModule12CommFailAlarm": tpModule12CommFailAlarm,
       "tpModule13CommFailAlarm": tpModule13CommFailAlarm,
       "tpModule14CommFailAlarm": tpModule14CommFailAlarm,
       "tpModule15CommFailAlarm": tpModule15CommFailAlarm,
       "internal": internal,
       "internaltraps": internaltraps,
       "tpSystemReset": tpSystemReset,
       "tpPeriodicTrap": tpPeriodicTrap,
       "tpGenericTrap": tpGenericTrap,
       "tpCommFailPCtoSMPS": tpCommFailPCtoSMPS,
       "tpCommFailACEM": tpCommFailACEM,
       "tpCommFailInverter": tpCommFailInverter,
       "tpCommFailDGController": tpCommFailDGController,
       "tpCommFailPAC": tpCommFailPAC,
       "internalparams": internalparams,
       "eSystemResetCause": eSystemResetCause,
       "ePeriodicTrap": ePeriodicTrap,
       "eGenericTrap": eGenericTrap,
       "devicestatus": devicestatus,
       "eCommFailPCtoSMPS": eCommFailPCtoSMPS,
       "eCommFailACEM": eCommFailACEM,
       "eCommFailInverter": eCommFailInverter,
       "eCommFailDGController": eCommFailDGController,
       "eCommFailPAC": eCommFailPAC,
       "control": control,
       "cTrapResendFlag": cTrapResendFlag,
       "dpsInfo": dpsInfo}
)
