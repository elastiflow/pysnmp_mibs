# SNMP MIB module (DELTAPOWERSOLUTIONS-AG3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_40288/DELTAPOWERSOLUTIONS-AG3-MIB.mib
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
_Ag3_ObjectIdentity = ObjectIdentity
ag3 = _Ag3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2)
)
_Root_ObjectIdentity = ObjectIdentity
root = _Root_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2)
)
_Ipv4TrapTable_Object = MibTable
ipv4TrapTable = _Ipv4TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipv4TrapTable.setStatus("current")
_Ipv4TrapEntry_Object = MibTableRow
ipv4TrapEntry = _Ipv4TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 1, 1)
)
ipv4TrapEntry.setIndexNames(
    (0, "DELTAPOWERSOLUTIONS-AG3-MIB", "ipv4TrapReceiverNumber"),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 1, 1, 2),
    _Ipv4TrapEnabled_Type()
)
ipv4TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapEnabled.setStatus("current")
_Ipv4TrapReceiverIPAddress_Type = IpAddress
_Ipv4TrapReceiverIPAddress_Object = MibTableColumn
ipv4TrapReceiverIPAddress = _Ipv4TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 2),
    _Siteid_Type()
)
siteid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteid.setStatus("current")
_Ipv6TrapTable_Object = MibTable
ipv6TrapTable = _Ipv6TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipv6TrapTable.setStatus("current")
_Ipv6TrapEntry_Object = MibTableRow
ipv6TrapEntry = _Ipv6TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 3, 1)
)
ipv6TrapEntry.setIndexNames(
    (0, "DELTAPOWERSOLUTIONS-AG3-MIB", "ipv6TrapReceiverNumber"),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 2, 3, 1, 4),
    _Ipv6TrapCommunity_Type()
)
ipv6TrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6TrapCommunity.setStatus("current")
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3)
)
_EAlarms_ObjectIdentity = ObjectIdentity
eAlarms = _EAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1)
)
_EAlarmsGp_ObjectIdentity = ObjectIdentity
eAlarmsGp = _EAlarmsGp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 7),
    _ECellOverVolProtectionMod7_Type()
)
eCellOverVolProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod7.setStatus("current")


class _ECellOverVolProtectionMod8_Type(Integer32):
    """Custom type eCellOverVolProtectionMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod8_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod8_Object = MibScalar
eCellOverVolProtectionMod8 = _ECellOverVolProtectionMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 8),
    _ECellOverVolProtectionMod8_Type()
)
eCellOverVolProtectionMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod8.setStatus("current")


class _ECellOverVolProtectionMod9_Type(Integer32):
    """Custom type eCellOverVolProtectionMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod9_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod9_Object = MibScalar
eCellOverVolProtectionMod9 = _ECellOverVolProtectionMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 9),
    _ECellOverVolProtectionMod9_Type()
)
eCellOverVolProtectionMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod9.setStatus("current")


class _ECellOverVolProtectionMod10_Type(Integer32):
    """Custom type eCellOverVolProtectionMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod10_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod10_Object = MibScalar
eCellOverVolProtectionMod10 = _ECellOverVolProtectionMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 10),
    _ECellOverVolProtectionMod10_Type()
)
eCellOverVolProtectionMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod10.setStatus("current")


class _ECellOverVolProtectionMod11_Type(Integer32):
    """Custom type eCellOverVolProtectionMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod11_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod11_Object = MibScalar
eCellOverVolProtectionMod11 = _ECellOverVolProtectionMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 11),
    _ECellOverVolProtectionMod11_Type()
)
eCellOverVolProtectionMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod11.setStatus("current")


class _ECellOverVolProtectionMod12_Type(Integer32):
    """Custom type eCellOverVolProtectionMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod12_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod12_Object = MibScalar
eCellOverVolProtectionMod12 = _ECellOverVolProtectionMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 12),
    _ECellOverVolProtectionMod12_Type()
)
eCellOverVolProtectionMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod12.setStatus("current")


class _ECellOverVolProtectionMod13_Type(Integer32):
    """Custom type eCellOverVolProtectionMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod13_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod13_Object = MibScalar
eCellOverVolProtectionMod13 = _ECellOverVolProtectionMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 13),
    _ECellOverVolProtectionMod13_Type()
)
eCellOverVolProtectionMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod13.setStatus("current")


class _ECellOverVolProtectionMod14_Type(Integer32):
    """Custom type eCellOverVolProtectionMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod14_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod14_Object = MibScalar
eCellOverVolProtectionMod14 = _ECellOverVolProtectionMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 14),
    _ECellOverVolProtectionMod14_Type()
)
eCellOverVolProtectionMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod14.setStatus("current")


class _ECellOverVolProtectionMod15_Type(Integer32):
    """Custom type eCellOverVolProtectionMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellOverVolProtectionMod15_Type.__name__ = "Integer32"
_ECellOverVolProtectionMod15_Object = MibScalar
eCellOverVolProtectionMod15 = _ECellOverVolProtectionMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 15),
    _ECellOverVolProtectionMod15_Type()
)
eCellOverVolProtectionMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellOverVolProtectionMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 22),
    _ECellUnderVolProtectionMod7_Type()
)
eCellUnderVolProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod7.setStatus("current")


class _ECellUnderVolProtectionMod8_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod8_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod8_Object = MibScalar
eCellUnderVolProtectionMod8 = _ECellUnderVolProtectionMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 23),
    _ECellUnderVolProtectionMod8_Type()
)
eCellUnderVolProtectionMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod8.setStatus("current")


class _ECellUnderVolProtectionMod9_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod9_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod9_Object = MibScalar
eCellUnderVolProtectionMod9 = _ECellUnderVolProtectionMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 24),
    _ECellUnderVolProtectionMod9_Type()
)
eCellUnderVolProtectionMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod9.setStatus("current")


class _ECellUnderVolProtectionMod10_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod10_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod10_Object = MibScalar
eCellUnderVolProtectionMod10 = _ECellUnderVolProtectionMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 25),
    _ECellUnderVolProtectionMod10_Type()
)
eCellUnderVolProtectionMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod10.setStatus("current")


class _ECellUnderVolProtectionMod11_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod11_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod11_Object = MibScalar
eCellUnderVolProtectionMod11 = _ECellUnderVolProtectionMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 26),
    _ECellUnderVolProtectionMod11_Type()
)
eCellUnderVolProtectionMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod11.setStatus("current")


class _ECellUnderVolProtectionMod12_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod12_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod12_Object = MibScalar
eCellUnderVolProtectionMod12 = _ECellUnderVolProtectionMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 27),
    _ECellUnderVolProtectionMod12_Type()
)
eCellUnderVolProtectionMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod12.setStatus("current")


class _ECellUnderVolProtectionMod13_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod13_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod13_Object = MibScalar
eCellUnderVolProtectionMod13 = _ECellUnderVolProtectionMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 28),
    _ECellUnderVolProtectionMod13_Type()
)
eCellUnderVolProtectionMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod13.setStatus("current")


class _ECellUnderVolProtectionMod14_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod14_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod14_Object = MibScalar
eCellUnderVolProtectionMod14 = _ECellUnderVolProtectionMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 29),
    _ECellUnderVolProtectionMod14_Type()
)
eCellUnderVolProtectionMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod14.setStatus("current")


class _ECellUnderVolProtectionMod15_Type(Integer32):
    """Custom type eCellUnderVolProtectionMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECellUnderVolProtectionMod15_Type.__name__ = "Integer32"
_ECellUnderVolProtectionMod15_Object = MibScalar
eCellUnderVolProtectionMod15 = _ECellUnderVolProtectionMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 30),
    _ECellUnderVolProtectionMod15_Type()
)
eCellUnderVolProtectionMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellUnderVolProtectionMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 31),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 32),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 33),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 34),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 35),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 36),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 37),
    _EBattUnderVolWarningMod7_Type()
)
eBattUnderVolWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 38),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 39),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 40),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 41),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 42),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 43),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 44),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 45),
    _EBattUnderVolWarningMod15_Type()
)
eBattUnderVolWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattUnderVolWarningMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 46),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 47),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 48),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 49),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 50),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 51),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 52),
    _EBattOverVolWarningMod7_Type()
)
eBattOverVolWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 53),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 54),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 55),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 56),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 57),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 58),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 59),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 60),
    _EBattOverVolWarningMod15_Type()
)
eBattOverVolWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolWarningMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 61),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 62),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 63),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 64),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 65),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 66),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 67),
    _ECellChgOverTempProtMod7_Type()
)
eCellChgOverTempProtMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 68),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 69),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 70),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 71),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 72),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 73),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 74),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 75),
    _ECellChgOverTempProtMod15_Type()
)
eCellChgOverTempProtMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellChgOverTempProtMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 76),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 77),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 78),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 79),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 80),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 81),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 82),
    _ECellDisChgOverTempProtMod7_Type()
)
eCellDisChgOverTempProtMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 83),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 84),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 85),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 86),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 87),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 88),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 89),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 90),
    _ECellDisChgOverTempProtMod15_Type()
)
eCellDisChgOverTempProtMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCellDisChgOverTempProtMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 91),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 92),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 93),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 94),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 95),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 96),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 97),
    _EAnyCellUnderTempProtMod7_Type()
)
eAnyCellUnderTempProtMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 98),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 99),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 100),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 101),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 102),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 103),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 104),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 105),
    _EAnyCellUnderTempProtMod15_Type()
)
eAnyCellUnderTempProtMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAnyCellUnderTempProtMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 106),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 107),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 108),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 109),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 110),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 111),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 112),
    _EBattChgOverCurrWarningMod7_Type()
)
eBattChgOverCurrWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 113),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 114),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 115),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 116),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 117),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 118),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 119),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 120),
    _EBattChgOverCurrWarningMod15_Type()
)
eBattChgOverCurrWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattChgOverCurrWarningMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 121),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 122),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 123),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 124),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 125),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 126),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 127),
    _EBattDisChgOverCurrWarnMod7_Type()
)
eBattDisChgOverCurrWarnMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 128),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 129),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 130),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 131),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 132),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 133),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 134),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 135),
    _EBattDisChgOverCurrWarnMod15_Type()
)
eBattDisChgOverCurrWarnMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattDisChgOverCurrWarnMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 136),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 137),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 138),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 139),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 140),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 141),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 142),
    _EBattLowSOCWarningMod7_Type()
)
eBattLowSOCWarningMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 143),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 144),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 145),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 146),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 147),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 148),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 149),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 150),
    _EBattLowSOCWarningMod15_Type()
)
eBattLowSOCWarningMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattLowSOCWarningMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 151),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 152),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 153),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 154),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 155),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 156),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 157),
    _EBattOverCurrProtectionMod7_Type()
)
eBattOverCurrProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod7.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 158),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 159),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 160),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 161),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 162),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 163),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 164),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 165),
    _EBattOverCurrProtectionMod15_Type()
)
eBattOverCurrProtectionMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverCurrProtectionMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 166),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 167),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 168),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 169),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 170),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 171),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 172),
    _EBattOverVolProtectionMod7_Type()
)
eBattOverVolProtectionMod7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod7.setStatus("current")


class _EBattOverVolProtectionMod8_Type(Integer32):
    """Custom type eBattOverVolProtectionMod8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod8_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod8_Object = MibScalar
eBattOverVolProtectionMod8 = _EBattOverVolProtectionMod8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 173),
    _EBattOverVolProtectionMod8_Type()
)
eBattOverVolProtectionMod8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod8.setStatus("current")


class _EBattOverVolProtectionMod9_Type(Integer32):
    """Custom type eBattOverVolProtectionMod9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod9_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod9_Object = MibScalar
eBattOverVolProtectionMod9 = _EBattOverVolProtectionMod9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 174),
    _EBattOverVolProtectionMod9_Type()
)
eBattOverVolProtectionMod9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod9.setStatus("current")


class _EBattOverVolProtectionMod10_Type(Integer32):
    """Custom type eBattOverVolProtectionMod10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod10_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod10_Object = MibScalar
eBattOverVolProtectionMod10 = _EBattOverVolProtectionMod10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 175),
    _EBattOverVolProtectionMod10_Type()
)
eBattOverVolProtectionMod10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod10.setStatus("current")


class _EBattOverVolProtectionMod11_Type(Integer32):
    """Custom type eBattOverVolProtectionMod11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod11_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod11_Object = MibScalar
eBattOverVolProtectionMod11 = _EBattOverVolProtectionMod11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 176),
    _EBattOverVolProtectionMod11_Type()
)
eBattOverVolProtectionMod11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod11.setStatus("current")


class _EBattOverVolProtectionMod12_Type(Integer32):
    """Custom type eBattOverVolProtectionMod12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod12_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod12_Object = MibScalar
eBattOverVolProtectionMod12 = _EBattOverVolProtectionMod12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 177),
    _EBattOverVolProtectionMod12_Type()
)
eBattOverVolProtectionMod12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod12.setStatus("current")


class _EBattOverVolProtectionMod13_Type(Integer32):
    """Custom type eBattOverVolProtectionMod13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod13_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod13_Object = MibScalar
eBattOverVolProtectionMod13 = _EBattOverVolProtectionMod13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 178),
    _EBattOverVolProtectionMod13_Type()
)
eBattOverVolProtectionMod13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod13.setStatus("current")


class _EBattOverVolProtectionMod14_Type(Integer32):
    """Custom type eBattOverVolProtectionMod14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod14_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod14_Object = MibScalar
eBattOverVolProtectionMod14 = _EBattOverVolProtectionMod14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 179),
    _EBattOverVolProtectionMod14_Type()
)
eBattOverVolProtectionMod14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod14.setStatus("current")


class _EBattOverVolProtectionMod15_Type(Integer32):
    """Custom type eBattOverVolProtectionMod15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBattOverVolProtectionMod15_Type.__name__ = "Integer32"
_EBattOverVolProtectionMod15_Object = MibScalar
eBattOverVolProtectionMod15 = _EBattOverVolProtectionMod15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 180),
    _EBattOverVolProtectionMod15_Type()
)
eBattOverVolProtectionMod15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBattOverVolProtectionMod15.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 181),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 182),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 183),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 184),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 185),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 186),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 187),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 188),
    _EModule7Isolated_Type()
)
eModule7Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule7Isolated.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 189),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 190),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 191),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 192),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 193),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 194),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 195),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 196),
    _EModule15Isolated_Type()
)
eModule15Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule15Isolated.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 197),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 198),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 199),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 200),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 201),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 202),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 203),
    _EModule7CommFailAlarm_Type()
)
eModule7CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule7CommFailAlarm.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 204),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 205),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 206),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 207),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 208),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 209),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 210),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 211),
    _EModule15CommFailAlarm_Type()
)
eModule15CommFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModule15CommFailAlarm.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 212),
    _EACPowerfail_Type()
)
eACPowerfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eACPowerfail.setStatus("current")


class _ESingleRectifierModuleFail_Type(Integer32):
    """Custom type eSingleRectifierModuleFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESingleRectifierModuleFail_Type.__name__ = "Integer32"
