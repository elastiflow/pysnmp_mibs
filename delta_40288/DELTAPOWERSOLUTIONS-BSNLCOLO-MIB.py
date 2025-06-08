# SNMP MIB module (DELTAPOWERSOLUTIONS-BSNLCOLO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/delta_40288/DELTAPOWERSOLUTIONS-BSNLCOLO-MIB.mib
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
_Bsnlcolo_ObjectIdentity = ObjectIdentity
bsnlcolo = _Bsnlcolo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3)
)
_Root_ObjectIdentity = ObjectIdentity
root = _Root_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2)
)
_Ipv4TrapTable_Object = MibTable
ipv4TrapTable = _Ipv4TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipv4TrapTable.setStatus("current")
_Ipv4TrapEntry_Object = MibTableRow
ipv4TrapEntry = _Ipv4TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 1, 1)
)
ipv4TrapEntry.setIndexNames(
    (0, "DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "ipv4TrapReceiverNumber"),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 1, 1, 2),
    _Ipv4TrapEnabled_Type()
)
ipv4TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4TrapEnabled.setStatus("current")
_Ipv4TrapReceiverIPAddress_Type = IpAddress
_Ipv4TrapReceiverIPAddress_Object = MibTableColumn
ipv4TrapReceiverIPAddress = _Ipv4TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 2),
    _Siteid_Type()
)
siteid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteid.setStatus("current")
_Ipv6TrapTable_Object = MibTable
ipv6TrapTable = _Ipv6TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipv6TrapTable.setStatus("current")
_Ipv6TrapEntry_Object = MibTableRow
ipv6TrapEntry = _Ipv6TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 3, 1)
)
ipv6TrapEntry.setIndexNames(
    (0, "DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "ipv6TrapReceiverNumber"),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 2, 3, 1, 4),
    _Ipv6TrapCommunity_Type()
)
ipv6TrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6TrapCommunity.setStatus("current")
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3)
)
_EAlarms_ObjectIdentity = ObjectIdentity
eAlarms = _EAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1)
)
_EAlarmsGp_ObjectIdentity = ObjectIdentity
eAlarmsGp = _EAlarmsGp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1)
)


class _EACPowerFail_Type(Integer32):
    """Custom type eACPowerFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EACPowerFail_Type.__name__ = "Integer32"
_EACPowerFail_Object = MibScalar
eACPowerFail = _EACPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 1),
    _EACPowerFail_Type()
)
eACPowerFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eACPowerFail.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 3),
    _EMultipleRectifierModuleFail_Type()
)
eMultipleRectifierModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMultipleRectifierModuleFail.setStatus("current")


class _EMCBTripLoad1_Type(Integer32):
    """Custom type eMCBTripLoad1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMCBTripLoad1_Type.__name__ = "Integer32"
_EMCBTripLoad1_Object = MibScalar
eMCBTripLoad1 = _EMCBTripLoad1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 4),
    _EMCBTripLoad1_Type()
)
eMCBTripLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMCBTripLoad1.setStatus("current")


class _EMCBTripLoad2_Type(Integer32):
    """Custom type eMCBTripLoad2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMCBTripLoad2_Type.__name__ = "Integer32"
_EMCBTripLoad2_Object = MibScalar
eMCBTripLoad2 = _EMCBTripLoad2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 5),
    _EMCBTripLoad2_Type()
)
eMCBTripLoad2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMCBTripLoad2.setStatus("current")


class _EMCBTripLoad3_Type(Integer32):
    """Custom type eMCBTripLoad3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMCBTripLoad3_Type.__name__ = "Integer32"
_EMCBTripLoad3_Object = MibScalar
eMCBTripLoad3 = _EMCBTripLoad3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 6),
    _EMCBTripLoad3_Type()
)
eMCBTripLoad3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMCBTripLoad3.setStatus("current")


class _EMCBTripLoad4_Type(Integer32):
    """Custom type eMCBTripLoad4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMCBTripLoad4_Type.__name__ = "Integer32"
_EMCBTripLoad4_Object = MibScalar
eMCBTripLoad4 = _EMCBTripLoad4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 7),
    _EMCBTripLoad4_Type()
)
eMCBTripLoad4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMCBTripLoad4.setStatus("current")


class _EMCBTripLoad5_Type(Integer32):
    """Custom type eMCBTripLoad5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMCBTripLoad5_Type.__name__ = "Integer32"
_EMCBTripLoad5_Object = MibScalar
eMCBTripLoad5 = _EMCBTripLoad5_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 8),
    _EMCBTripLoad5_Type()
)
eMCBTripLoad5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMCBTripLoad5.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 10),
    _EBatteryfuseFail_Type()
)
eBatteryfuseFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryfuseFail.setStatus("current")


class _EBatteryOnDischargeorLoadonBattery_Type(Integer32):
    """Custom type eBatteryOnDischargeorLoadonBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryOnDischargeorLoadonBattery_Type.__name__ = "Integer32"
_EBatteryOnDischargeorLoadonBattery_Object = MibScalar
eBatteryOnDischargeorLoadonBattery = _EBatteryOnDischargeorLoadonBattery_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 11),
    _EBatteryOnDischargeorLoadonBattery_Type()
)
eBatteryOnDischargeorLoadonBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryOnDischargeorLoadonBattery.setStatus("current")


class _EFirealarm_Type(Integer32):
    """Custom type eFirealarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EFirealarm_Type.__name__ = "Integer32"
_EFirealarm_Object = MibScalar
eFirealarm = _EFirealarm_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 12),
    _EFirealarm_Type()
)
eFirealarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirealarm.setStatus("current")


class _EDoorOpen_Type(Integer32):
    """Custom type eDoorOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDoorOpen_Type.__name__ = "Integer32"
_EDoorOpen_Object = MibScalar
eDoorOpen = _EDoorOpen_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 13),
    _EDoorOpen_Type()
)
eDoorOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDoorOpen.setStatus("current")


class _EBatterySymmetryFail_Type(Integer32):
    """Custom type eBatterySymmetryFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatterySymmetryFail_Type.__name__ = "Integer32"