_ESingleRectifierModuleFail_Object = MibScalar
eSingleRectifierModuleFail = _ESingleRectifierModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 213),
    _ESingleRectifierModuleFail_Type()
)
eSingleRectifierModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSingleRectifierModuleFail.setStatus("current")


class _EMultipleRectifierModuleFail_Type(Integer32):
    """Custom type eMultipleRectifierModuleFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMultipleRectifierModuleFail_Type.__name__ = "Integer32"
_EMultipleRectifierModuleFail_Object = MibScalar
eMultipleRectifierModuleFail = _EMultipleRectifierModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 214),
    _EMultipleRectifierModuleFail_Type()
)
eMultipleRectifierModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMultipleRectifierModuleFail.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 215),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 216),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 217),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 218),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 219),
    _EBatteryonLoad_Type()
)
eBatteryonLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryonLoad.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 220),
    _EFireAlarm_Type()
)
eFireAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFireAlarm.setStatus("current")


class _EUPS1Faulty_Type(Integer32):
    """Custom type eUPS1Faulty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EUPS1Faulty_Type.__name__ = "Integer32"
_EUPS1Faulty_Object = MibScalar
eUPS1Faulty = _EUPS1Faulty_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 221),
    _EUPS1Faulty_Type()
)
eUPS1Faulty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUPS1Faulty.setStatus("current")


class _EUPS1OnBypass_Type(Integer32):
    """Custom type eUPS1OnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EUPS1OnBypass_Type.__name__ = "Integer32"
_EUPS1OnBypass_Object = MibScalar
eUPS1OnBypass = _EUPS1OnBypass_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 222),
    _EUPS1OnBypass_Type()
)
eUPS1OnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUPS1OnBypass.setStatus("current")


class _EUPS2Faulty_Type(Integer32):
    """Custom type eUPS2Faulty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EUPS2Faulty_Type.__name__ = "Integer32"
_EUPS2Faulty_Object = MibScalar
eUPS2Faulty = _EUPS2Faulty_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 223),
    _EUPS2Faulty_Type()
)
eUPS2Faulty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUPS2Faulty.setStatus("current")


class _EUPS2OnBypass_Type(Integer32):
    """Custom type eUPS2OnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EUPS2OnBypass_Type.__name__ = "Integer32"
_EUPS2OnBypass_Object = MibScalar
eUPS2OnBypass = _EUPS2OnBypass_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 224),
    _EUPS2OnBypass_Type()
)
eUPS2OnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUPS2OnBypass.setStatus("current")


class _EHighTempAlarm_Type(Integer32):
    """Custom type eHighTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighTempAlarm_Type.__name__ = "Integer32"
_EHighTempAlarm_Object = MibScalar
eHighTempAlarm = _EHighTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 1, 1, 225),
    _EHighTempAlarm_Type()
)
eHighTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighTempAlarm.setStatus("current")
_EParameters_ObjectIdentity = ObjectIdentity
eParameters = _EParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2)
)
_ECurrentInfo_ObjectIdentity = ObjectIdentity
eCurrentInfo = _ECurrentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1)
)
_EChargingCurrentModule1_Type = DisplayString
_EChargingCurrentModule1_Object = MibScalar
eChargingCurrentModule1 = _EChargingCurrentModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 1),
    _EChargingCurrentModule1_Type()
)
eChargingCurrentModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule1.setStatus("current")
_EChargingCurrentModule2_Type = DisplayString
_EChargingCurrentModule2_Object = MibScalar
eChargingCurrentModule2 = _EChargingCurrentModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 2),
    _EChargingCurrentModule2_Type()
)
eChargingCurrentModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule2.setStatus("current")
_EChargingCurrentModule3_Type = DisplayString
_EChargingCurrentModule3_Object = MibScalar
eChargingCurrentModule3 = _EChargingCurrentModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 3),
    _EChargingCurrentModule3_Type()
)
eChargingCurrentModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule3.setStatus("current")
_EChargingCurrentModule4_Type = DisplayString
_EChargingCurrentModule4_Object = MibScalar
eChargingCurrentModule4 = _EChargingCurrentModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 4),
    _EChargingCurrentModule4_Type()
)
eChargingCurrentModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule4.setStatus("current")
_EChargingCurrentModule5_Type = DisplayString
_EChargingCurrentModule5_Object = MibScalar
eChargingCurrentModule5 = _EChargingCurrentModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 5),
    _EChargingCurrentModule5_Type()
)
eChargingCurrentModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule5.setStatus("current")
_EChargingCurrentModule6_Type = DisplayString
_EChargingCurrentModule6_Object = MibScalar
eChargingCurrentModule6 = _EChargingCurrentModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 6),
    _EChargingCurrentModule6_Type()
)
eChargingCurrentModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule6.setStatus("current")
_EChargingCurrentModule7_Type = DisplayString
_EChargingCurrentModule7_Object = MibScalar
eChargingCurrentModule7 = _EChargingCurrentModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 7),
    _EChargingCurrentModule7_Type()
)
eChargingCurrentModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule7.setStatus("current")
_EChargingCurrentModule8_Type = DisplayString
_EChargingCurrentModule8_Object = MibScalar
eChargingCurrentModule8 = _EChargingCurrentModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 8),
    _EChargingCurrentModule8_Type()
)
eChargingCurrentModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule8.setStatus("current")
_EChargingCurrentModule9_Type = DisplayString
_EChargingCurrentModule9_Object = MibScalar
eChargingCurrentModule9 = _EChargingCurrentModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 9),
    _EChargingCurrentModule9_Type()
)
eChargingCurrentModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule9.setStatus("current")
_EChargingCurrentModule10_Type = DisplayString
_EChargingCurrentModule10_Object = MibScalar
eChargingCurrentModule10 = _EChargingCurrentModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 10),
    _EChargingCurrentModule10_Type()
)
eChargingCurrentModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule10.setStatus("current")
_EChargingCurrentModule11_Type = DisplayString
_EChargingCurrentModule11_Object = MibScalar
eChargingCurrentModule11 = _EChargingCurrentModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 11),
    _EChargingCurrentModule11_Type()
)
eChargingCurrentModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule11.setStatus("current")
_EChargingCurrentModule12_Type = DisplayString
_EChargingCurrentModule12_Object = MibScalar
eChargingCurrentModule12 = _EChargingCurrentModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 12),
    _EChargingCurrentModule12_Type()
)
eChargingCurrentModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule12.setStatus("current")
_EChargingCurrentModule13_Type = DisplayString
_EChargingCurrentModule13_Object = MibScalar
eChargingCurrentModule13 = _EChargingCurrentModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 13),
    _EChargingCurrentModule13_Type()
)
eChargingCurrentModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule13.setStatus("current")
_EChargingCurrentModule14_Type = DisplayString
_EChargingCurrentModule14_Object = MibScalar
eChargingCurrentModule14 = _EChargingCurrentModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 14),
    _EChargingCurrentModule14_Type()
)
eChargingCurrentModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule14.setStatus("current")
_EChargingCurrentModule15_Type = DisplayString
_EChargingCurrentModule15_Object = MibScalar
eChargingCurrentModule15 = _EChargingCurrentModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 1, 15),
    _EChargingCurrentModule15_Type()
)
eChargingCurrentModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingCurrentModule15.setStatus("current")
_ESOCInfo_ObjectIdentity = ObjectIdentity
eSOCInfo = _ESOCInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2)
)
_ESOCModule1_Type = DisplayString
_ESOCModule1_Object = MibScalar
eSOCModule1 = _ESOCModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 1),
    _ESOCModule1_Type()
)
eSOCModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule1.setStatus("current")
_ESOCModule2_Type = DisplayString
_ESOCModule2_Object = MibScalar
eSOCModule2 = _ESOCModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 2),
    _ESOCModule2_Type()
)
eSOCModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule2.setStatus("current")
_ESOCModule3_Type = DisplayString
_ESOCModule3_Object = MibScalar
eSOCModule3 = _ESOCModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 3),
    _ESOCModule3_Type()
)
eSOCModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule3.setStatus("current")
_ESOCModule4_Type = DisplayString
_ESOCModule4_Object = MibScalar
eSOCModule4 = _ESOCModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 4),
    _ESOCModule4_Type()
)
eSOCModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule4.setStatus("current")
_ESOCModule5_Type = DisplayString
_ESOCModule5_Object = MibScalar
eSOCModule5 = _ESOCModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 5),
    _ESOCModule5_Type()
)
eSOCModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule5.setStatus("current")
_ESOCModule6_Type = DisplayString
_ESOCModule6_Object = MibScalar
eSOCModule6 = _ESOCModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 6),
    _ESOCModule6_Type()
)
eSOCModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule6.setStatus("current")
_ESOCModule7_Type = DisplayString
_ESOCModule7_Object = MibScalar
eSOCModule7 = _ESOCModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 7),
    _ESOCModule7_Type()
)
eSOCModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule7.setStatus("current")
_ESOCModule8_Type = DisplayString
_ESOCModule8_Object = MibScalar
eSOCModule8 = _ESOCModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 8),
    _ESOCModule8_Type()
)
eSOCModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule8.setStatus("current")
_ESOCModule9_Type = DisplayString
_ESOCModule9_Object = MibScalar
eSOCModule9 = _ESOCModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 9),
    _ESOCModule9_Type()
)
eSOCModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule9.setStatus("current")
_ESOCModule10_Type = DisplayString
_ESOCModule10_Object = MibScalar
eSOCModule10 = _ESOCModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 10),
    _ESOCModule10_Type()
)
eSOCModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule10.setStatus("current")
_ESOCModule11_Type = DisplayString
_ESOCModule11_Object = MibScalar
eSOCModule11 = _ESOCModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 11),
    _ESOCModule11_Type()
)
eSOCModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule11.setStatus("current")
_ESOCModule12_Type = DisplayString
_ESOCModule12_Object = MibScalar
eSOCModule12 = _ESOCModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 12),
    _ESOCModule12_Type()
)
eSOCModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule12.setStatus("current")
_ESOCModule13_Type = DisplayString
_ESOCModule13_Object = MibScalar
eSOCModule13 = _ESOCModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 13),
    _ESOCModule13_Type()
)
eSOCModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule13.setStatus("current")
_ESOCModule14_Type = DisplayString
_ESOCModule14_Object = MibScalar
eSOCModule14 = _ESOCModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 14),
    _ESOCModule14_Type()
)
eSOCModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule14.setStatus("current")
_ESOCModule15_Type = DisplayString
_ESOCModule15_Object = MibScalar
eSOCModule15 = _ESOCModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 2, 15),
    _ESOCModule15_Type()
)
eSOCModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOCModule15.setStatus("current")
_ESOHInfo_ObjectIdentity = ObjectIdentity
eSOHInfo = _ESOHInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3)
)
_ESOHModule1_Type = DisplayString
_ESOHModule1_Object = MibScalar
eSOHModule1 = _ESOHModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 1),
    _ESOHModule1_Type()
)
eSOHModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule1.setStatus("current")
_ESOHModule2_Type = DisplayString
_ESOHModule2_Object = MibScalar
eSOHModule2 = _ESOHModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 2),
    _ESOHModule2_Type()
)
eSOHModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule2.setStatus("current")
_ESOHModule3_Type = DisplayString
_ESOHModule3_Object = MibScalar
eSOHModule3 = _ESOHModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 3),
    _ESOHModule3_Type()
)
eSOHModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule3.setStatus("current")
_ESOHModule4_Type = DisplayString
_ESOHModule4_Object = MibScalar
eSOHModule4 = _ESOHModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 4),
    _ESOHModule4_Type()
)
eSOHModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule4.setStatus("current")
_ESOHModule5_Type = DisplayString
_ESOHModule5_Object = MibScalar
eSOHModule5 = _ESOHModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 5),
    _ESOHModule5_Type()
)
eSOHModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule5.setStatus("current")
_ESOHModule6_Type = DisplayString
_ESOHModule6_Object = MibScalar
eSOHModule6 = _ESOHModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 6),
    _ESOHModule6_Type()
)
eSOHModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule6.setStatus("current")
_ESOHModule7_Type = DisplayString
_ESOHModule7_Object = MibScalar
eSOHModule7 = _ESOHModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 7),
    _ESOHModule7_Type()
)
eSOHModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule7.setStatus("current")
_ESOHModule8_Type = DisplayString
_ESOHModule8_Object = MibScalar
eSOHModule8 = _ESOHModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 8),
    _ESOHModule8_Type()
)
eSOHModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule8.setStatus("current")
_ESOHModule9_Type = DisplayString
_ESOHModule9_Object = MibScalar
eSOHModule9 = _ESOHModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 9),
    _ESOHModule9_Type()
)
eSOHModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule9.setStatus("current")
_ESOHModule10_Type = DisplayString
_ESOHModule10_Object = MibScalar
eSOHModule10 = _ESOHModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 10),
    _ESOHModule10_Type()
)
eSOHModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule10.setStatus("current")
_ESOHModule11_Type = DisplayString
_ESOHModule11_Object = MibScalar
eSOHModule11 = _ESOHModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 11),
    _ESOHModule11_Type()
)
eSOHModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule11.setStatus("current")
_ESOHModule12_Type = DisplayString
_ESOHModule12_Object = MibScalar
eSOHModule12 = _ESOHModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 12),
    _ESOHModule12_Type()
)
eSOHModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule12.setStatus("current")
_ESOHModule13_Type = DisplayString
_ESOHModule13_Object = MibScalar
eSOHModule13 = _ESOHModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 13),
    _ESOHModule13_Type()
)
eSOHModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule13.setStatus("current")
_ESOHModule14_Type = DisplayString
_ESOHModule14_Object = MibScalar
eSOHModule14 = _ESOHModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 14),
    _ESOHModule14_Type()
)
eSOHModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule14.setStatus("current")
_ESOHModule15_Type = DisplayString
_ESOHModule15_Object = MibScalar
eSOHModule15 = _ESOHModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 3, 15),
    _ESOHModule15_Type()
)
eSOHModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSOHModule15.setStatus("current")
_EBattMaxCurrInfo_ObjectIdentity = ObjectIdentity
eBattMaxCurrInfo = _EBattMaxCurrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4)
)
_EBatteryMaxTempModule1_Type = DisplayString
_EBatteryMaxTempModule1_Object = MibScalar
eBatteryMaxTempModule1 = _EBatteryMaxTempModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 1),
    _EBatteryMaxTempModule1_Type()
)
eBatteryMaxTempModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule1.setStatus("current")
_EBatteryMaxTempModule2_Type = DisplayString
_EBatteryMaxTempModule2_Object = MibScalar
eBatteryMaxTempModule2 = _EBatteryMaxTempModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 2),
    _EBatteryMaxTempModule2_Type()
)
eBatteryMaxTempModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule2.setStatus("current")
_EBatteryMaxTempModule3_Type = DisplayString
_EBatteryMaxTempModule3_Object = MibScalar
eBatteryMaxTempModule3 = _EBatteryMaxTempModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 3),
    _EBatteryMaxTempModule3_Type()
)
eBatteryMaxTempModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule3.setStatus("current")
_EBatteryMaxTempModule4_Type = DisplayString
_EBatteryMaxTempModule4_Object = MibScalar
eBatteryMaxTempModule4 = _EBatteryMaxTempModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 4),
    _EBatteryMaxTempModule4_Type()
)
eBatteryMaxTempModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule4.setStatus("current")
_EBatteryMaxTempModule5_Type = DisplayString
_EBatteryMaxTempModule5_Object = MibScalar
eBatteryMaxTempModule5 = _EBatteryMaxTempModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 5),
    _EBatteryMaxTempModule5_Type()
)
eBatteryMaxTempModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule5.setStatus("current")
_EBatteryMaxTempModule6_Type = DisplayString
_EBatteryMaxTempModule6_Object = MibScalar
eBatteryMaxTempModule6 = _EBatteryMaxTempModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 6),
    _EBatteryMaxTempModule6_Type()
)
eBatteryMaxTempModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule6.setStatus("current")
_EBatteryMaxTempModule7_Type = DisplayString
_EBatteryMaxTempModule7_Object = MibScalar
eBatteryMaxTempModule7 = _EBatteryMaxTempModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 7),
    _EBatteryMaxTempModule7_Type()
)
eBatteryMaxTempModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule7.setStatus("current")
_EBatteryMaxTempModule8_Type = DisplayString
_EBatteryMaxTempModule8_Object = MibScalar
eBatteryMaxTempModule8 = _EBatteryMaxTempModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 8),
    _EBatteryMaxTempModule8_Type()
)
eBatteryMaxTempModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule8.setStatus("current")
_EBatteryMaxTempModule9_Type = DisplayString
_EBatteryMaxTempModule9_Object = MibScalar
eBatteryMaxTempModule9 = _EBatteryMaxTempModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 9),
    _EBatteryMaxTempModule9_Type()
)
eBatteryMaxTempModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule9.setStatus("current")
_EBatteryMaxTempModule10_Type = DisplayString
_EBatteryMaxTempModule10_Object = MibScalar
eBatteryMaxTempModule10 = _EBatteryMaxTempModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 10),
    _EBatteryMaxTempModule10_Type()
)
eBatteryMaxTempModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule10.setStatus("current")
_EBatteryMaxTempModule11_Type = DisplayString
_EBatteryMaxTempModule11_Object = MibScalar
eBatteryMaxTempModule11 = _EBatteryMaxTempModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 11),
    _EBatteryMaxTempModule11_Type()
)
eBatteryMaxTempModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule11.setStatus("current")
_EBatteryMaxTempModule12_Type = DisplayString
_EBatteryMaxTempModule12_Object = MibScalar
eBatteryMaxTempModule12 = _EBatteryMaxTempModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 12),
    _EBatteryMaxTempModule12_Type()
)
eBatteryMaxTempModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule12.setStatus("current")
_EBatteryMaxTempModule13_Type = DisplayString
_EBatteryMaxTempModule13_Object = MibScalar
eBatteryMaxTempModule13 = _EBatteryMaxTempModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 13),
    _EBatteryMaxTempModule13_Type()
)
eBatteryMaxTempModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule13.setStatus("current")
_EBatteryMaxTempModule14_Type = DisplayString
_EBatteryMaxTempModule14_Object = MibScalar
eBatteryMaxTempModule14 = _EBatteryMaxTempModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 14),
    _EBatteryMaxTempModule14_Type()
)
eBatteryMaxTempModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule14.setStatus("current")
_EBatteryMaxTempModule15_Type = DisplayString
_EBatteryMaxTempModule15_Object = MibScalar
eBatteryMaxTempModule15 = _EBatteryMaxTempModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 4, 15),
    _EBatteryMaxTempModule15_Type()
)
eBatteryMaxTempModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryMaxTempModule15.setStatus("current")
_EVoltageInfo_ObjectIdentity = ObjectIdentity
eVoltageInfo = _EVoltageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5)
)
_EModuleVoltageModule1_Type = DisplayString
_EModuleVoltageModule1_Object = MibScalar
eModuleVoltageModule1 = _EModuleVoltageModule1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 1),
    _EModuleVoltageModule1_Type()
)
eModuleVoltageModule1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule1.setStatus("current")
_EModuleVoltageModule2_Type = DisplayString
_EModuleVoltageModule2_Object = MibScalar
eModuleVoltageModule2 = _EModuleVoltageModule2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 2),
    _EModuleVoltageModule2_Type()
)
eModuleVoltageModule2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule2.setStatus("current")
_EModuleVoltageModule3_Type = DisplayString
_EModuleVoltageModule3_Object = MibScalar
eModuleVoltageModule3 = _EModuleVoltageModule3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 3),
    _EModuleVoltageModule3_Type()
)
eModuleVoltageModule3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule3.setStatus("current")
_EModuleVoltageModule4_Type = DisplayString
_EModuleVoltageModule4_Object = MibScalar
eModuleVoltageModule4 = _EModuleVoltageModule4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 4),
    _EModuleVoltageModule4_Type()
)
eModuleVoltageModule4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule4.setStatus("current")
_EModuleVoltageModule5_Type = DisplayString
_EModuleVoltageModule5_Object = MibScalar
eModuleVoltageModule5 = _EModuleVoltageModule5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 5),
    _EModuleVoltageModule5_Type()
)
eModuleVoltageModule5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule5.setStatus("current")
_EModuleVoltageModule6_Type = DisplayString
_EModuleVoltageModule6_Object = MibScalar
eModuleVoltageModule6 = _EModuleVoltageModule6_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 6),
    _EModuleVoltageModule6_Type()
)
eModuleVoltageModule6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule6.setStatus("current")
_EModuleVoltageModule7_Type = DisplayString
_EModuleVoltageModule7_Object = MibScalar
eModuleVoltageModule7 = _EModuleVoltageModule7_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 7),
    _EModuleVoltageModule7_Type()
)
eModuleVoltageModule7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule7.setStatus("current")
_EModuleVoltageModule8_Type = DisplayString
_EModuleVoltageModule8_Object = MibScalar
eModuleVoltageModule8 = _EModuleVoltageModule8_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 8),
    _EModuleVoltageModule8_Type()
)
eModuleVoltageModule8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule8.setStatus("current")
_EModuleVoltageModule9_Type = DisplayString
_EModuleVoltageModule9_Object = MibScalar
eModuleVoltageModule9 = _EModuleVoltageModule9_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 9),
    _EModuleVoltageModule9_Type()
)
eModuleVoltageModule9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule9.setStatus("current")
_EModuleVoltageModule10_Type = DisplayString
_EModuleVoltageModule10_Object = MibScalar
eModuleVoltageModule10 = _EModuleVoltageModule10_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 10),
    _EModuleVoltageModule10_Type()
)
eModuleVoltageModule10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule10.setStatus("current")
_EModuleVoltageModule11_Type = DisplayString
_EModuleVoltageModule11_Object = MibScalar
eModuleVoltageModule11 = _EModuleVoltageModule11_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 11),
    _EModuleVoltageModule11_Type()
)
eModuleVoltageModule11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule11.setStatus("current")
_EModuleVoltageModule12_Type = DisplayString
_EModuleVoltageModule12_Object = MibScalar
eModuleVoltageModule12 = _EModuleVoltageModule12_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 12),
    _EModuleVoltageModule12_Type()
)
eModuleVoltageModule12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule12.setStatus("current")
_EModuleVoltageModule13_Type = DisplayString
_EModuleVoltageModule13_Object = MibScalar
eModuleVoltageModule13 = _EModuleVoltageModule13_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 13),
    _EModuleVoltageModule13_Type()
)
eModuleVoltageModule13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule13.setStatus("current")
_EModuleVoltageModule14_Type = DisplayString
_EModuleVoltageModule14_Object = MibScalar
eModuleVoltageModule14 = _EModuleVoltageModule14_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 14),
    _EModuleVoltageModule14_Type()
)
eModuleVoltageModule14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule14.setStatus("current")
_EModuleVoltageModule15_Type = DisplayString
_EModuleVoltageModule15_Object = MibScalar
eModuleVoltageModule15 = _EModuleVoltageModule15_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 5, 15),
    _EModuleVoltageModule15_Type()
)
eModuleVoltageModule15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleVoltageModule15.setStatus("current")
_ESystemInfo_ObjectIdentity = ObjectIdentity
eSystemInfo = _ESystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 6)
)
_EManufacturerName_Type = DisplayString
_EManufacturerName_Object = MibScalar
eManufacturerName = _EManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 6, 1),
    _EManufacturerName_Type()
)
eManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eManufacturerName.setStatus("current")
_EPartNo_Type = DisplayString
_EPartNo_Object = MibScalar
ePartNo = _EPartNo_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 6, 2),
    _EPartNo_Type()
)
ePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePartNo.setStatus("current")
_ESrNo_Type = DisplayString
_ESrNo_Object = MibScalar
eSrNo = _ESrNo_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 6, 3),
    _ESrNo_Type()
)
eSrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSrNo.setStatus("current")
_EDesignCapacity_Type = DisplayString
_EDesignCapacity_Object = MibScalar
eDesignCapacity = _EDesignCapacity_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 6, 4),
    _EDesignCapacity_Type()
)
eDesignCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDesignCapacity.setStatus("current")
_EMaxChargeCurrInfo_ObjectIdentity = ObjectIdentity
eMaxChargeCurrInfo = _EMaxChargeCurrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 7)
)
_EModuleMaxChargeCurrentLimit_Type = DisplayString
_EModuleMaxChargeCurrentLimit_Object = MibScalar
eModuleMaxChargeCurrentLimit = _EModuleMaxChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 7, 1),
    _EModuleMaxChargeCurrentLimit_Type()
)
eModuleMaxChargeCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModuleMaxChargeCurrentLimit.setStatus("current")
_EInstMaxModuleCurrentInfo_ObjectIdentity = ObjectIdentity
eInstMaxModuleCurrentInfo = _EInstMaxModuleCurrentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 8)
)
_EInstantaneousMaxModuleCurrent_Type = DisplayString
_EInstantaneousMaxModuleCurrent_Object = MibScalar
eInstantaneousMaxModuleCurrent = _EInstantaneousMaxModuleCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 8, 1),
    _EInstantaneousMaxModuleCurrent_Type()
)
eInstantaneousMaxModuleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInstantaneousMaxModuleCurrent.setStatus("current")
_ESMPSInfo_ObjectIdentity = ObjectIdentity
eSMPSInfo = _ESMPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9)
)
_EDCVoltage_Type = DisplayString
_EDCVoltage_Object = MibScalar
eDCVoltage = _EDCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 1),
    _EDCVoltage_Type()
)
eDCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCVoltage.setStatus("current")
_EDCCurrent_Type = DisplayString
_EDCCurrent_Object = MibScalar
eDCCurrent = _EDCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 2),
    _EDCCurrent_Type()
)
eDCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCCurrent.setStatus("current")
_EDCKWH_Type = DisplayString
_EDCKWH_Object = MibScalar
eDCKWH = _EDCKWH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 3),
    _EDCKWH_Type()
)
eDCKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCKWH.setStatus("current")
_ELoadcurrent_Type = DisplayString
_ELoadcurrent_Object = MibScalar
eLoadcurrent = _ELoadcurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 4),
    _ELoadcurrent_Type()
)
eLoadcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadcurrent.setStatus("current")
_EBatteryCurrent_Type = DisplayString
_EBatteryCurrent_Object = MibScalar
eBatteryCurrent = _EBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 5),
    _EBatteryCurrent_Type()
)
eBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCurrent.setStatus("current")
_ENoOfRectifiersPoweredUp_Type = DisplayString
_ENoOfRectifiersPoweredUp_Object = MibScalar
eNoOfRectifiersPoweredUp = _ENoOfRectifiersPoweredUp_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 6),
    _ENoOfRectifiersPoweredUp_Type()
)
eNoOfRectifiersPoweredUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNoOfRectifiersPoweredUp.setStatus("current")
_ESMPSManufacturerName_Type = DisplayString
_ESMPSManufacturerName_Object = MibScalar
eSMPSManufacturerName = _ESMPSManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 7),
    _ESMPSManufacturerName_Type()
)
eSMPSManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMPSManufacturerName.setStatus("current")
_EControllerModel_Type = DisplayString
_EControllerModel_Object = MibScalar
eControllerModel = _EControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 8),
    _EControllerModel_Type()
)
eControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eControllerModel.setStatus("current")
_ESMPSFirmwareVersion_Type = DisplayString
_ESMPSFirmwareVersion_Object = MibScalar
eSMPSFirmwareVersion = _ESMPSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 9),
    _ESMPSFirmwareVersion_Type()
)
eSMPSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMPSFirmwareVersion.setStatus("current")
_ESMPSPartNo_Type = DisplayString
_ESMPSPartNo_Object = MibScalar
eSMPSPartNo = _ESMPSPartNo_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 10),
    _ESMPSPartNo_Type()
)
eSMPSPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSMPSPartNo.setStatus("current")
_EInputLineAVoltage_Type = DisplayString
_EInputLineAVoltage_Object = MibScalar
eInputLineAVoltage = _EInputLineAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 11),
    _EInputLineAVoltage_Type()
)
eInputLineAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineAVoltage.setStatus("current")
_EInputLineBVoltage_Type = DisplayString
_EInputLineBVoltage_Object = MibScalar
eInputLineBVoltage = _EInputLineBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 12),
    _EInputLineBVoltage_Type()
)
eInputLineBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineBVoltage.setStatus("current")
_EInputLineCVoltage_Type = DisplayString
_EInputLineCVoltage_Object = MibScalar
eInputLineCVoltage = _EInputLineCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 13),
    _EInputLineCVoltage_Type()
)
eInputLineCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineCVoltage.setStatus("current")
_EInputLineACurrent_Type = DisplayString
_EInputLineACurrent_Object = MibScalar
eInputLineACurrent = _EInputLineACurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 14),
    _EInputLineACurrent_Type()
)
eInputLineACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineACurrent.setStatus("current")
_EInputLineBCurrent_Type = DisplayString
_EInputLineBCurrent_Object = MibScalar
eInputLineBCurrent = _EInputLineBCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 15),
    _EInputLineBCurrent_Type()
)
eInputLineBCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineBCurrent.setStatus("current")
_EInputLineCCurrent_Type = DisplayString
_EInputLineCCurrent_Object = MibScalar
eInputLineCCurrent = _EInputLineCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 16),
    _EInputLineCCurrent_Type()
)
eInputLineCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineCCurrent.setStatus("current")
_EMainsSource1KWh_Type = DisplayString
_EMainsSource1KWh_Object = MibScalar
eMainsSource1KWh = _EMainsSource1KWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 17),
    _EMainsSource1KWh_Type()
)
eMainsSource1KWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsSource1KWh.setStatus("current")
_EMainsCumulativeRunHrs_Type = DisplayString
_EMainsCumulativeRunHrs_Object = MibScalar
eMainsCumulativeRunHrs = _EMainsCumulativeRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 18),
    _EMainsCumulativeRunHrs_Type()
)
eMainsCumulativeRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsCumulativeRunHrs.setStatus("current")
_EBatteryCumulativeKWh_Type = DisplayString
_EBatteryCumulativeKWh_Object = MibScalar
eBatteryCumulativeKWh = _EBatteryCumulativeKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 19),
    _EBatteryCumulativeKWh_Type()
)
eBatteryCumulativeKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCumulativeKWh.setStatus("current")
_EBatteryCumulativeRunHrs_Type = DisplayString
_EBatteryCumulativeRunHrs_Object = MibScalar
eBatteryCumulativeRunHrs = _EBatteryCumulativeRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 20),
    _EBatteryCumulativeRunHrs_Type()
)
eBatteryCumulativeRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCumulativeRunHrs.setStatus("current")
_EMainsSource2KWh_Type = DisplayString
_EMainsSource2KWh_Object = MibScalar
eMainsSource2KWh = _EMainsSource2KWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 21),
    _EMainsSource2KWh_Type()
)
eMainsSource2KWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsSource2KWh.setStatus("current")
_EDCOutputPower_Type = DisplayString
_EDCOutputPower_Object = MibScalar
eDCOutputPower = _EDCOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 22),
    _EDCOutputPower_Type()
)
eDCOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCOutputPower.setStatus("current")
_ELoadCumulativeKWh_Type = DisplayString
_ELoadCumulativeKWh_Object = MibScalar
eLoadCumulativeKWh = _ELoadCumulativeKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 9, 23),
    _ELoadCumulativeKWh_Type()
)
eLoadCumulativeKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadCumulativeKWh.setStatus("current")
_ESettingInfo_ObjectIdentity = ObjectIdentity
eSettingInfo = _ESettingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10)
)
_EFloatVoltage_Type = DisplayString
_EFloatVoltage_Object = MibScalar
eFloatVoltage = _EFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10, 1),
    _EFloatVoltage_Type()
)
eFloatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFloatVoltage.setStatus("current")
_EBoostVoltage_Type = DisplayString
_EBoostVoltage_Object = MibScalar
eBoostVoltage = _EBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10, 2),
    _EBoostVoltage_Type()
)
eBoostVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBoostVoltage.setStatus("current")
_EChargeCurrentLimit_Type = DisplayString
_EChargeCurrentLimit_Object = MibScalar
eChargeCurrentLimit = _EChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10, 3),
    _EChargeCurrentLimit_Type()
)
eChargeCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargeCurrentLimit.setStatus("current")
_ELLVDVoltage_Type = DisplayString
_ELLVDVoltage_Object = MibScalar
eLLVDVoltage = _ELLVDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10, 4),
    _ELLVDVoltage_Type()
)
eLLVDVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLLVDVoltage.setStatus("current")
_EBLVDVoltage_Type = DisplayString
_EBLVDVoltage_Object = MibScalar
eBLVDVoltage = _EBLVDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10, 5),
    _EBLVDVoltage_Type()
)
eBLVDVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBLVDVoltage.setStatus("current")
_EAmbientHighTempThreshold_Type = DisplayString
_EAmbientHighTempThreshold_Object = MibScalar
eAmbientHighTempThreshold = _EAmbientHighTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 3, 2, 10, 6),
    _EAmbientHighTempThreshold_Type()
)
eAmbientHighTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAmbientHighTempThreshold.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11)
)
_Internaltraps_ObjectIdentity = ObjectIdentity
internaltraps = _Internaltraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 1)
)
_Internalparams_ObjectIdentity = ObjectIdentity
internalparams = _Internalparams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 2)
)
_ESystemResetCause_Type = Integer32
_ESystemResetCause_Object = MibScalar
eSystemResetCause = _ESystemResetCause_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 2, 1),
    _ESystemResetCause_Type()
)
eSystemResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSystemResetCause.setStatus("current")
_EPeriodicTrap_Type = Integer32
_EPeriodicTrap_Object = MibScalar
ePeriodicTrap = _EPeriodicTrap_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 2, 2),
    _EPeriodicTrap_Type()
)
ePeriodicTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePeriodicTrap.setStatus("current")
_EGenericTrap_Type = Integer32
_EGenericTrap_Object = MibScalar
eGenericTrap = _EGenericTrap_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 2, 3),
    _EGenericTrap_Type()
)
eGenericTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGenericTrap.setStatus("current")
_Devicestatus_ObjectIdentity = ObjectIdentity
devicestatus = _Devicestatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 3)
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 3, 1),
    _ECommFailPCtoSMPS_Type()
)
eCommFailPCtoSMPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailPCtoSMPS.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 12)
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 12, 1),
    _CTrapResendFlag_Type()
)
cTrapResendFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTrapResendFlag.setStatus("current")