_EBatterySymmetryFail_Object = MibScalar
eBatterySymmetryFail = _EBatterySymmetryFail_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 14),
    _EBatterySymmetryFail_Type()
)
eBatterySymmetryFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatterySymmetryFail.setStatus("current")


class _EHighTempBattery1_Type(Integer32):
    """Custom type eHighTempBattery1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighTempBattery1_Type.__name__ = "Integer32"
_EHighTempBattery1_Object = MibScalar
eHighTempBattery1 = _EHighTempBattery1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 15),
    _EHighTempBattery1_Type()
)
eHighTempBattery1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighTempBattery1.setStatus("current")


class _EHighTempBattery2_Type(Integer32):
    """Custom type eHighTempBattery2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighTempBattery2_Type.__name__ = "Integer32"
_EHighTempBattery2_Object = MibScalar
eHighTempBattery2 = _EHighTempBattery2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 16),
    _EHighTempBattery2_Type()
)
eHighTempBattery2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighTempBattery2.setStatus("current")


class _EHighTempCabinet_Type(Integer32):
    """Custom type eHighTempCabinet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EHighTempCabinet_Type.__name__ = "Integer32"
_EHighTempCabinet_Object = MibScalar
eHighTempCabinet = _EHighTempCabinet_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 17),
    _EHighTempCabinet_Type()
)
eHighTempCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eHighTempCabinet.setStatus("current")


class _EExternalHighTemperature_Type(Integer32):
    """Custom type eExternalHighTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EExternalHighTemperature_Type.__name__ = "Integer32"
_EExternalHighTemperature_Object = MibScalar
eExternalHighTemperature = _EExternalHighTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 18),
    _EExternalHighTemperature_Type()
)
eExternalHighTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eExternalHighTemperature.setStatus("current")


class _EBatteryVoltageLow_Type(Integer32):
    """Custom type eBatteryVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryVoltageLow_Type.__name__ = "Integer32"
_EBatteryVoltageLow_Object = MibScalar
eBatteryVoltageLow = _EBatteryVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 19),
    _EBatteryVoltageLow_Type()
)
eBatteryVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryVoltageLow.setStatus("current")


class _ESpareDI1_Type(Integer32):
    """Custom type eSpareDI1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESpareDI1_Type.__name__ = "Integer32"
_ESpareDI1_Object = MibScalar
eSpareDI1 = _ESpareDI1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 20),
    _ESpareDI1_Type()
)
eSpareDI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareDI1.setStatus("current")


class _ESpareDI2_Type(Integer32):
    """Custom type eSpareDI2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESpareDI2_Type.__name__ = "Integer32"
_ESpareDI2_Object = MibScalar
eSpareDI2 = _ESpareDI2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 21),
    _ESpareDI2_Type()
)
eSpareDI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareDI2.setStatus("current")


class _ESpareDI3_Type(Integer32):
    """Custom type eSpareDI3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESpareDI3_Type.__name__ = "Integer32"
_ESpareDI3_Object = MibScalar
eSpareDI3 = _ESpareDI3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 22),
    _ESpareDI3_Type()
)
eSpareDI3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSpareDI3.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 25),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 26),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 27),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 28),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 29),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 30),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 31),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 32),
    _EDGIdleRunning_Type()
)
eDGIdleRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGIdleRunning.setStatus("current")


class _EDGInManualMode_Type(Integer32):
    """Custom type eDGInManualMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGInManualMode_Type.__name__ = "Integer32"
_EDGInManualMode_Object = MibScalar
eDGInManualMode = _EDGInManualMode_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 33),
    _EDGInManualMode_Type()
)
eDGInManualMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGInManualMode.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 34),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 35),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 36),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 37),
    _EDGReserve_Type()
)
eDGReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGReserve.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 38),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 39),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 40),
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 1, 1, 41),
    _EDiffPressureFilterStatus_Type()
)
eDiffPressureFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDiffPressureFilterStatus.setStatus("current")
_EParameters_ObjectIdentity = ObjectIdentity
eParameters = _EParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2)
)
_ESMPSInfo_ObjectIdentity = ObjectIdentity
eSMPSInfo = _ESMPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1)
)


class _EDCBusVoltage_Type(Integer32):
    """Custom type eDCBusVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDCBusVoltage_Type.__name__ = "Integer32"
_EDCBusVoltage_Object = MibScalar
eDCBusVoltage = _EDCBusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 1),
    _EDCBusVoltage_Type()
)
eDCBusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCBusVoltage.setStatus("current")


class _EBatteryCurrent_Type(Integer32):
    """Custom type eBatteryCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryCurrent_Type.__name__ = "Integer32"
_EBatteryCurrent_Object = MibScalar
eBatteryCurrent = _EBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 2),
    _EBatteryCurrent_Type()
)
eBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryCurrent.setStatus("current")


class _ETemperatureBattery1_Type(Integer32):
    """Custom type eTemperatureBattery1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ETemperatureBattery1_Type.__name__ = "Integer32"
_ETemperatureBattery1_Object = MibScalar
eTemperatureBattery1 = _ETemperatureBattery1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 3),
    _ETemperatureBattery1_Type()
)
eTemperatureBattery1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperatureBattery1.setStatus("current")


class _ETemperatureBattery2_Type(Integer32):
    """Custom type eTemperatureBattery2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ETemperatureBattery2_Type.__name__ = "Integer32"
_ETemperatureBattery2_Object = MibScalar
eTemperatureBattery2 = _ETemperatureBattery2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 4),
    _ETemperatureBattery2_Type()
)
eTemperatureBattery2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperatureBattery2.setStatus("current")


class _ECabinetTemperature_Type(Integer32):
    """Custom type eCabinetTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECabinetTemperature_Type.__name__ = "Integer32"
_ECabinetTemperature_Object = MibScalar
eCabinetTemperature = _ECabinetTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 5),
    _ECabinetTemperature_Type()
)
eCabinetTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCabinetTemperature.setStatus("current")


class _ERectifierCurrent_Type(Integer32):
    """Custom type eRectifierCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ERectifierCurrent_Type.__name__ = "Integer32"
_ERectifierCurrent_Object = MibScalar
eRectifierCurrent = _ERectifierCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 6),
    _ERectifierCurrent_Type()
)
eRectifierCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRectifierCurrent.setStatus("current")


class _ERectifierKWH_Type(Integer32):
    """Custom type eRectifierKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ERectifierKWH_Type.__name__ = "Integer32"
_ERectifierKWH_Object = MibScalar
eRectifierKWH = _ERectifierKWH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 7),
    _ERectifierKWH_Type()
)
eRectifierKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRectifierKWH.setStatus("current")


class _ELoadcurrent_Type(Integer32):
    """Custom type eLoadcurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELoadcurrent_Type.__name__ = "Integer32"
_ELoadcurrent_Object = MibScalar
eLoadcurrent = _ELoadcurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 8),
    _ELoadcurrent_Type()
)
eLoadcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadcurrent.setStatus("current")


class _ENoofrectifierspoweredup_Type(Integer32):
    """Custom type eNoofrectifierspoweredup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ENoofrectifierspoweredup_Type.__name__ = "Integer32"
_ENoofrectifierspoweredup_Object = MibScalar
eNoofrectifierspoweredup = _ENoofrectifierspoweredup_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 9),
    _ENoofrectifierspoweredup_Type()
)
eNoofrectifierspoweredup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eNoofrectifierspoweredup.setStatus("current")


class _EBatteryKWh_Type(Integer32):
    """Custom type eBatteryKWh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryKWh_Type.__name__ = "Integer32"
_EBatteryKWh_Object = MibScalar
eBatteryKWh = _EBatteryKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 10),
    _EBatteryKWh_Type()
)
eBatteryKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryKWh.setStatus("current")


class _EDCOutputPower_Type(Integer32):
    """Custom type eDCOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDCOutputPower_Type.__name__ = "Integer32"
_EDCOutputPower_Object = MibScalar
eDCOutputPower = _EDCOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 11),
    _EDCOutputPower_Type()
)
eDCOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDCOutputPower.setStatus("current")


class _ELoadKWh_Type(Integer32):
    """Custom type eLoadKWh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ELoadKWh_Type.__name__ = "Integer32"
_ELoadKWh_Object = MibScalar
eLoadKWh = _ELoadKWh_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 12),
    _ELoadKWh_Type()
)
eLoadKWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLoadKWh.setStatus("current")


class _EFloatVoltage_Type(Integer32):
    """Custom type eFloatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EFloatVoltage_Type.__name__ = "Integer32"
_EFloatVoltage_Object = MibScalar
eFloatVoltage = _EFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 13),
    _EFloatVoltage_Type()
)
eFloatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFloatVoltage.setStatus("current")


class _EBoostVoltage_Type(Integer32):
    """Custom type eBoostVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBoostVoltage_Type.__name__ = "Integer32"
_EBoostVoltage_Object = MibScalar
eBoostVoltage = _EBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 14),
    _EBoostVoltage_Type()
)
eBoostVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBoostVoltage.setStatus("current")


class _EBatteryChargeCurrentLimit_Type(Integer32):
    """Custom type eBatteryChargeCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBatteryChargeCurrentLimit_Type.__name__ = "Integer32"
_EBatteryChargeCurrentLimit_Object = MibScalar
eBatteryChargeCurrentLimit = _EBatteryChargeCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 15),
    _EBatteryChargeCurrentLimit_Type()
)
eBatteryChargeCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBatteryChargeCurrentLimit.setStatus("current")


class _EBLVDVoltage_Type(Integer32):
    """Custom type eBLVDVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EBLVDVoltage_Type.__name__ = "Integer32"
_EBLVDVoltage_Object = MibScalar
eBLVDVoltage = _EBLVDVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 16),
    _EBLVDVoltage_Type()
)
eBLVDVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eBLVDVoltage.setStatus("current")


class _EManufacturerName_Type(Integer32):
    """Custom type eManufacturerName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EManufacturerName_Type.__name__ = "Integer32"
_EManufacturerName_Object = MibScalar
eManufacturerName = _EManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 17),
    _EManufacturerName_Type()
)
eManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eManufacturerName.setStatus("current")


class _EFirmwareVersion_Type(Integer32):
    """Custom type eFirmwareVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EFirmwareVersion_Type.__name__ = "Integer32"
_EFirmwareVersion_Object = MibScalar
eFirmwareVersion = _EFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 1, 18),
    _EFirmwareVersion_Type()
)
eFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirmwareVersion.setStatus("current")
_EACEMInfo_ObjectIdentity = ObjectIdentity
eACEMInfo = _EACEMInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2)
)


class _EPowerKWMeter1_Type(Integer32):
    """Custom type ePowerKWMeter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPowerKWMeter1_Type.__name__ = "Integer32"
_EPowerKWMeter1_Object = MibScalar
ePowerKWMeter1 = _EPowerKWMeter1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 1),
    _EPowerKWMeter1_Type()
)
ePowerKWMeter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter1.setStatus("current")


class _EEnergyKWHMeter1_Type(Integer32):
    """Custom type eEnergyKWHMeter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEnergyKWHMeter1_Type.__name__ = "Integer32"
_EEnergyKWHMeter1_Object = MibScalar
eEnergyKWHMeter1 = _EEnergyKWHMeter1_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 2),
    _EEnergyKWHMeter1_Type()
)
eEnergyKWHMeter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter1.setStatus("current")


class _EPowerKWMeter2_Type(Integer32):
    """Custom type ePowerKWMeter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPowerKWMeter2_Type.__name__ = "Integer32"