# Managed Objects groups


# Notification objects

tpCellOverVolProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 1)
)
tpCellOverVolProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod1.setStatus(
        "current"
    )

tpCellOverVolProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 2)
)
tpCellOverVolProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod2.setStatus(
        "current"
    )

tpCellOverVolProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 3)
)
tpCellOverVolProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod3.setStatus(
        "current"
    )

tpCellOverVolProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 4)
)
tpCellOverVolProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod4.setStatus(
        "current"
    )

tpCellOverVolProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 5)
)
tpCellOverVolProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod5.setStatus(
        "current"
    )

tpCellOverVolProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 6)
)
tpCellOverVolProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod6.setStatus(
        "current"
    )

tpCellOverVolProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 7)
)
tpCellOverVolProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod7.setStatus(
        "current"
    )

tpCellOverVolProtectionMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 8)
)
tpCellOverVolProtectionMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod8"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod8.setStatus(
        "current"
    )

tpCellOverVolProtectionMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 9)
)
tpCellOverVolProtectionMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod9"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod9.setStatus(
        "current"
    )

tpCellOverVolProtectionMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 10)
)
tpCellOverVolProtectionMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod10"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod10.setStatus(
        "current"
    )

tpCellOverVolProtectionMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 11)
)
tpCellOverVolProtectionMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod11"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod11.setStatus(
        "current"
    )

tpCellOverVolProtectionMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 12)
)
tpCellOverVolProtectionMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod12"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod12.setStatus(
        "current"
    )

tpCellOverVolProtectionMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 13)
)
tpCellOverVolProtectionMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod13"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod13.setStatus(
        "current"
    )

tpCellOverVolProtectionMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 14)
)
tpCellOverVolProtectionMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod14"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod14.setStatus(
        "current"
    )

tpCellOverVolProtectionMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 15)
)
tpCellOverVolProtectionMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellOverVolProtectionMod15"))
)
if mibBuilder.loadTexts:
    tpCellOverVolProtectionMod15.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 16)
)
tpCellUnderVolProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod1.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 17)
)
tpCellUnderVolProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod2.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 18)
)
tpCellUnderVolProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod3.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 19)
)
tpCellUnderVolProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod4.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 20)
)
tpCellUnderVolProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod5.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 21)
)
tpCellUnderVolProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod6.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 22)
)
tpCellUnderVolProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod7.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 23)
)
tpCellUnderVolProtectionMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod8"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod8.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 24)
)
tpCellUnderVolProtectionMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod9"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod9.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 25)
)
tpCellUnderVolProtectionMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod10"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod10.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 26)
)
tpCellUnderVolProtectionMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod11"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod11.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 27)
)
tpCellUnderVolProtectionMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod12"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod12.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 28)
)
tpCellUnderVolProtectionMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod13"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod13.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 29)
)
tpCellUnderVolProtectionMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod14"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod14.setStatus(
        "current"
    )

tpCellUnderVolProtectionMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 30)
)
tpCellUnderVolProtectionMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellUnderVolProtectionMod15"))
)
if mibBuilder.loadTexts:
    tpCellUnderVolProtectionMod15.setStatus(
        "current"
    )

tpBattUnderVolWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 31)
)
tpBattUnderVolWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod1.setStatus(
        "current"
    )

tpBattUnderVolWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 32)
)
tpBattUnderVolWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod2.setStatus(
        "current"
    )

tpBattUnderVolWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 33)
)
tpBattUnderVolWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod3.setStatus(
        "current"
    )

tpBattUnderVolWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 34)
)
tpBattUnderVolWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod4.setStatus(
        "current"
    )

tpBattUnderVolWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 35)
)
tpBattUnderVolWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod5.setStatus(
        "current"
    )

tpBattUnderVolWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 36)
)
tpBattUnderVolWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod6.setStatus(
        "current"
    )

tpBattUnderVolWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 37)
)
tpBattUnderVolWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod7.setStatus(
        "current"
    )

tpBattUnderVolWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 38)
)
tpBattUnderVolWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod8.setStatus(
        "current"
    )

tpBattUnderVolWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 39)
)
tpBattUnderVolWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod9.setStatus(
        "current"
    )

tpBattUnderVolWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 40)
)
tpBattUnderVolWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod10.setStatus(
        "current"
    )

tpBattUnderVolWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 41)
)
tpBattUnderVolWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod11.setStatus(
        "current"
    )

tpBattUnderVolWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 42)
)
tpBattUnderVolWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod12.setStatus(
        "current"
    )

tpBattUnderVolWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 43)
)
tpBattUnderVolWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod13.setStatus(
        "current"
    )

tpBattUnderVolWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 44)
)
tpBattUnderVolWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod14.setStatus(
        "current"
    )

tpBattUnderVolWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 45)
)
tpBattUnderVolWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolWarningMod15.setStatus(
        "current"
    )

tpBattOverVolWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 46)
)
tpBattOverVolWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod1.setStatus(
        "current"
    )

tpBattOverVolWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 47)
)
tpBattOverVolWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod2.setStatus(
        "current"
    )

tpBattOverVolWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 48)
)
tpBattOverVolWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod3.setStatus(
        "current"
    )

tpBattOverVolWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 49)
)
tpBattOverVolWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod4.setStatus(
        "current"
    )

tpBattOverVolWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 50)
)
tpBattOverVolWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod5.setStatus(
        "current"
    )

tpBattOverVolWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 51)
)
tpBattOverVolWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod6.setStatus(
        "current"
    )

tpBattOverVolWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 52)
)
tpBattOverVolWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod7.setStatus(
        "current"
    )

tpBattOverVolWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 53)
)
tpBattOverVolWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod8.setStatus(
        "current"
    )

tpBattOverVolWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 54)
)
tpBattOverVolWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod9.setStatus(
        "current"
    )

tpBattOverVolWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 55)
)
tpBattOverVolWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod10.setStatus(
        "current"
    )

tpBattOverVolWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 56)
)
tpBattOverVolWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod11.setStatus(
        "current"
    )

tpBattOverVolWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 57)
)
tpBattOverVolWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod12.setStatus(
        "current"
    )

tpBattOverVolWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 58)
)
tpBattOverVolWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod13.setStatus(
        "current"
    )

tpBattOverVolWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 59)
)
tpBattOverVolWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod14.setStatus(
        "current"
    )

tpBattOverVolWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 60)
)
tpBattOverVolWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattOverVolWarningMod15.setStatus(
        "current"
    )

tpCellChgOverTempProtMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 61)
)
tpCellChgOverTempProtMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod1"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod1.setStatus(
        "current"
    )

tpCellChgOverTempProtMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 62)
)
tpCellChgOverTempProtMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod2"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod2.setStatus(
        "current"
    )

tpCellChgOverTempProtMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 63)
)
tpCellChgOverTempProtMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod3"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod3.setStatus(
        "current"
    )

tpCellChgOverTempProtMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 64)
)
tpCellChgOverTempProtMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod4"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod4.setStatus(
        "current"
    )

tpCellChgOverTempProtMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 65)
)
tpCellChgOverTempProtMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod5"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod5.setStatus(
        "current"
    )

tpCellChgOverTempProtMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 66)
)
tpCellChgOverTempProtMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod6"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod6.setStatus(
        "current"
    )

tpCellChgOverTempProtMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 67)
)
tpCellChgOverTempProtMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod7"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod7.setStatus(
        "current"
    )

tpCellChgOverTempProtMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 68)
)
tpCellChgOverTempProtMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod8"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod8.setStatus(
        "current"
    )

tpCellChgOverTempProtMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 69)
)
tpCellChgOverTempProtMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod9"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod9.setStatus(
        "current"
    )

tpCellChgOverTempProtMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 70)
)
tpCellChgOverTempProtMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod10"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod10.setStatus(
        "current"
    )

tpCellChgOverTempProtMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 71)
)
tpCellChgOverTempProtMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod11"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod11.setStatus(
        "current"
    )

tpCellChgOverTempProtMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 72)
)
tpCellChgOverTempProtMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod12"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod12.setStatus(
        "current"
    )

tpCellChgOverTempProtMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 73)
)
tpCellChgOverTempProtMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod13"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod13.setStatus(
        "current"
    )

tpCellChgOverTempProtMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 74)
)
tpCellChgOverTempProtMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod14"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod14.setStatus(
        "current"
    )

tpCellChgOverTempProtMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 75)
)
tpCellChgOverTempProtMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellChgOverTempProtMod15"))
)
if mibBuilder.loadTexts:
    tpCellChgOverTempProtMod15.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 76)
)
tpCellDisChgOverTempProtMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod1"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod1.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 77)
)
tpCellDisChgOverTempProtMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod2"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod2.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 78)
)
tpCellDisChgOverTempProtMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod3"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod3.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 79)
)
tpCellDisChgOverTempProtMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod4"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod4.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 80)
)
tpCellDisChgOverTempProtMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod5"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod5.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 81)
)
tpCellDisChgOverTempProtMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod6"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod6.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 82)
)
tpCellDisChgOverTempProtMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod7"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod7.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 83)
)
tpCellDisChgOverTempProtMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod8"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod8.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 84)
)
tpCellDisChgOverTempProtMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod9"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod9.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 85)
)
tpCellDisChgOverTempProtMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod10"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod10.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 86)
)
tpCellDisChgOverTempProtMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod11"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod11.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 87)
)
tpCellDisChgOverTempProtMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod12"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod12.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 88)
)
tpCellDisChgOverTempProtMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod13"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod13.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 89)
)
tpCellDisChgOverTempProtMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod14"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod14.setStatus(
        "current"
    )

tpCellDisChgOverTempProtMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 90)
)
tpCellDisChgOverTempProtMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCellDisChgOverTempProtMod15"))
)
if mibBuilder.loadTexts:
    tpCellDisChgOverTempProtMod15.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 91)
)
tpAnyCellUnderTempProtMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod1"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod1.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 92)
)
tpAnyCellUnderTempProtMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod2"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod2.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 93)
)
tpAnyCellUnderTempProtMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod3"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod3.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 94)
)
tpAnyCellUnderTempProtMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod4"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod4.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 95)
)
tpAnyCellUnderTempProtMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod5"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod5.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 96)
)
tpAnyCellUnderTempProtMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod6"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod6.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 97)
)
tpAnyCellUnderTempProtMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod7"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod7.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 98)
)
tpAnyCellUnderTempProtMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod8"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod8.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 99)
)
tpAnyCellUnderTempProtMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod9"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod9.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 100)
)
tpAnyCellUnderTempProtMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod10"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod10.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 101)
)
tpAnyCellUnderTempProtMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod11"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod11.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 102)
)
tpAnyCellUnderTempProtMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod12"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod12.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 103)
)
tpAnyCellUnderTempProtMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod13"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod13.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 104)
)
tpAnyCellUnderTempProtMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod14"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod14.setStatus(
        "current"
    )

tpAnyCellUnderTempProtMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 105)
)
tpAnyCellUnderTempProtMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eAnyCellUnderTempProtMod15"))
)
if mibBuilder.loadTexts:
    tpAnyCellUnderTempProtMod15.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 106)
)
tpBattChgOverCurrWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod1.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 107)
)
tpBattChgOverCurrWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod2.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 108)
)
tpBattChgOverCurrWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod3.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 109)
)
tpBattChgOverCurrWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod4.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 110)
)
tpBattChgOverCurrWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod5.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 111)
)
tpBattChgOverCurrWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod6.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 112)
)
tpBattChgOverCurrWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod7.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 113)
)
tpBattChgOverCurrWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod8.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 114)
)
tpBattChgOverCurrWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod9.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 115)
)
tpBattChgOverCurrWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod10.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 116)
)
tpBattChgOverCurrWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod11.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 117)
)
tpBattChgOverCurrWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod12.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 118)
)
tpBattChgOverCurrWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod13.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 119)
)
tpBattChgOverCurrWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod14.setStatus(
        "current"
    )

tpBattChgOverCurrWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 120)
)
tpBattChgOverCurrWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattChgOverCurrWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattChgOverCurrWarningMod15.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 121)
)
tpBattDisChgOverCurrWarnMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod1"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod1.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 122)
)
tpBattDisChgOverCurrWarnMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod2"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod2.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 123)
)
tpBattDisChgOverCurrWarnMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod3"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod3.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 124)
)
tpBattDisChgOverCurrWarnMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod4"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod4.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 125)
)
tpBattDisChgOverCurrWarnMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod5"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod5.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 126)
)
tpBattDisChgOverCurrWarnMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod6"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod6.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 127)
)
tpBattDisChgOverCurrWarnMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod7"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod7.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 128)
)
tpBattDisChgOverCurrWarnMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod8"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod8.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 129)
)
tpBattDisChgOverCurrWarnMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod9"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod9.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 130)
)
tpBattDisChgOverCurrWarnMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod10"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod10.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 131)
)
tpBattDisChgOverCurrWarnMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod11"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod11.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 132)
)
tpBattDisChgOverCurrWarnMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod12"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod12.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 133)
)
tpBattDisChgOverCurrWarnMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod13"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod13.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 134)
)
tpBattDisChgOverCurrWarnMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod14"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod14.setStatus(
        "current"
    )

tpBattDisChgOverCurrWarnMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 135)
)
tpBattDisChgOverCurrWarnMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattDisChgOverCurrWarnMod15"))
)
if mibBuilder.loadTexts:
    tpBattDisChgOverCurrWarnMod15.setStatus(
        "current"
    )

tpBattLowSOCWarningMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 136)
)
tpBattLowSOCWarningMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod1"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod1.setStatus(
        "current"
    )

tpBattLowSOCWarningMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 137)
)
tpBattLowSOCWarningMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod2"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod2.setStatus(
        "current"
    )

tpBattLowSOCWarningMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 138)
)
tpBattLowSOCWarningMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod3"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod3.setStatus(
        "current"
    )

tpBattLowSOCWarningMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 139)
)
tpBattLowSOCWarningMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod4"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod4.setStatus(
        "current"
    )

tpBattLowSOCWarningMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 140)
)
tpBattLowSOCWarningMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod5"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod5.setStatus(
        "current"
    )

tpBattLowSOCWarningMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 141)
)
tpBattLowSOCWarningMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod6"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod6.setStatus(
        "current"
    )

tpBattLowSOCWarningMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 142)
)
tpBattLowSOCWarningMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod7"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod7.setStatus(
        "current"
    )

tpBattLowSOCWarningMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 143)
)
tpBattLowSOCWarningMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod8"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod8.setStatus(
        "current"
    )

tpBattLowSOCWarningMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 144)
)
tpBattLowSOCWarningMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod9"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod9.setStatus(
        "current"
    )

tpBattLowSOCWarningMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 145)
)
tpBattLowSOCWarningMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod10"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod10.setStatus(
        "current"
    )

tpBattLowSOCWarningMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 146)
)
tpBattLowSOCWarningMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod11"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod11.setStatus(
        "current"
    )

tpBattLowSOCWarningMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 147)
)
tpBattLowSOCWarningMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod12"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod12.setStatus(
        "current"
    )

tpBattLowSOCWarningMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 148)
)
tpBattLowSOCWarningMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod13"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod13.setStatus(
        "current"
    )

tpBattLowSOCWarningMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 149)
)
tpBattLowSOCWarningMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod14"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod14.setStatus(
        "current"
    )

tpBattLowSOCWarningMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 150)
)
tpBattLowSOCWarningMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattLowSOCWarningMod15"))
)
if mibBuilder.loadTexts:
    tpBattLowSOCWarningMod15.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 151)
)
tpBattOverCurrProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod1.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 152)
)
tpBattOverCurrProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod2.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 153)
)
tpBattOverCurrProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod3.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 154)
)
tpBattOverCurrProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod4.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 155)
)
tpBattOverCurrProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod5.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 156)
)
tpBattOverCurrProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod6.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 157)
)
tpBattOverCurrProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod7.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 158)
)
tpBattOverCurrProtectionMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod8"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod8.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 159)
)
tpBattOverCurrProtectionMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod9"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod9.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 160)
)
tpBattOverCurrProtectionMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod10"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod10.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 161)
)
tpBattOverCurrProtectionMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod11"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod11.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 162)
)
tpBattOverCurrProtectionMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod12"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod12.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 163)
)
tpBattOverCurrProtectionMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod13"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod13.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 164)
)
tpBattOverCurrProtectionMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod14"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod14.setStatus(
        "current"
    )

tpBattOverCurrProtectionMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 165)
)
tpBattOverCurrProtectionMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverCurrProtectionMod15"))
)
if mibBuilder.loadTexts:
    tpBattOverCurrProtectionMod15.setStatus(
        "current"
    )

tpBattOverVolProtectionMod1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 166)
)
tpBattOverVolProtectionMod1.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod1"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod1.setStatus(
        "current"
    )

tpBattOverVolProtectionMod2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 167)
)
tpBattOverVolProtectionMod2.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod2"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod2.setStatus(
        "current"
    )

tpBattOverVolProtectionMod3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 168)
)
tpBattOverVolProtectionMod3.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod3"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod3.setStatus(
        "current"
    )

tpBattOverVolProtectionMod4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 169)
)
tpBattOverVolProtectionMod4.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod4"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod4.setStatus(
        "current"
    )

tpBattOverVolProtectionMod5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 170)
)
tpBattOverVolProtectionMod5.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod5"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod5.setStatus(
        "current"
    )

tpBattOverVolProtectionMod6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 171)
)
tpBattOverVolProtectionMod6.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod6"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod6.setStatus(
        "current"
    )

tpBattOverVolProtectionMod7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 172)
)
tpBattOverVolProtectionMod7.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod7"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod7.setStatus(
        "current"
    )

tpBattOverVolProtectionMod8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 173)
)
tpBattOverVolProtectionMod8.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod8"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod8.setStatus(
        "current"
    )

tpBattOverVolProtectionMod9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 174)
)
tpBattOverVolProtectionMod9.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod9"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod9.setStatus(
        "current"
    )

tpBattOverVolProtectionMod10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 175)
)
tpBattOverVolProtectionMod10.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod10"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod10.setStatus(
        "current"
    )

tpBattOverVolProtectionMod11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 176)
)
tpBattOverVolProtectionMod11.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod11"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod11.setStatus(
        "current"
    )

tpBattOverVolProtectionMod12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 177)
)
tpBattOverVolProtectionMod12.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod12"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod12.setStatus(
        "current"
    )

tpBattOverVolProtectionMod13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 178)
)
tpBattOverVolProtectionMod13.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod13"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod13.setStatus(
        "current"
    )

tpBattOverVolProtectionMod14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 179)
)
tpBattOverVolProtectionMod14.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod14"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod14.setStatus(
        "current"
    )

tpBattOverVolProtectionMod15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 180)
)
tpBattOverVolProtectionMod15.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattOverVolProtectionMod15"))
)
if mibBuilder.loadTexts:
    tpBattOverVolProtectionMod15.setStatus(
        "current"
    )

tpBattUnderVolProtAnyModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 181)
)
tpBattUnderVolProtAnyModule.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBattUnderVolProtAnyModule"))
)
if mibBuilder.loadTexts:
    tpBattUnderVolProtAnyModule.setStatus(
        "current"
    )

tpModule1Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 182)
)
tpModule1Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule1Isolated"))
)
if mibBuilder.loadTexts:
    tpModule1Isolated.setStatus(
        "current"
    )

tpModule2Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 183)
)
tpModule2Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule2Isolated"))
)
if mibBuilder.loadTexts:
    tpModule2Isolated.setStatus(
        "current"
    )

tpModule3Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 184)
)
tpModule3Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule3Isolated"))
)
if mibBuilder.loadTexts:
    tpModule3Isolated.setStatus(
        "current"
    )

tpModule4Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 185)
)
tpModule4Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule4Isolated"))
)
if mibBuilder.loadTexts:
    tpModule4Isolated.setStatus(
        "current"
    )

tpModule5Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 186)
)
tpModule5Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule5Isolated"))
)
if mibBuilder.loadTexts:
    tpModule5Isolated.setStatus(
        "current"
    )

tpModule6Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 187)
)
tpModule6Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule6Isolated"))
)
if mibBuilder.loadTexts:
    tpModule6Isolated.setStatus(
        "current"
    )

tpModule7Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 188)
)
tpModule7Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule7Isolated"))
)
if mibBuilder.loadTexts:
    tpModule7Isolated.setStatus(
        "current"
    )

tpModule8Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 189)
)
tpModule8Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule8Isolated"))
)
if mibBuilder.loadTexts:
    tpModule8Isolated.setStatus(
        "current"
    )

tpModule9Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 190)
)
tpModule9Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule9Isolated"))
)
if mibBuilder.loadTexts:
    tpModule9Isolated.setStatus(
        "current"
    )

tpModule10Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 191)
)
tpModule10Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule10Isolated"))
)
if mibBuilder.loadTexts:
    tpModule10Isolated.setStatus(
        "current"
    )

tpModule11Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 192)
)
tpModule11Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule11Isolated"))
)
if mibBuilder.loadTexts:
    tpModule11Isolated.setStatus(
        "current"
    )

tpModule12Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 193)
)
tpModule12Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule12Isolated"))
)
if mibBuilder.loadTexts:
    tpModule12Isolated.setStatus(
        "current"
    )

tpModule13Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 194)
)
tpModule13Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule13Isolated"))
)
if mibBuilder.loadTexts:
    tpModule13Isolated.setStatus(
        "current"
    )

tpModule14Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 195)
)
tpModule14Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule14Isolated"))
)
if mibBuilder.loadTexts:
    tpModule14Isolated.setStatus(
        "current"
    )

tpModule15Isolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 196)
)
tpModule15Isolated.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule15Isolated"))
)
if mibBuilder.loadTexts:
    tpModule15Isolated.setStatus(
        "current"
    )

tpModule1CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 197)
)
tpModule1CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule1CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule1CommFailAlarm.setStatus(
        "current"
    )

tpModule2CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 198)
)
tpModule2CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule2CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule2CommFailAlarm.setStatus(
        "current"
    )

tpModule3CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 199)
)
tpModule3CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule3CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule3CommFailAlarm.setStatus(
        "current"
    )

tpModule4CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 200)
)
tpModule4CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule4CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule4CommFailAlarm.setStatus(
        "current"
    )

tpModule5CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 201)
)
tpModule5CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule5CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule5CommFailAlarm.setStatus(
        "current"
    )

tpModule6CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 202)
)
tpModule6CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule6CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule6CommFailAlarm.setStatus(
        "current"
    )

tpModule7CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 203)
)
tpModule7CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule7CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule7CommFailAlarm.setStatus(
        "current"
    )

tpModule8CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 204)
)
tpModule8CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule8CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule8CommFailAlarm.setStatus(
        "current"
    )

tpModule9CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 205)
)
tpModule9CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule9CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule9CommFailAlarm.setStatus(
        "current"
    )

tpModule10CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 206)
)
tpModule10CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule10CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule10CommFailAlarm.setStatus(
        "current"
    )

tpModule11CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 207)
)
tpModule11CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule11CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule11CommFailAlarm.setStatus(
        "current"
    )

tpModule12CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 208)
)
tpModule12CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule12CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule12CommFailAlarm.setStatus(
        "current"
    )

tpModule13CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 209)
)
tpModule13CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule13CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule13CommFailAlarm.setStatus(
        "current"
    )

tpModule14CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 210)
)
tpModule14CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule14CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule14CommFailAlarm.setStatus(
        "current"
    )

tpModule15CommFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 211)
)
tpModule15CommFailAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eModule15CommFailAlarm"))
)
if mibBuilder.loadTexts:
    tpModule15CommFailAlarm.setStatus(
        "current"
    )

tpACPowerfail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 212)
)
tpACPowerfail.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eACPowerfail"))
)
if mibBuilder.loadTexts:
    tpACPowerfail.setStatus(
        "current"
    )

tpSingleRectifierModuleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 213)
)
tpSingleRectifierModuleFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eSingleRectifierModuleFail"))
)
if mibBuilder.loadTexts:
    tpSingleRectifierModuleFail.setStatus(
        "current"
    )

tpMultipleRectifierModuleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 214)
)
tpMultipleRectifierModuleFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eMultipleRectifierModuleFail"))
)
if mibBuilder.loadTexts:
    tpMultipleRectifierModuleFail.setStatus(
        "current"
    )

tpLoadFusetrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 215)
)
tpLoadFusetrip.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eLoadFusetrip"))
)
if mibBuilder.loadTexts:
    tpLoadFusetrip.setStatus(
        "current"
    )

tpLLVDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 216)
)
tpLLVDAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eLLVDAlarm"))
)
if mibBuilder.loadTexts:
    tpLLVDAlarm.setStatus(
        "current"
    )

tpBLVDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 217)
)
tpBLVDAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBLVDAlarm"))
)
if mibBuilder.loadTexts:
    tpBLVDAlarm.setStatus(
        "current"
    )

tpBatteryfuseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 218)
)
tpBatteryfuseFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBatteryfuseFail"))
)
if mibBuilder.loadTexts:
    tpBatteryfuseFail.setStatus(
        "current"
    )

tpBatteryonLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 219)
)
tpBatteryonLoad.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eBatteryonLoad"))
)
if mibBuilder.loadTexts:
    tpBatteryonLoad.setStatus(
        "current"
    )

tpFireAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 220)
)
tpFireAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eFireAlarm"))
)
if mibBuilder.loadTexts:
    tpFireAlarm.setStatus(
        "current"
    )

tpUPS1Faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 221)
)
tpUPS1Faulty.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eUPS1Faulty"))
)
if mibBuilder.loadTexts:
    tpUPS1Faulty.setStatus(
        "current"
    )

tpUPS1OnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 222)
)
tpUPS1OnBypass.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eUPS1OnBypass"))
)
if mibBuilder.loadTexts:
    tpUPS1OnBypass.setStatus(
        "current"
    )

tpUPS2Faulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 223)
)
tpUPS2Faulty.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eUPS2Faulty"))
)
if mibBuilder.loadTexts:
    tpUPS2Faulty.setStatus(
        "current"
    )

tpUPS2OnBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 224)
)
tpUPS2OnBypass.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eUPS2OnBypass"))
)
if mibBuilder.loadTexts:
    tpUPS2OnBypass.setStatus(
        "current"
    )

tpHighTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 10, 225)
)
tpHighTempAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eHighTempAlarm"))
)
if mibBuilder.loadTexts:
    tpHighTempAlarm.setStatus(
        "current"
    )

tpSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 1, 1)
)
tpSystemReset.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eSystemResetCause"))
)
if mibBuilder.loadTexts:
    tpSystemReset.setStatus(
        "current"
    )

tpPeriodicTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 1, 3)
)
tpPeriodicTrap.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "ePeriodicTrap"))
)
if mibBuilder.loadTexts:
    tpPeriodicTrap.setStatus(
        "current"
    )

tpGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 1, 5)
)
tpGenericTrap.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eGenericTrap"))
)
if mibBuilder.loadTexts:
    tpGenericTrap.setStatus(
        "current"
    )

tpCommFailPCtoSMPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 2, 1, 11, 1, 7)
)
tpCommFailPCtoSMPS.setObjects(
      *(("DELTAPOWERSOLUTIONS-AG3-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-AG3-MIB", "eCommFailPCtoSMPS"))
)
if mibBuilder.loadTexts:
    tpCommFailPCtoSMPS.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELTAPOWERSOLUTIONS-AG3-MIB",
    **{"DPSUsmAuthPrivProtocol": DPSUsmAuthPrivProtocol,
       "deltapowersolutions": deltapowersolutions,
       "products": products,
       "ag3": ag3,
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
       "eCellOverVolProtectionMod8": eCellOverVolProtectionMod8,
       "eCellOverVolProtectionMod9": eCellOverVolProtectionMod9,
       "eCellOverVolProtectionMod10": eCellOverVolProtectionMod10,
       "eCellOverVolProtectionMod11": eCellOverVolProtectionMod11,
       "eCellOverVolProtectionMod12": eCellOverVolProtectionMod12,
       "eCellOverVolProtectionMod13": eCellOverVolProtectionMod13,
       "eCellOverVolProtectionMod14": eCellOverVolProtectionMod14,
       "eCellOverVolProtectionMod15": eCellOverVolProtectionMod15,
       "eCellUnderVolProtectionMod1": eCellUnderVolProtectionMod1,
       "eCellUnderVolProtectionMod2": eCellUnderVolProtectionMod2,
       "eCellUnderVolProtectionMod3": eCellUnderVolProtectionMod3,
       "eCellUnderVolProtectionMod4": eCellUnderVolProtectionMod4,
       "eCellUnderVolProtectionMod5": eCellUnderVolProtectionMod5,
       "eCellUnderVolProtectionMod6": eCellUnderVolProtectionMod6,
       "eCellUnderVolProtectionMod7": eCellUnderVolProtectionMod7,
       "eCellUnderVolProtectionMod8": eCellUnderVolProtectionMod8,
       "eCellUnderVolProtectionMod9": eCellUnderVolProtectionMod9,
       "eCellUnderVolProtectionMod10": eCellUnderVolProtectionMod10,
       "eCellUnderVolProtectionMod11": eCellUnderVolProtectionMod11,
       "eCellUnderVolProtectionMod12": eCellUnderVolProtectionMod12,
       "eCellUnderVolProtectionMod13": eCellUnderVolProtectionMod13,
       "eCellUnderVolProtectionMod14": eCellUnderVolProtectionMod14,
       "eCellUnderVolProtectionMod15": eCellUnderVolProtectionMod15,
       "eBattUnderVolWarningMod1": eBattUnderVolWarningMod1,
       "eBattUnderVolWarningMod2": eBattUnderVolWarningMod2,
       "eBattUnderVolWarningMod3": eBattUnderVolWarningMod3,
       "eBattUnderVolWarningMod4": eBattUnderVolWarningMod4,
       "eBattUnderVolWarningMod5": eBattUnderVolWarningMod5,
       "eBattUnderVolWarningMod6": eBattUnderVolWarningMod6,
       "eBattUnderVolWarningMod7": eBattUnderVolWarningMod7,
       "eBattUnderVolWarningMod8": eBattUnderVolWarningMod8,
       "eBattUnderVolWarningMod9": eBattUnderVolWarningMod9,
       "eBattUnderVolWarningMod10": eBattUnderVolWarningMod10,
       "eBattUnderVolWarningMod11": eBattUnderVolWarningMod11,
       "eBattUnderVolWarningMod12": eBattUnderVolWarningMod12,
       "eBattUnderVolWarningMod13": eBattUnderVolWarningMod13,
       "eBattUnderVolWarningMod14": eBattUnderVolWarningMod14,
       "eBattUnderVolWarningMod15": eBattUnderVolWarningMod15,
       "eBattOverVolWarningMod1": eBattOverVolWarningMod1,
       "eBattOverVolWarningMod2": eBattOverVolWarningMod2,
       "eBattOverVolWarningMod3": eBattOverVolWarningMod3,
       "eBattOverVolWarningMod4": eBattOverVolWarningMod4,
       "eBattOverVolWarningMod5": eBattOverVolWarningMod5,
       "eBattOverVolWarningMod6": eBattOverVolWarningMod6,
       "eBattOverVolWarningMod7": eBattOverVolWarningMod7,
       "eBattOverVolWarningMod8": eBattOverVolWarningMod8,
       "eBattOverVolWarningMod9": eBattOverVolWarningMod9,
       "eBattOverVolWarningMod10": eBattOverVolWarningMod10,
       "eBattOverVolWarningMod11": eBattOverVolWarningMod11,
       "eBattOverVolWarningMod12": eBattOverVolWarningMod12,
       "eBattOverVolWarningMod13": eBattOverVolWarningMod13,
       "eBattOverVolWarningMod14": eBattOverVolWarningMod14,
       "eBattOverVolWarningMod15": eBattOverVolWarningMod15,
       "eCellChgOverTempProtMod1": eCellChgOverTempProtMod1,
       "eCellChgOverTempProtMod2": eCellChgOverTempProtMod2,
       "eCellChgOverTempProtMod3": eCellChgOverTempProtMod3,
       "eCellChgOverTempProtMod4": eCellChgOverTempProtMod4,
       "eCellChgOverTempProtMod5": eCellChgOverTempProtMod5,
       "eCellChgOverTempProtMod6": eCellChgOverTempProtMod6,
       "eCellChgOverTempProtMod7": eCellChgOverTempProtMod7,
       "eCellChgOverTempProtMod8": eCellChgOverTempProtMod8,
       "eCellChgOverTempProtMod9": eCellChgOverTempProtMod9,
       "eCellChgOverTempProtMod10": eCellChgOverTempProtMod10,
       "eCellChgOverTempProtMod11": eCellChgOverTempProtMod11,
       "eCellChgOverTempProtMod12": eCellChgOverTempProtMod12,
       "eCellChgOverTempProtMod13": eCellChgOverTempProtMod13,
       "eCellChgOverTempProtMod14": eCellChgOverTempProtMod14,
       "eCellChgOverTempProtMod15": eCellChgOverTempProtMod15,
       "eCellDisChgOverTempProtMod1": eCellDisChgOverTempProtMod1,
       "eCellDisChgOverTempProtMod2": eCellDisChgOverTempProtMod2,
       "eCellDisChgOverTempProtMod3": eCellDisChgOverTempProtMod3,
       "eCellDisChgOverTempProtMod4": eCellDisChgOverTempProtMod4,
       "eCellDisChgOverTempProtMod5": eCellDisChgOverTempProtMod5,
       "eCellDisChgOverTempProtMod6": eCellDisChgOverTempProtMod6,
       "eCellDisChgOverTempProtMod7": eCellDisChgOverTempProtMod7,
       "eCellDisChgOverTempProtMod8": eCellDisChgOverTempProtMod8,
       "eCellDisChgOverTempProtMod9": eCellDisChgOverTempProtMod9,
       "eCellDisChgOverTempProtMod10": eCellDisChgOverTempProtMod10,
       "eCellDisChgOverTempProtMod11": eCellDisChgOverTempProtMod11,
       "eCellDisChgOverTempProtMod12": eCellDisChgOverTempProtMod12,
       "eCellDisChgOverTempProtMod13": eCellDisChgOverTempProtMod13,
       "eCellDisChgOverTempProtMod14": eCellDisChgOverTempProtMod14,
       "eCellDisChgOverTempProtMod15": eCellDisChgOverTempProtMod15,
       "eAnyCellUnderTempProtMod1": eAnyCellUnderTempProtMod1,
       "eAnyCellUnderTempProtMod2": eAnyCellUnderTempProtMod2,
       "eAnyCellUnderTempProtMod3": eAnyCellUnderTempProtMod3,
       "eAnyCellUnderTempProtMod4": eAnyCellUnderTempProtMod4,
       "eAnyCellUnderTempProtMod5": eAnyCellUnderTempProtMod5,
       "eAnyCellUnderTempProtMod6": eAnyCellUnderTempProtMod6,
       "eAnyCellUnderTempProtMod7": eAnyCellUnderTempProtMod7,
       "eAnyCellUnderTempProtMod8": eAnyCellUnderTempProtMod8,
       "eAnyCellUnderTempProtMod9": eAnyCellUnderTempProtMod9,
       "eAnyCellUnderTempProtMod10": eAnyCellUnderTempProtMod10,
       "eAnyCellUnderTempProtMod11": eAnyCellUnderTempProtMod11,
       "eAnyCellUnderTempProtMod12": eAnyCellUnderTempProtMod12,
       "eAnyCellUnderTempProtMod13": eAnyCellUnderTempProtMod13,
       "eAnyCellUnderTempProtMod14": eAnyCellUnderTempProtMod14,
       "eAnyCellUnderTempProtMod15": eAnyCellUnderTempProtMod15,
       "eBattChgOverCurrWarningMod1": eBattChgOverCurrWarningMod1,
       "eBattChgOverCurrWarningMod2": eBattChgOverCurrWarningMod2,
       "eBattChgOverCurrWarningMod3": eBattChgOverCurrWarningMod3,
       "eBattChgOverCurrWarningMod4": eBattChgOverCurrWarningMod4,
       "eBattChgOverCurrWarningMod5": eBattChgOverCurrWarningMod5,
       "eBattChgOverCurrWarningMod6": eBattChgOverCurrWarningMod6,
       "eBattChgOverCurrWarningMod7": eBattChgOverCurrWarningMod7,
       "eBattChgOverCurrWarningMod8": eBattChgOverCurrWarningMod8,
       "eBattChgOverCurrWarningMod9": eBattChgOverCurrWarningMod9,
       "eBattChgOverCurrWarningMod10": eBattChgOverCurrWarningMod10,
       "eBattChgOverCurrWarningMod11": eBattChgOverCurrWarningMod11,
       "eBattChgOverCurrWarningMod12": eBattChgOverCurrWarningMod12,
       "eBattChgOverCurrWarningMod13": eBattChgOverCurrWarningMod13,
       "eBattChgOverCurrWarningMod14": eBattChgOverCurrWarningMod14,
       "eBattChgOverCurrWarningMod15": eBattChgOverCurrWarningMod15,
       "eBattDisChgOverCurrWarnMod1": eBattDisChgOverCurrWarnMod1,
       "eBattDisChgOverCurrWarnMod2": eBattDisChgOverCurrWarnMod2,
       "eBattDisChgOverCurrWarnMod3": eBattDisChgOverCurrWarnMod3,
       "eBattDisChgOverCurrWarnMod4": eBattDisChgOverCurrWarnMod4,
       "eBattDisChgOverCurrWarnMod5": eBattDisChgOverCurrWarnMod5,
       "eBattDisChgOverCurrWarnMod6": eBattDisChgOverCurrWarnMod6,
       "eBattDisChgOverCurrWarnMod7": eBattDisChgOverCurrWarnMod7,
       "eBattDisChgOverCurrWarnMod8": eBattDisChgOverCurrWarnMod8,
       "eBattDisChgOverCurrWarnMod9": eBattDisChgOverCurrWarnMod9,
       "eBattDisChgOverCurrWarnMod10": eBattDisChgOverCurrWarnMod10,
       "eBattDisChgOverCurrWarnMod11": eBattDisChgOverCurrWarnMod11,
       "eBattDisChgOverCurrWarnMod12": eBattDisChgOverCurrWarnMod12,
       "eBattDisChgOverCurrWarnMod13": eBattDisChgOverCurrWarnMod13,
       "eBattDisChgOverCurrWarnMod14": eBattDisChgOverCurrWarnMod14,
       "eBattDisChgOverCurrWarnMod15": eBattDisChgOverCurrWarnMod15,
       "eBattLowSOCWarningMod1": eBattLowSOCWarningMod1,
       "eBattLowSOCWarningMod2": eBattLowSOCWarningMod2,
       "eBattLowSOCWarningMod3": eBattLowSOCWarningMod3,
       "eBattLowSOCWarningMod4": eBattLowSOCWarningMod4,
       "eBattLowSOCWarningMod5": eBattLowSOCWarningMod5,
       "eBattLowSOCWarningMod6": eBattLowSOCWarningMod6,
       "eBattLowSOCWarningMod7": eBattLowSOCWarningMod7,
       "eBattLowSOCWarningMod8": eBattLowSOCWarningMod8,
       "eBattLowSOCWarningMod9": eBattLowSOCWarningMod9,
       "eBattLowSOCWarningMod10": eBattLowSOCWarningMod10,
       "eBattLowSOCWarningMod11": eBattLowSOCWarningMod11,
       "eBattLowSOCWarningMod12": eBattLowSOCWarningMod12,
       "eBattLowSOCWarningMod13": eBattLowSOCWarningMod13,
       "eBattLowSOCWarningMod14": eBattLowSOCWarningMod14,
       "eBattLowSOCWarningMod15": eBattLowSOCWarningMod15,
       "eBattOverCurrProtectionMod1": eBattOverCurrProtectionMod1,
       "eBattOverCurrProtectionMod2": eBattOverCurrProtectionMod2,
       "eBattOverCurrProtectionMod3": eBattOverCurrProtectionMod3,
       "eBattOverCurrProtectionMod4": eBattOverCurrProtectionMod4,
       "eBattOverCurrProtectionMod5": eBattOverCurrProtectionMod5,
       "eBattOverCurrProtectionMod6": eBattOverCurrProtectionMod6,
       "eBattOverCurrProtectionMod7": eBattOverCurrProtectionMod7,
       "eBattOverCurrProtectionMod8": eBattOverCurrProtectionMod8,
       "eBattOverCurrProtectionMod9": eBattOverCurrProtectionMod9,
       "eBattOverCurrProtectionMod10": eBattOverCurrProtectionMod10,
       "eBattOverCurrProtectionMod11": eBattOverCurrProtectionMod11,
       "eBattOverCurrProtectionMod12": eBattOverCurrProtectionMod12,
       "eBattOverCurrProtectionMod13": eBattOverCurrProtectionMod13,
       "eBattOverCurrProtectionMod14": eBattOverCurrProtectionMod14,
       "eBattOverCurrProtectionMod15": eBattOverCurrProtectionMod15,
       "eBattOverVolProtectionMod1": eBattOverVolProtectionMod1,
       "eBattOverVolProtectionMod2": eBattOverVolProtectionMod2,
       "eBattOverVolProtectionMod3": eBattOverVolProtectionMod3,
       "eBattOverVolProtectionMod4": eBattOverVolProtectionMod4,
       "eBattOverVolProtectionMod5": eBattOverVolProtectionMod5,
       "eBattOverVolProtectionMod6": eBattOverVolProtectionMod6,
       "eBattOverVolProtectionMod7": eBattOverVolProtectionMod7,
       "eBattOverVolProtectionMod8": eBattOverVolProtectionMod8,
       "eBattOverVolProtectionMod9": eBattOverVolProtectionMod9,
       "eBattOverVolProtectionMod10": eBattOverVolProtectionMod10,
       "eBattOverVolProtectionMod11": eBattOverVolProtectionMod11,
       "eBattOverVolProtectionMod12": eBattOverVolProtectionMod12,
       "eBattOverVolProtectionMod13": eBattOverVolProtectionMod13,
       "eBattOverVolProtectionMod14": eBattOverVolProtectionMod14,
       "eBattOverVolProtectionMod15": eBattOverVolProtectionMod15,
       "eBattUnderVolProtAnyModule": eBattUnderVolProtAnyModule,
       "eModule1Isolated": eModule1Isolated,
       "eModule2Isolated": eModule2Isolated,
       "eModule3Isolated": eModule3Isolated,
       "eModule4Isolated": eModule4Isolated,
       "eModule5Isolated": eModule5Isolated,
       "eModule6Isolated": eModule6Isolated,
       "eModule7Isolated": eModule7Isolated,
       "eModule8Isolated": eModule8Isolated,
       "eModule9Isolated": eModule9Isolated,
       "eModule10Isolated": eModule10Isolated,
       "eModule11Isolated": eModule11Isolated,
       "eModule12Isolated": eModule12Isolated,
       "eModule13Isolated": eModule13Isolated,
       "eModule14Isolated": eModule14Isolated,
       "eModule15Isolated": eModule15Isolated,
       "eModule1CommFailAlarm": eModule1CommFailAlarm,
       "eModule2CommFailAlarm": eModule2CommFailAlarm,
       "eModule3CommFailAlarm": eModule3CommFailAlarm,
       "eModule4CommFailAlarm": eModule4CommFailAlarm,
       "eModule5CommFailAlarm": eModule5CommFailAlarm,
       "eModule6CommFailAlarm": eModule6CommFailAlarm,
       "eModule7CommFailAlarm": eModule7CommFailAlarm,
       "eModule8CommFailAlarm": eModule8CommFailAlarm,
       "eModule9CommFailAlarm": eModule9CommFailAlarm,
       "eModule10CommFailAlarm": eModule10CommFailAlarm,
       "eModule11CommFailAlarm": eModule11CommFailAlarm,
       "eModule12CommFailAlarm": eModule12CommFailAlarm,
       "eModule13CommFailAlarm": eModule13CommFailAlarm,
       "eModule14CommFailAlarm": eModule14CommFailAlarm,
       "eModule15CommFailAlarm": eModule15CommFailAlarm,
       "eACPowerfail": eACPowerfail,
       "eSingleRectifierModuleFail": eSingleRectifierModuleFail,
       "eMultipleRectifierModuleFail": eMultipleRectifierModuleFail,
       "eLoadFusetrip": eLoadFusetrip,
       "eLLVDAlarm": eLLVDAlarm,
       "eBLVDAlarm": eBLVDAlarm,
       "eBatteryfuseFail": eBatteryfuseFail,
       "eBatteryonLoad": eBatteryonLoad,
       "eFireAlarm": eFireAlarm,
       "eUPS1Faulty": eUPS1Faulty,
       "eUPS1OnBypass": eUPS1OnBypass,
       "eUPS2Faulty": eUPS2Faulty,
       "eUPS2OnBypass": eUPS2OnBypass,
       "eHighTempAlarm": eHighTempAlarm,
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
       "eSOCInfo": eSOCInfo,
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
       "eSOHInfo": eSOHInfo,
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
       "eBatteryMaxTempModule1": eBatteryMaxTempModule1,
       "eBatteryMaxTempModule2": eBatteryMaxTempModule2,
       "eBatteryMaxTempModule3": eBatteryMaxTempModule3,
       "eBatteryMaxTempModule4": eBatteryMaxTempModule4,
       "eBatteryMaxTempModule5": eBatteryMaxTempModule5,
       "eBatteryMaxTempModule6": eBatteryMaxTempModule6,
       "eBatteryMaxTempModule7": eBatteryMaxTempModule7,
       "eBatteryMaxTempModule8": eBatteryMaxTempModule8,
       "eBatteryMaxTempModule9": eBatteryMaxTempModule9,
       "eBatteryMaxTempModule10": eBatteryMaxTempModule10,
       "eBatteryMaxTempModule11": eBatteryMaxTempModule11,
       "eBatteryMaxTempModule12": eBatteryMaxTempModule12,
       "eBatteryMaxTempModule13": eBatteryMaxTempModule13,
       "eBatteryMaxTempModule14": eBatteryMaxTempModule14,
       "eBatteryMaxTempModule15": eBatteryMaxTempModule15,
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
       "eMaxChargeCurrInfo": eMaxChargeCurrInfo,
       "eModuleMaxChargeCurrentLimit": eModuleMaxChargeCurrentLimit,
       "eInstMaxModuleCurrentInfo": eInstMaxModuleCurrentInfo,
       "eInstantaneousMaxModuleCurrent": eInstantaneousMaxModuleCurrent,
       "eSMPSInfo": eSMPSInfo,
       "eDCVoltage": eDCVoltage,
       "eDCCurrent": eDCCurrent,
       "eDCKWH": eDCKWH,
       "eLoadcurrent": eLoadcurrent,
       "eBatteryCurrent": eBatteryCurrent,
       "eNoOfRectifiersPoweredUp": eNoOfRectifiersPoweredUp,
       "eSMPSManufacturerName": eSMPSManufacturerName,
       "eControllerModel": eControllerModel,
       "eSMPSFirmwareVersion": eSMPSFirmwareVersion,
       "eSMPSPartNo": eSMPSPartNo,
       "eInputLineAVoltage": eInputLineAVoltage,
       "eInputLineBVoltage": eInputLineBVoltage,
       "eInputLineCVoltage": eInputLineCVoltage,
       "eInputLineACurrent": eInputLineACurrent,
       "eInputLineBCurrent": eInputLineBCurrent,
       "eInputLineCCurrent": eInputLineCCurrent,
       "eMainsSource1KWh": eMainsSource1KWh,
       "eMainsCumulativeRunHrs": eMainsCumulativeRunHrs,
       "eBatteryCumulativeKWh": eBatteryCumulativeKWh,
       "eBatteryCumulativeRunHrs": eBatteryCumulativeRunHrs,
       "eMainsSource2KWh": eMainsSource2KWh,
       "eDCOutputPower": eDCOutputPower,
       "eLoadCumulativeKWh": eLoadCumulativeKWh,
       "eSettingInfo": eSettingInfo,
       "eFloatVoltage": eFloatVoltage,
       "eBoostVoltage": eBoostVoltage,
       "eChargeCurrentLimit": eChargeCurrentLimit,
       "eLLVDVoltage": eLLVDVoltage,
       "eBLVDVoltage": eBLVDVoltage,
       "eAmbientHighTempThreshold": eAmbientHighTempThreshold,
       "trapNotifications": trapNotifications,
       "tpCellOverVolProtectionMod1": tpCellOverVolProtectionMod1,
       "tpCellOverVolProtectionMod2": tpCellOverVolProtectionMod2,
       "tpCellOverVolProtectionMod3": tpCellOverVolProtectionMod3,
       "tpCellOverVolProtectionMod4": tpCellOverVolProtectionMod4,
       "tpCellOverVolProtectionMod5": tpCellOverVolProtectionMod5,
       "tpCellOverVolProtectionMod6": tpCellOverVolProtectionMod6,
       "tpCellOverVolProtectionMod7": tpCellOverVolProtectionMod7,
       "tpCellOverVolProtectionMod8": tpCellOverVolProtectionMod8,
       "tpCellOverVolProtectionMod9": tpCellOverVolProtectionMod9,
       "tpCellOverVolProtectionMod10": tpCellOverVolProtectionMod10,
       "tpCellOverVolProtectionMod11": tpCellOverVolProtectionMod11,
       "tpCellOverVolProtectionMod12": tpCellOverVolProtectionMod12,
       "tpCellOverVolProtectionMod13": tpCellOverVolProtectionMod13,
       "tpCellOverVolProtectionMod14": tpCellOverVolProtectionMod14,
       "tpCellOverVolProtectionMod15": tpCellOverVolProtectionMod15,
       "tpCellUnderVolProtectionMod1": tpCellUnderVolProtectionMod1,
       "tpCellUnderVolProtectionMod2": tpCellUnderVolProtectionMod2,
       "tpCellUnderVolProtectionMod3": tpCellUnderVolProtectionMod3,
       "tpCellUnderVolProtectionMod4": tpCellUnderVolProtectionMod4,
       "tpCellUnderVolProtectionMod5": tpCellUnderVolProtectionMod5,
       "tpCellUnderVolProtectionMod6": tpCellUnderVolProtectionMod6,
       "tpCellUnderVolProtectionMod7": tpCellUnderVolProtectionMod7,
       "tpCellUnderVolProtectionMod8": tpCellUnderVolProtectionMod8,
       "tpCellUnderVolProtectionMod9": tpCellUnderVolProtectionMod9,
       "tpCellUnderVolProtectionMod10": tpCellUnderVolProtectionMod10,
       "tpCellUnderVolProtectionMod11": tpCellUnderVolProtectionMod11,
       "tpCellUnderVolProtectionMod12": tpCellUnderVolProtectionMod12,
       "tpCellUnderVolProtectionMod13": tpCellUnderVolProtectionMod13,
       "tpCellUnderVolProtectionMod14": tpCellUnderVolProtectionMod14,
       "tpCellUnderVolProtectionMod15": tpCellUnderVolProtectionMod15,
       "tpBattUnderVolWarningMod1": tpBattUnderVolWarningMod1,
       "tpBattUnderVolWarningMod2": tpBattUnderVolWarningMod2,
       "tpBattUnderVolWarningMod3": tpBattUnderVolWarningMod3,
       "tpBattUnderVolWarningMod4": tpBattUnderVolWarningMod4,
       "tpBattUnderVolWarningMod5": tpBattUnderVolWarningMod5,
       "tpBattUnderVolWarningMod6": tpBattUnderVolWarningMod6,
       "tpBattUnderVolWarningMod7": tpBattUnderVolWarningMod7,
       "tpBattUnderVolWarningMod8": tpBattUnderVolWarningMod8,
       "tpBattUnderVolWarningMod9": tpBattUnderVolWarningMod9,
       "tpBattUnderVolWarningMod10": tpBattUnderVolWarningMod10,
       "tpBattUnderVolWarningMod11": tpBattUnderVolWarningMod11,
       "tpBattUnderVolWarningMod12": tpBattUnderVolWarningMod12,
       "tpBattUnderVolWarningMod13": tpBattUnderVolWarningMod13,
       "tpBattUnderVolWarningMod14": tpBattUnderVolWarningMod14,
       "tpBattUnderVolWarningMod15": tpBattUnderVolWarningMod15,
       "tpBattOverVolWarningMod1": tpBattOverVolWarningMod1,
       "tpBattOverVolWarningMod2": tpBattOverVolWarningMod2,
       "tpBattOverVolWarningMod3": tpBattOverVolWarningMod3,
       "tpBattOverVolWarningMod4": tpBattOverVolWarningMod4,
       "tpBattOverVolWarningMod5": tpBattOverVolWarningMod5,
       "tpBattOverVolWarningMod6": tpBattOverVolWarningMod6,
       "tpBattOverVolWarningMod7": tpBattOverVolWarningMod7,
       "tpBattOverVolWarningMod8": tpBattOverVolWarningMod8,
       "tpBattOverVolWarningMod9": tpBattOverVolWarningMod9,
       "tpBattOverVolWarningMod10": tpBattOverVolWarningMod10,
       "tpBattOverVolWarningMod11": tpBattOverVolWarningMod11,
       "tpBattOverVolWarningMod12": tpBattOverVolWarningMod12,
       "tpBattOverVolWarningMod13": tpBattOverVolWarningMod13,
       "tpBattOverVolWarningMod14": tpBattOverVolWarningMod14,
       "tpBattOverVolWarningMod15": tpBattOverVolWarningMod15,
       "tpCellChgOverTempProtMod1": tpCellChgOverTempProtMod1,
       "tpCellChgOverTempProtMod2": tpCellChgOverTempProtMod2,
       "tpCellChgOverTempProtMod3": tpCellChgOverTempProtMod3,
       "tpCellChgOverTempProtMod4": tpCellChgOverTempProtMod4,
       "tpCellChgOverTempProtMod5": tpCellChgOverTempProtMod5,
       "tpCellChgOverTempProtMod6": tpCellChgOverTempProtMod6,
       "tpCellChgOverTempProtMod7": tpCellChgOverTempProtMod7,
       "tpCellChgOverTempProtMod8": tpCellChgOverTempProtMod8,
       "tpCellChgOverTempProtMod9": tpCellChgOverTempProtMod9,
       "tpCellChgOverTempProtMod10": tpCellChgOverTempProtMod10,
       "tpCellChgOverTempProtMod11": tpCellChgOverTempProtMod11,
       "tpCellChgOverTempProtMod12": tpCellChgOverTempProtMod12,
       "tpCellChgOverTempProtMod13": tpCellChgOverTempProtMod13,
       "tpCellChgOverTempProtMod14": tpCellChgOverTempProtMod14,
       "tpCellChgOverTempProtMod15": tpCellChgOverTempProtMod15,
       "tpCellDisChgOverTempProtMod1": tpCellDisChgOverTempProtMod1,
       "tpCellDisChgOverTempProtMod2": tpCellDisChgOverTempProtMod2,
       "tpCellDisChgOverTempProtMod3": tpCellDisChgOverTempProtMod3,
       "tpCellDisChgOverTempProtMod4": tpCellDisChgOverTempProtMod4,
       "tpCellDisChgOverTempProtMod5": tpCellDisChgOverTempProtMod5,
       "tpCellDisChgOverTempProtMod6": tpCellDisChgOverTempProtMod6,
       "tpCellDisChgOverTempProtMod7": tpCellDisChgOverTempProtMod7,
       "tpCellDisChgOverTempProtMod8": tpCellDisChgOverTempProtMod8,
       "tpCellDisChgOverTempProtMod9": tpCellDisChgOverTempProtMod9,
       "tpCellDisChgOverTempProtMod10": tpCellDisChgOverTempProtMod10,
       "tpCellDisChgOverTempProtMod11": tpCellDisChgOverTempProtMod11,
       "tpCellDisChgOverTempProtMod12": tpCellDisChgOverTempProtMod12,
       "tpCellDisChgOverTempProtMod13": tpCellDisChgOverTempProtMod13,
       "tpCellDisChgOverTempProtMod14": tpCellDisChgOverTempProtMod14,
       "tpCellDisChgOverTempProtMod15": tpCellDisChgOverTempProtMod15,
       "tpAnyCellUnderTempProtMod1": tpAnyCellUnderTempProtMod1,
       "tpAnyCellUnderTempProtMod2": tpAnyCellUnderTempProtMod2,
       "tpAnyCellUnderTempProtMod3": tpAnyCellUnderTempProtMod3,
       "tpAnyCellUnderTempProtMod4": tpAnyCellUnderTempProtMod4,
       "tpAnyCellUnderTempProtMod5": tpAnyCellUnderTempProtMod5,
       "tpAnyCellUnderTempProtMod6": tpAnyCellUnderTempProtMod6,
       "tpAnyCellUnderTempProtMod7": tpAnyCellUnderTempProtMod7,
       "tpAnyCellUnderTempProtMod8": tpAnyCellUnderTempProtMod8,
       "tpAnyCellUnderTempProtMod9": tpAnyCellUnderTempProtMod9,
       "tpAnyCellUnderTempProtMod10": tpAnyCellUnderTempProtMod10,
       "tpAnyCellUnderTempProtMod11": tpAnyCellUnderTempProtMod11,
       "tpAnyCellUnderTempProtMod12": tpAnyCellUnderTempProtMod12,
       "tpAnyCellUnderTempProtMod13": tpAnyCellUnderTempProtMod13,
       "tpAnyCellUnderTempProtMod14": tpAnyCellUnderTempProtMod14,
       "tpAnyCellUnderTempProtMod15": tpAnyCellUnderTempProtMod15,
       "tpBattChgOverCurrWarningMod1": tpBattChgOverCurrWarningMod1,
       "tpBattChgOverCurrWarningMod2": tpBattChgOverCurrWarningMod2,
       "tpBattChgOverCurrWarningMod3": tpBattChgOverCurrWarningMod3,
       "tpBattChgOverCurrWarningMod4": tpBattChgOverCurrWarningMod4,
       "tpBattChgOverCurrWarningMod5": tpBattChgOverCurrWarningMod5,
       "tpBattChgOverCurrWarningMod6": tpBattChgOverCurrWarningMod6,
       "tpBattChgOverCurrWarningMod7": tpBattChgOverCurrWarningMod7,
       "tpBattChgOverCurrWarningMod8": tpBattChgOverCurrWarningMod8,
       "tpBattChgOverCurrWarningMod9": tpBattChgOverCurrWarningMod9,
       "tpBattChgOverCurrWarningMod10": tpBattChgOverCurrWarningMod10,
       "tpBattChgOverCurrWarningMod11": tpBattChgOverCurrWarningMod11,
       "tpBattChgOverCurrWarningMod12": tpBattChgOverCurrWarningMod12,
       "tpBattChgOverCurrWarningMod13": tpBattChgOverCurrWarningMod13,
       "tpBattChgOverCurrWarningMod14": tpBattChgOverCurrWarningMod14,
       "tpBattChgOverCurrWarningMod15": tpBattChgOverCurrWarningMod15,
       "tpBattDisChgOverCurrWarnMod1": tpBattDisChgOverCurrWarnMod1,
       "tpBattDisChgOverCurrWarnMod2": tpBattDisChgOverCurrWarnMod2,
       "tpBattDisChgOverCurrWarnMod3": tpBattDisChgOverCurrWarnMod3,
       "tpBattDisChgOverCurrWarnMod4": tpBattDisChgOverCurrWarnMod4,
       "tpBattDisChgOverCurrWarnMod5": tpBattDisChgOverCurrWarnMod5,
       "tpBattDisChgOverCurrWarnMod6": tpBattDisChgOverCurrWarnMod6,
       "tpBattDisChgOverCurrWarnMod7": tpBattDisChgOverCurrWarnMod7,
       "tpBattDisChgOverCurrWarnMod8": tpBattDisChgOverCurrWarnMod8,
       "tpBattDisChgOverCurrWarnMod9": tpBattDisChgOverCurrWarnMod9,
       "tpBattDisChgOverCurrWarnMod10": tpBattDisChgOverCurrWarnMod10,
       "tpBattDisChgOverCurrWarnMod11": tpBattDisChgOverCurrWarnMod11,
       "tpBattDisChgOverCurrWarnMod12": tpBattDisChgOverCurrWarnMod12,
       "tpBattDisChgOverCurrWarnMod13": tpBattDisChgOverCurrWarnMod13,
       "tpBattDisChgOverCurrWarnMod14": tpBattDisChgOverCurrWarnMod14,
       "tpBattDisChgOverCurrWarnMod15": tpBattDisChgOverCurrWarnMod15,
       "tpBattLowSOCWarningMod1": tpBattLowSOCWarningMod1,
       "tpBattLowSOCWarningMod2": tpBattLowSOCWarningMod2,
       "tpBattLowSOCWarningMod3": tpBattLowSOCWarningMod3,
       "tpBattLowSOCWarningMod4": tpBattLowSOCWarningMod4,
       "tpBattLowSOCWarningMod5": tpBattLowSOCWarningMod5,
       "tpBattLowSOCWarningMod6": tpBattLowSOCWarningMod6,
       "tpBattLowSOCWarningMod7": tpBattLowSOCWarningMod7,
       "tpBattLowSOCWarningMod8": tpBattLowSOCWarningMod8,
       "tpBattLowSOCWarningMod9": tpBattLowSOCWarningMod9,
       "tpBattLowSOCWarningMod10": tpBattLowSOCWarningMod10,
       "tpBattLowSOCWarningMod11": tpBattLowSOCWarningMod11,
       "tpBattLowSOCWarningMod12": tpBattLowSOCWarningMod12,
       "tpBattLowSOCWarningMod13": tpBattLowSOCWarningMod13,
       "tpBattLowSOCWarningMod14": tpBattLowSOCWarningMod14,
       "tpBattLowSOCWarningMod15": tpBattLowSOCWarningMod15,
       "tpBattOverCurrProtectionMod1": tpBattOverCurrProtectionMod1,
       "tpBattOverCurrProtectionMod2": tpBattOverCurrProtectionMod2,
       "tpBattOverCurrProtectionMod3": tpBattOverCurrProtectionMod3,
       "tpBattOverCurrProtectionMod4": tpBattOverCurrProtectionMod4,
       "tpBattOverCurrProtectionMod5": tpBattOverCurrProtectionMod5,
       "tpBattOverCurrProtectionMod6": tpBattOverCurrProtectionMod6,
       "tpBattOverCurrProtectionMod7": tpBattOverCurrProtectionMod7,
       "tpBattOverCurrProtectionMod8": tpBattOverCurrProtectionMod8,
       "tpBattOverCurrProtectionMod9": tpBattOverCurrProtectionMod9,
       "tpBattOverCurrProtectionMod10": tpBattOverCurrProtectionMod10,
       "tpBattOverCurrProtectionMod11": tpBattOverCurrProtectionMod11,
       "tpBattOverCurrProtectionMod12": tpBattOverCurrProtectionMod12,
       "tpBattOverCurrProtectionMod13": tpBattOverCurrProtectionMod13,
       "tpBattOverCurrProtectionMod14": tpBattOverCurrProtectionMod14,
       "tpBattOverCurrProtectionMod15": tpBattOverCurrProtectionMod15,
       "tpBattOverVolProtectionMod1": tpBattOverVolProtectionMod1,
       "tpBattOverVolProtectionMod2": tpBattOverVolProtectionMod2,
       "tpBattOverVolProtectionMod3": tpBattOverVolProtectionMod3,
       "tpBattOverVolProtectionMod4": tpBattOverVolProtectionMod4,
       "tpBattOverVolProtectionMod5": tpBattOverVolProtectionMod5,
       "tpBattOverVolProtectionMod6": tpBattOverVolProtectionMod6,
       "tpBattOverVolProtectionMod7": tpBattOverVolProtectionMod7,
       "tpBattOverVolProtectionMod8": tpBattOverVolProtectionMod8,
       "tpBattOverVolProtectionMod9": tpBattOverVolProtectionMod9,
       "tpBattOverVolProtectionMod10": tpBattOverVolProtectionMod10,
       "tpBattOverVolProtectionMod11": tpBattOverVolProtectionMod11,
       "tpBattOverVolProtectionMod12": tpBattOverVolProtectionMod12,
       "tpBattOverVolProtectionMod13": tpBattOverVolProtectionMod13,
       "tpBattOverVolProtectionMod14": tpBattOverVolProtectionMod14,
       "tpBattOverVolProtectionMod15": tpBattOverVolProtectionMod15,
       "tpBattUnderVolProtAnyModule": tpBattUnderVolProtAnyModule,
       "tpModule1Isolated": tpModule1Isolated,
       "tpModule2Isolated": tpModule2Isolated,
       "tpModule3Isolated": tpModule3Isolated,
       "tpModule4Isolated": tpModule4Isolated,
       "tpModule5Isolated": tpModule5Isolated,
       "tpModule6Isolated": tpModule6Isolated,
       "tpModule7Isolated": tpModule7Isolated,
       "tpModule8Isolated": tpModule8Isolated,
       "tpModule9Isolated": tpModule9Isolated,
       "tpModule10Isolated": tpModule10Isolated,
       "tpModule11Isolated": tpModule11Isolated,
       "tpModule12Isolated": tpModule12Isolated,
       "tpModule13Isolated": tpModule13Isolated,
       "tpModule14Isolated": tpModule14Isolated,
       "tpModule15Isolated": tpModule15Isolated,
       "tpModule1CommFailAlarm": tpModule1CommFailAlarm,
       "tpModule2CommFailAlarm": tpModule2CommFailAlarm,
       "tpModule3CommFailAlarm": tpModule3CommFailAlarm,
       "tpModule4CommFailAlarm": tpModule4CommFailAlarm,
       "tpModule5CommFailAlarm": tpModule5CommFailAlarm,
       "tpModule6CommFailAlarm": tpModule6CommFailAlarm,
       "tpModule7CommFailAlarm": tpModule7CommFailAlarm,
       "tpModule8CommFailAlarm": tpModule8CommFailAlarm,
       "tpModule9CommFailAlarm": tpModule9CommFailAlarm,
       "tpModule10CommFailAlarm": tpModule10CommFailAlarm,
       "tpModule11CommFailAlarm": tpModule11CommFailAlarm,
       "tpModule12CommFailAlarm": tpModule12CommFailAlarm,
       "tpModule13CommFailAlarm": tpModule13CommFailAlarm,
       "tpModule14CommFailAlarm": tpModule14CommFailAlarm,
       "tpModule15CommFailAlarm": tpModule15CommFailAlarm,
       "tpACPowerfail": tpACPowerfail,
       "tpSingleRectifierModuleFail": tpSingleRectifierModuleFail,
       "tpMultipleRectifierModuleFail": tpMultipleRectifierModuleFail,
       "tpLoadFusetrip": tpLoadFusetrip,
       "tpLLVDAlarm": tpLLVDAlarm,
       "tpBLVDAlarm": tpBLVDAlarm,
       "tpBatteryfuseFail": tpBatteryfuseFail,
       "tpBatteryonLoad": tpBatteryonLoad,
       "tpFireAlarm": tpFireAlarm,
       "tpUPS1Faulty": tpUPS1Faulty,
       "tpUPS1OnBypass": tpUPS1OnBypass,
       "tpUPS2Faulty": tpUPS2Faulty,
       "tpUPS2OnBypass": tpUPS2OnBypass,
       "tpHighTempAlarm": tpHighTempAlarm,
       "internal": internal,
       "internaltraps": internaltraps,
       "tpSystemReset": tpSystemReset,
       "tpPeriodicTrap": tpPeriodicTrap,
       "tpGenericTrap": tpGenericTrap,
       "tpCommFailPCtoSMPS": tpCommFailPCtoSMPS,
       "internalparams": internalparams,
       "eSystemResetCause": eSystemResetCause,
       "ePeriodicTrap": ePeriodicTrap,
       "eGenericTrap": eGenericTrap,
       "devicestatus": devicestatus,
       "eCommFailPCtoSMPS": eCommFailPCtoSMPS,
       "control": control,
       "cTrapResendFlag": cTrapResendFlag,
       "dpsInfo": dpsInfo}
)