_EPowerKWMeter2_Object = MibScalar
ePowerKWMeter2 = _EPowerKWMeter2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 3),
    _EPowerKWMeter2_Type()
)
ePowerKWMeter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter2.setStatus("current")


class _EEnergyKWHMeter2_Type(Integer32):
    """Custom type eEnergyKWHMeter2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEnergyKWHMeter2_Type.__name__ = "Integer32"
_EEnergyKWHMeter2_Object = MibScalar
eEnergyKWHMeter2 = _EEnergyKWHMeter2_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 4),
    _EEnergyKWHMeter2_Type()
)
eEnergyKWHMeter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter2.setStatus("current")


class _EPowerKWMeter3_Type(Integer32):
    """Custom type ePowerKWMeter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPowerKWMeter3_Type.__name__ = "Integer32"
_EPowerKWMeter3_Object = MibScalar
ePowerKWMeter3 = _EPowerKWMeter3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 5),
    _EPowerKWMeter3_Type()
)
ePowerKWMeter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter3.setStatus("current")


class _EEnergyKWHMeter3_Type(Integer32):
    """Custom type eEnergyKWHMeter3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEnergyKWHMeter3_Type.__name__ = "Integer32"
_EEnergyKWHMeter3_Object = MibScalar
eEnergyKWHMeter3 = _EEnergyKWHMeter3_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 6),
    _EEnergyKWHMeter3_Type()
)
eEnergyKWHMeter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter3.setStatus("current")


class _EPowerKWMeter4_Type(Integer32):
    """Custom type ePowerKWMeter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPowerKWMeter4_Type.__name__ = "Integer32"
_EPowerKWMeter4_Object = MibScalar
ePowerKWMeter4 = _EPowerKWMeter4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 7),
    _EPowerKWMeter4_Type()
)
ePowerKWMeter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePowerKWMeter4.setStatus("current")


class _EEnergyKWHMeter4_Type(Integer32):
    """Custom type eEnergyKWHMeter4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EEnergyKWHMeter4_Type.__name__ = "Integer32"
_EEnergyKWHMeter4_Object = MibScalar
eEnergyKWHMeter4 = _EEnergyKWHMeter4_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 8),
    _EEnergyKWHMeter4_Type()
)
eEnergyKWHMeter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eEnergyKWHMeter4.setStatus("current")


class _EInputLineAVoltage_Type(Integer32):
    """Custom type eInputLineAVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInputLineAVoltage_Type.__name__ = "Integer32"
_EInputLineAVoltage_Object = MibScalar
eInputLineAVoltage = _EInputLineAVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 9),
    _EInputLineAVoltage_Type()
)
eInputLineAVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineAVoltage.setStatus("current")


class _EInputLineBVoltage_Type(Integer32):
    """Custom type eInputLineBVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInputLineBVoltage_Type.__name__ = "Integer32"
_EInputLineBVoltage_Object = MibScalar
eInputLineBVoltage = _EInputLineBVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 10),
    _EInputLineBVoltage_Type()
)
eInputLineBVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineBVoltage.setStatus("current")


class _EInputLineCVoltage_Type(Integer32):
    """Custom type eInputLineCVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInputLineCVoltage_Type.__name__ = "Integer32"
_EInputLineCVoltage_Object = MibScalar
eInputLineCVoltage = _EInputLineCVoltage_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 11),
    _EInputLineCVoltage_Type()
)
eInputLineCVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineCVoltage.setStatus("current")


class _EInputLineACurrent_Type(Integer32):
    """Custom type eInputLineACurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInputLineACurrent_Type.__name__ = "Integer32"
_EInputLineACurrent_Object = MibScalar
eInputLineACurrent = _EInputLineACurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 12),
    _EInputLineACurrent_Type()
)
eInputLineACurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineACurrent.setStatus("current")


class _EInputLineBCurrent_Type(Integer32):
    """Custom type eInputLineBCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInputLineBCurrent_Type.__name__ = "Integer32"
_EInputLineBCurrent_Object = MibScalar
eInputLineBCurrent = _EInputLineBCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 13),
    _EInputLineBCurrent_Type()
)
eInputLineBCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineBCurrent.setStatus("current")


class _EInputLineCCurrent_Type(Integer32):
    """Custom type eInputLineCCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EInputLineCCurrent_Type.__name__ = "Integer32"
_EInputLineCCurrent_Object = MibScalar
eInputLineCCurrent = _EInputLineCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 2, 14),
    _EInputLineCCurrent_Type()
)
eInputLineCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eInputLineCCurrent.setStatus("current")
_EDGInfo_ObjectIdentity = ObjectIdentity
eDGInfo = _EDGInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3)
)


class _EDGLubeOilPressure_Type(Integer32):
    """Custom type eDGLubeOilPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGLubeOilPressure_Type.__name__ = "Integer32"
_EDGLubeOilPressure_Object = MibScalar
eDGLubeOilPressure = _EDGLubeOilPressure_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 1),
    _EDGLubeOilPressure_Type()
)
eDGLubeOilPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGLubeOilPressure.setStatus("current")


class _EChargingAlternatorVoltageDC_Type(Integer32):
    """Custom type eChargingAlternatorVoltageDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EChargingAlternatorVoltageDC_Type.__name__ = "Integer32"
_EChargingAlternatorVoltageDC_Object = MibScalar
eChargingAlternatorVoltageDC = _EChargingAlternatorVoltageDC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 2),
    _EChargingAlternatorVoltageDC_Type()
)
eChargingAlternatorVoltageDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargingAlternatorVoltageDC.setStatus("current")


class _EDGKWH_Type(Integer32):
    """Custom type eDGKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGKWH_Type.__name__ = "Integer32"
_EDGKWH_Object = MibScalar
eDGKWH = _EDGKWH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 3),
    _EDGKWH_Type()
)
eDGKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGKWH.setStatus("current")


class _ESWBKWH_Type(Integer32):
    """Custom type eSWBKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESWBKWH_Type.__name__ = "Integer32"
_ESWBKWH_Object = MibScalar
eSWBKWH = _ESWBKWH_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 4),
    _ESWBKWH_Type()
)
eSWBKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWBKWH.setStatus("current")


class _EDGRunHrs_Type(Integer32):
    """Custom type eDGRunHrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGRunHrs_Type.__name__ = "Integer32"
_EDGRunHrs_Object = MibScalar
eDGRunHrs = _EDGRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 5),
    _EDGRunHrs_Type()
)
eDGRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGRunHrs.setStatus("current")


class _EMainsRKW_Type(Integer32):
    """Custom type eMainsRKW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMainsRKW_Type.__name__ = "Integer32"
_EMainsRKW_Object = MibScalar
eMainsRKW = _EMainsRKW_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 6),
    _EMainsRKW_Type()
)
eMainsRKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsRKW.setStatus("current")


class _EMainsYKW_Type(Integer32):
    """Custom type eMainsYKW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMainsYKW_Type.__name__ = "Integer32"
_EMainsYKW_Object = MibScalar
eMainsYKW = _EMainsYKW_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 7),
    _EMainsYKW_Type()
)
eMainsYKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsYKW.setStatus("current")


class _EMainsBKW_Type(Integer32):
    """Custom type eMainsBKW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EMainsBKW_Type.__name__ = "Integer32"
_EMainsBKW_Object = MibScalar
eMainsBKW = _EMainsBKW_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 8),
    _EMainsBKW_Type()
)
eMainsBKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMainsBKW.setStatus("current")


class _EDGRKW_Type(Integer32):
    """Custom type eDGRKW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGRKW_Type.__name__ = "Integer32"
_EDGRKW_Object = MibScalar
eDGRKW = _EDGRKW_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 9),
    _EDGRKW_Type()
)
eDGRKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGRKW.setStatus("current")


class _EDGYKW_Type(Integer32):
    """Custom type eDGYKW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGYKW_Type.__name__ = "Integer32"
_EDGYKW_Object = MibScalar
eDGYKW = _EDGYKW_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 10),
    _EDGYKW_Type()
)
eDGYKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGYKW.setStatus("current")


class _EDGBKW_Type(Integer32):
    """Custom type eDGBKW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGBKW_Type.__name__ = "Integer32"
_EDGBKW_Object = MibScalar
eDGBKW = _EDGBKW_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 11),
    _EDGBKW_Type()
)
eDGBKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGBKW.setStatus("current")


class _EDGFuelLevelLitre_Type(Integer32):
    """Custom type eDGFuelLevelLitre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EDGFuelLevelLitre_Type.__name__ = "Integer32"
_EDGFuelLevelLitre_Object = MibScalar
eDGFuelLevelLitre = _EDGFuelLevelLitre_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 3, 12),
    _EDGFuelLevelLitre_Type()
)
eDGFuelLevelLitre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDGFuelLevelLitre.setStatus("current")
_EPACInfo_ObjectIdentity = ObjectIdentity
ePACInfo = _EPACInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 4)
)


class _ESupplyAirTemperature_Type(Integer32):
    """Custom type eSupplyAirTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ESupplyAirTemperature_Type.__name__ = "Integer32"
_ESupplyAirTemperature_Object = MibScalar
eSupplyAirTemperature = _ESupplyAirTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 4, 1),
    _ESupplyAirTemperature_Type()
)
eSupplyAirTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSupplyAirTemperature.setStatus("current")


class _EReturnAirTempearture_Type(Integer32):
    """Custom type eReturnAirTempearture based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EReturnAirTempearture_Type.__name__ = "Integer32"
_EReturnAirTempearture_Object = MibScalar
eReturnAirTempearture = _EReturnAirTempearture_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 4, 2),
    _EReturnAirTempearture_Type()
)
eReturnAirTempearture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eReturnAirTempearture.setStatus("current")


class _ECHWControlValveOutput_Type(Integer32):
    """Custom type eCHWControlValveOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ECHWControlValveOutput_Type.__name__ = "Integer32"
_ECHWControlValveOutput_Object = MibScalar
eCHWControlValveOutput = _ECHWControlValveOutput_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 4, 3),
    _ECHWControlValveOutput_Type()
)
eCHWControlValveOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCHWControlValveOutput.setStatus("current")


class _EPACUnitRunHours_Type(Integer32):
    """Custom type ePACUnitRunHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_EPACUnitRunHours_Type.__name__ = "Integer32"
_EPACUnitRunHours_Object = MibScalar
ePACUnitRunHours = _EPACUnitRunHours_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 3, 2, 4, 4),
    _EPACUnitRunHours_Type()
)
ePACUnitRunHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePACUnitRunHours.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11)
)
_Internaltraps_ObjectIdentity = ObjectIdentity
internaltraps = _Internaltraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 1)
)
_Devicestatus_ObjectIdentity = ObjectIdentity
devicestatus = _Devicestatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 3)
)


class _ECommFailSMPS_Type(Integer32):
    """Custom type eCommFailSMPS based on Integer32"""
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


_ECommFailSMPS_Type.__name__ = "Integer32"
_ECommFailSMPS_Object = MibScalar
eCommFailSMPS = _ECommFailSMPS_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 3, 1),
    _ECommFailSMPS_Type()
)
eCommFailSMPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailSMPS.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 3, 2),
    _ECommFailACEM_Type()
)
eCommFailACEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailACEM.setStatus("current")


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
          ("noCommunication", 0),
          ("communicationOK", 1))
    )


_ECommFailDGController_Type.__name__ = "Integer32"
_ECommFailDGController_Object = MibScalar
eCommFailDGController = _ECommFailDGController_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 3, 3),
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
          ("noCommunication", 0),
          ("communicationOK", 1))
    )


_ECommFailPAC_Type.__name__ = "Integer32"
_ECommFailPAC_Object = MibScalar
eCommFailPAC = _ECommFailPAC_Object(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 3, 4),
    _ECommFailPAC_Type()
)
eCommFailPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCommFailPAC.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 12)
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
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 12, 1),
    _CTrapResendFlag_Type()
)
cTrapResendFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTrapResendFlag.setStatus("current")

# Managed Objects groups


# Notification objects

tpACPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 1)
)
tpACPowerFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eACPowerFail"))
)
if mibBuilder.loadTexts:
    tpACPowerFail.setStatus(
        "current"
    )

tpSingleRectifierModuleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 2)
)
tpSingleRectifierModuleFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eSingleRectifierModuleFail"))
)
if mibBuilder.loadTexts:
    tpSingleRectifierModuleFail.setStatus(
        "current"
    )

tpMultipleRectifierModuleFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 3)
)
tpMultipleRectifierModuleFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eMultipleRectifierModuleFail"))
)
if mibBuilder.loadTexts:
    tpMultipleRectifierModuleFail.setStatus(
        "current"
    )

tpMCBTripLoad1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 4)
)
tpMCBTripLoad1.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eMCBTripLoad1"))
)
if mibBuilder.loadTexts:
    tpMCBTripLoad1.setStatus(
        "current"
    )

tpMCBTripLoad2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 5)
)
tpMCBTripLoad2.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eMCBTripLoad2"))
)
if mibBuilder.loadTexts:
    tpMCBTripLoad2.setStatus(
        "current"
    )

tpMCBTripLoad3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 6)
)
tpMCBTripLoad3.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eMCBTripLoad3"))
)
if mibBuilder.loadTexts:
    tpMCBTripLoad3.setStatus(
        "current"
    )

tpMCBTripLoad4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 7)
)
tpMCBTripLoad4.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eMCBTripLoad4"))
)
if mibBuilder.loadTexts:
    tpMCBTripLoad4.setStatus(
        "current"
    )

tpMCBTripLoad5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 8)
)
tpMCBTripLoad5.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eMCBTripLoad5"))
)
if mibBuilder.loadTexts:
    tpMCBTripLoad5.setStatus(
        "current"
    )

tpBLVDAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 9)
)
tpBLVDAlarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eBLVDAlarm"))
)
if mibBuilder.loadTexts:
    tpBLVDAlarm.setStatus(
        "current"
    )

tpBatteryfuseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 10)
)
tpBatteryfuseFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eBatteryfuseFail"))
)
if mibBuilder.loadTexts:
    tpBatteryfuseFail.setStatus(
        "current"
    )

tpBatteryOnDischargeorLoadonBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 11)
)
tpBatteryOnDischargeorLoadonBattery.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eBatteryOnDischargeorLoadonBattery"))
)
if mibBuilder.loadTexts:
    tpBatteryOnDischargeorLoadonBattery.setStatus(
        "current"
    )

tpFirealarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 12)
)
tpFirealarm.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eFirealarm"))
)
if mibBuilder.loadTexts:
    tpFirealarm.setStatus(
        "current"
    )

tpDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 13)
)
tpDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDoorOpen"))
)
if mibBuilder.loadTexts:
    tpDoorOpen.setStatus(
        "current"
    )

tpBatterySymmetryFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 14)
)
tpBatterySymmetryFail.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eBatterySymmetryFail"))
)
if mibBuilder.loadTexts:
    tpBatterySymmetryFail.setStatus(
        "current"
    )

tpHighTempBattery1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 15)
)
tpHighTempBattery1.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eHighTempBattery1"))
)
if mibBuilder.loadTexts:
    tpHighTempBattery1.setStatus(
        "current"
    )

tpHighTempBattery2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 16)
)
tpHighTempBattery2.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eHighTempBattery2"))
)
if mibBuilder.loadTexts:
    tpHighTempBattery2.setStatus(
        "current"
    )

tpHighTempCabinet = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 17)
)
tpHighTempCabinet.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eHighTempCabinet"))
)
if mibBuilder.loadTexts:
    tpHighTempCabinet.setStatus(
        "current"
    )

tpExternalHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 18)
)
tpExternalHighTemperature.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eExternalHighTemperature"))
)
if mibBuilder.loadTexts:
    tpExternalHighTemperature.setStatus(
        "current"
    )

tpBatteryVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 19)
)
tpBatteryVoltageLow.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eBatteryVoltageLow"))
)
if mibBuilder.loadTexts:
    tpBatteryVoltageLow.setStatus(
        "current"
    )

tpSpareDI1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 20)
)
tpSpareDI1.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eSpareDI1"))
)
if mibBuilder.loadTexts:
    tpSpareDI1.setStatus(
        "current"
    )

tpSpareDI2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 21)
)
tpSpareDI2.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eSpareDI2"))
)
if mibBuilder.loadTexts:
    tpSpareDI2.setStatus(
        "current"
    )

tpSpareDI3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 22)
)
tpSpareDI3.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eSpareDI3"))
)
if mibBuilder.loadTexts:
    tpSpareDI3.setStatus(
        "current"
    )

tpDGFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 23)
)
tpDGFailToStart.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGFailToStart"))
)
if mibBuilder.loadTexts:
    tpDGFailToStart.setStatus(
        "current"
    )

tpDGCanopyTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 24)
)
tpDGCanopyTempHigh.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGCanopyTempHigh"))
)
if mibBuilder.loadTexts:
    tpDGCanopyTempHigh.setStatus(
        "current"
    )

tpDGLowFuelLevelWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 25)
)
tpDGLowFuelLevelWarning.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGLowFuelLevelWarning"))
)
if mibBuilder.loadTexts:
    tpDGLowFuelLevelWarning.setStatus(
        "current"
    )

tpDGLowFuelLevelTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 26)
)
tpDGLowFuelLevelTrip.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGLowFuelLevelTrip"))
)
if mibBuilder.loadTexts:
    tpDGLowFuelLevelTrip.setStatus(
        "current"
    )

tpDGUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 27)
)
tpDGUnderFrequency.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGUnderFrequency"))
)
if mibBuilder.loadTexts:
    tpDGUnderFrequency.setStatus(
        "current"
    )

tpDGCommonFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 28)
)
tpDGCommonFault.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGCommonFault"))
)
if mibBuilder.loadTexts:
    tpDGCommonFault.setStatus(
        "current"
    )

tpDGOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 29)
)
tpDGOverload.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGOverload"))
)
if mibBuilder.loadTexts:
    tpDGOverload.setStatus(
        "current"
    )

tpLoadOnDG = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 30)
)
tpLoadOnDG.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eLoadOnDG"))
)
if mibBuilder.loadTexts:
    tpLoadOnDG.setStatus(
        "current"
    )

tpDGEngineOverSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 31)
)
tpDGEngineOverSpeed.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGEngineOverSpeed"))
)
if mibBuilder.loadTexts:
    tpDGEngineOverSpeed.setStatus(
        "current"
    )

tpDGIdleRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 32)
)
tpDGIdleRunning.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGIdleRunning"))
)
if mibBuilder.loadTexts:
    tpDGIdleRunning.setStatus(
        "current"
    )

tpDGInManualMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 33)
)
tpDGInManualMode.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGInManualMode"))
)
if mibBuilder.loadTexts:
    tpDGInManualMode.setStatus(
        "current"
    )

tpDGBatteryChargerFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 34)
)
tpDGBatteryChargerFaulty.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGBatteryChargerFaulty"))
)
if mibBuilder.loadTexts:
    tpDGBatteryChargerFaulty.setStatus(
        "current"
    )

tpDGCanopyDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 35)
)
tpDGCanopyDoorOpen.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGCanopyDoorOpen"))
)
if mibBuilder.loadTexts:
    tpDGCanopyDoorOpen.setStatus(
        "current"
    )

tpDGLLOP = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 36)
)
tpDGLLOP.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGLLOP"))
)
if mibBuilder.loadTexts:
    tpDGLLOP.setStatus(
        "current"
    )

tpDGReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 37)
)
tpDGReserve.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDGReserve"))
)
if mibBuilder.loadTexts:
    tpDGReserve.setStatus(
        "current"
    )

tpPACFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 38)
)
tpPACFault.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "ePACFault"))
)
if mibBuilder.loadTexts:
    tpPACFault.setStatus(
        "current"
    )

tpPACRunStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 39)
)
tpPACRunStatus.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "ePACRunStatus"))
)
if mibBuilder.loadTexts:
    tpPACRunStatus.setStatus(
        "current"
    )

tpPACTripStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 40)
)
tpPACTripStatus.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "ePACTripStatus"))
)
if mibBuilder.loadTexts:
    tpPACTripStatus.setStatus(
        "current"
    )

tpDiffPressureFilterStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 10, 41)
)
tpDiffPressureFilterStatus.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eDiffPressureFilterStatus"))
)
if mibBuilder.loadTexts:
    tpDiffPressureFilterStatus.setStatus(
        "current"
    )

tpCommFailSMPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 1, 7)
)
tpCommFailSMPS.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eCommFailSMPS"))
)
if mibBuilder.loadTexts:
    tpCommFailSMPS.setStatus(
        "current"
    )

tpCommFailACEM = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 1, 8)
)
tpCommFailACEM.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eCommFailACEM"))
)
if mibBuilder.loadTexts:
    tpCommFailACEM.setStatus(
        "current"
    )

tpCommFailDGController = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 1, 10)
)
tpCommFailDGController.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eCommFailDGController"))
)
if mibBuilder.loadTexts:
    tpCommFailDGController.setStatus(
        "current"
    )

tpCommFailPAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 40288, 1, 3, 1, 11, 1, 11)
)
tpCommFailPAC.setObjects(
      *(("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "siteid"),
        ("DELTAPOWERSOLUTIONS-BSNLCOLO-MIB", "eCommFailPAC"))
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
    "DELTAPOWERSOLUTIONS-BSNLCOLO-MIB",
    **{"DPSUsmAuthPrivProtocol": DPSUsmAuthPrivProtocol,
       "deltapowersolutions": deltapowersolutions,
       "products": products,
       "bsnlcolo": bsnlcolo,
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
       "eACPowerFail": eACPowerFail,
       "eSingleRectifierModuleFail": eSingleRectifierModuleFail,
       "eMultipleRectifierModuleFail": eMultipleRectifierModuleFail,
       "eMCBTripLoad1": eMCBTripLoad1,
       "eMCBTripLoad2": eMCBTripLoad2,
       "eMCBTripLoad3": eMCBTripLoad3,
       "eMCBTripLoad4": eMCBTripLoad4,
       "eMCBTripLoad5": eMCBTripLoad5,
       "eBLVDAlarm": eBLVDAlarm,
       "eBatteryfuseFail": eBatteryfuseFail,
       "eBatteryOnDischargeorLoadonBattery": eBatteryOnDischargeorLoadonBattery,
       "eFirealarm": eFirealarm,
       "eDoorOpen": eDoorOpen,
       "eBatterySymmetryFail": eBatterySymmetryFail,
       "eHighTempBattery1": eHighTempBattery1,
       "eHighTempBattery2": eHighTempBattery2,
       "eHighTempCabinet": eHighTempCabinet,
       "eExternalHighTemperature": eExternalHighTemperature,
       "eBatteryVoltageLow": eBatteryVoltageLow,
       "eSpareDI1": eSpareDI1,
       "eSpareDI2": eSpareDI2,
       "eSpareDI3": eSpareDI3,
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
       "eDGInManualMode": eDGInManualMode,
       "eDGBatteryChargerFaulty": eDGBatteryChargerFaulty,
       "eDGCanopyDoorOpen": eDGCanopyDoorOpen,
       "eDGLLOP": eDGLLOP,
       "eDGReserve": eDGReserve,
       "ePACFault": ePACFault,
       "ePACRunStatus": ePACRunStatus,
       "ePACTripStatus": ePACTripStatus,
       "eDiffPressureFilterStatus": eDiffPressureFilterStatus,
       "eParameters": eParameters,
       "eSMPSInfo": eSMPSInfo,
       "eDCBusVoltage": eDCBusVoltage,
       "eBatteryCurrent": eBatteryCurrent,
       "eTemperatureBattery1": eTemperatureBattery1,
       "eTemperatureBattery2": eTemperatureBattery2,
       "eCabinetTemperature": eCabinetTemperature,
       "eRectifierCurrent": eRectifierCurrent,
       "eRectifierKWH": eRectifierKWH,
       "eLoadcurrent": eLoadcurrent,
       "eNoofrectifierspoweredup": eNoofrectifierspoweredup,
       "eBatteryKWh": eBatteryKWh,
       "eDCOutputPower": eDCOutputPower,
       "eLoadKWh": eLoadKWh,
       "eFloatVoltage": eFloatVoltage,
       "eBoostVoltage": eBoostVoltage,
       "eBatteryChargeCurrentLimit": eBatteryChargeCurrentLimit,
       "eBLVDVoltage": eBLVDVoltage,
       "eManufacturerName": eManufacturerName,
       "eFirmwareVersion": eFirmwareVersion,
       "eACEMInfo": eACEMInfo,
       "ePowerKWMeter1": ePowerKWMeter1,
       "eEnergyKWHMeter1": eEnergyKWHMeter1,
       "ePowerKWMeter2": ePowerKWMeter2,
       "eEnergyKWHMeter2": eEnergyKWHMeter2,
       "ePowerKWMeter3": ePowerKWMeter3,
       "eEnergyKWHMeter3": eEnergyKWHMeter3,
       "ePowerKWMeter4": ePowerKWMeter4,
       "eEnergyKWHMeter4": eEnergyKWHMeter4,
       "eInputLineAVoltage": eInputLineAVoltage,
       "eInputLineBVoltage": eInputLineBVoltage,
       "eInputLineCVoltage": eInputLineCVoltage,
       "eInputLineACurrent": eInputLineACurrent,
       "eInputLineBCurrent": eInputLineBCurrent,
       "eInputLineCCurrent": eInputLineCCurrent,
       "eDGInfo": eDGInfo,
       "eDGLubeOilPressure": eDGLubeOilPressure,
       "eChargingAlternatorVoltageDC": eChargingAlternatorVoltageDC,
       "eDGKWH": eDGKWH,
       "eSWBKWH": eSWBKWH,
       "eDGRunHrs": eDGRunHrs,
       "eMainsRKW": eMainsRKW,
       "eMainsYKW": eMainsYKW,
       "eMainsBKW": eMainsBKW,
       "eDGRKW": eDGRKW,
       "eDGYKW": eDGYKW,
       "eDGBKW": eDGBKW,
       "eDGFuelLevelLitre": eDGFuelLevelLitre,
       "ePACInfo": ePACInfo,
       "eSupplyAirTemperature": eSupplyAirTemperature,
       "eReturnAirTempearture": eReturnAirTempearture,
       "eCHWControlValveOutput": eCHWControlValveOutput,
       "ePACUnitRunHours": ePACUnitRunHours,
       "trapNotifications": trapNotifications,
       "tpACPowerFail": tpACPowerFail,
       "tpSingleRectifierModuleFail": tpSingleRectifierModuleFail,
       "tpMultipleRectifierModuleFail": tpMultipleRectifierModuleFail,
       "tpMCBTripLoad1": tpMCBTripLoad1,
       "tpMCBTripLoad2": tpMCBTripLoad2,
       "tpMCBTripLoad3": tpMCBTripLoad3,
       "tpMCBTripLoad4": tpMCBTripLoad4,
       "tpMCBTripLoad5": tpMCBTripLoad5,
       "tpBLVDAlarm": tpBLVDAlarm,
       "tpBatteryfuseFail": tpBatteryfuseFail,
       "tpBatteryOnDischargeorLoadonBattery": tpBatteryOnDischargeorLoadonBattery,
       "tpFirealarm": tpFirealarm,
       "tpDoorOpen": tpDoorOpen,
       "tpBatterySymmetryFail": tpBatterySymmetryFail,
       "tpHighTempBattery1": tpHighTempBattery1,
       "tpHighTempBattery2": tpHighTempBattery2,
       "tpHighTempCabinet": tpHighTempCabinet,
       "tpExternalHighTemperature": tpExternalHighTemperature,
       "tpBatteryVoltageLow": tpBatteryVoltageLow,
       "tpSpareDI1": tpSpareDI1,
       "tpSpareDI2": tpSpareDI2,
       "tpSpareDI3": tpSpareDI3,
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
       "tpDGInManualMode": tpDGInManualMode,
       "tpDGBatteryChargerFaulty": tpDGBatteryChargerFaulty,
       "tpDGCanopyDoorOpen": tpDGCanopyDoorOpen,
       "tpDGLLOP": tpDGLLOP,
       "tpDGReserve": tpDGReserve,
       "tpPACFault": tpPACFault,
       "tpPACRunStatus": tpPACRunStatus,
       "tpPACTripStatus": tpPACTripStatus,
       "tpDiffPressureFilterStatus": tpDiffPressureFilterStatus,
       "internal": internal,
       "internaltraps": internaltraps,
       "tpCommFailSMPS": tpCommFailSMPS,
       "tpCommFailACEM": tpCommFailACEM,
       "tpCommFailDGController": tpCommFailDGController,
       "tpCommFailPAC": tpCommFailPAC,
       "devicestatus": devicestatus,
       "eCommFailSMPS": eCommFailSMPS,
       "eCommFailACEM": eCommFailACEM,
       "eCommFailDGController": eCommFailDGController,
       "eCommFailPAC": eCommFailPAC,
       "control": control,
       "cTrapResendFlag": cTrapResendFlag,
       "dpsInfo": dpsInfo}
)
