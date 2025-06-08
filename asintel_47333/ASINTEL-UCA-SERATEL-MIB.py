# SNMP MIB module (ASINTEL-UCA-SERATEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/asintel_47333/ASINTEL-UCA-SERATEL-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:36:11 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asintel_ObjectIdentity = ObjectIdentity
asintel = _Asintel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333)
)
_UcaSeratel_ObjectIdentity = ObjectIdentity
ucaSeratel = _UcaSeratel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1)
)
_NetworkConfiguration_ObjectIdentity = ObjectIdentity
networkConfiguration = _NetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0)
)
_IpConfig_ObjectIdentity = ObjectIdentity
ipConfig = _IpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 1)
)
_IpConfiguration_Type = IpAddress
_IpConfiguration_Object = MibScalar
ipConfiguration = _IpConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 1, 1),
    _IpConfiguration_Type()
)
ipConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfiguration.setStatus("mandatory")
_MaskConfiguration_Type = IpAddress
_MaskConfiguration_Object = MibScalar
maskConfiguration = _MaskConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 1, 2),
    _MaskConfiguration_Type()
)
maskConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskConfiguration.setStatus("mandatory")
_GatewayConfiguration_Type = IpAddress
_GatewayConfiguration_Object = MibScalar
gatewayConfiguration = _GatewayConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 1, 3),
    _GatewayConfiguration_Type()
)
gatewayConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayConfiguration.setStatus("mandatory")
_DnsAddressConfiguration_Type = IpAddress
_DnsAddressConfiguration_Object = MibScalar
dnsAddressConfiguration = _DnsAddressConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 1, 4),
    _DnsAddressConfiguration_Type()
)
dnsAddressConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsAddressConfiguration.setStatus("mandatory")
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2)
)
_TrapRemoteHostIP1_Type = IpAddress
_TrapRemoteHostIP1_Object = MibScalar
trapRemoteHostIP1 = _TrapRemoteHostIP1_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 1),
    _TrapRemoteHostIP1_Type()
)
trapRemoteHostIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRemoteHostIP1.setStatus("mandatory")
_TrapRemoteHostIP2_Type = IpAddress
_TrapRemoteHostIP2_Object = MibScalar
trapRemoteHostIP2 = _TrapRemoteHostIP2_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 2),
    _TrapRemoteHostIP2_Type()
)
trapRemoteHostIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRemoteHostIP2.setStatus("mandatory")
_TrapRemoteHostIP3_Type = IpAddress
_TrapRemoteHostIP3_Object = MibScalar
trapRemoteHostIP3 = _TrapRemoteHostIP3_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 3),
    _TrapRemoteHostIP3_Type()
)
trapRemoteHostIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRemoteHostIP3.setStatus("mandatory")
_TrapRemoteHostIP4_Type = IpAddress
_TrapRemoteHostIP4_Object = MibScalar
trapRemoteHostIP4 = _TrapRemoteHostIP4_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 4),
    _TrapRemoteHostIP4_Type()
)
trapRemoteHostIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRemoteHostIP4.setStatus("mandatory")
_AliveInterval_Type = Integer32
_AliveInterval_Object = MibScalar
aliveInterval = _AliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 5),
    _AliveInterval_Type()
)
aliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aliveInterval.setStatus("mandatory")


class _AliveEnable_Type(Integer32):
    """Custom type aliveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AliveEnable_Type.__name__ = "Integer32"
_AliveEnable_Object = MibScalar
aliveEnable = _AliveEnable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 6),
    _AliveEnable_Type()
)
aliveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aliveEnable.setStatus("mandatory")


class _TrapsEnable_Type(Integer32):
    """Custom type trapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TrapsEnable_Type.__name__ = "Integer32"
_TrapsEnable_Object = MibScalar
trapsEnable = _TrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 7),
    _TrapsEnable_Type()
)
trapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsEnable.setStatus("mandatory")
_PasswordRead_Type = DisplayString
_PasswordRead_Object = MibScalar
passwordRead = _PasswordRead_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 8),
    _PasswordRead_Type()
)
passwordRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordRead.setStatus("mandatory")
_PasswordWrite_Type = DisplayString
_PasswordWrite_Object = MibScalar
passwordWrite = _PasswordWrite_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 2, 9),
    _PasswordWrite_Type()
)
passwordWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordWrite.setStatus("mandatory")
_SntpConfig_ObjectIdentity = ObjectIdentity
sntpConfig = _SntpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 3)
)
_SntpServer1IP_Type = IpAddress
_SntpServer1IP_Object = MibScalar
sntpServer1IP = _SntpServer1IP_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 3, 1),
    _SntpServer1IP_Type()
)
sntpServer1IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer1IP.setStatus("mandatory")
_SntpServer2IP_Type = IpAddress
_SntpServer2IP_Object = MibScalar
sntpServer2IP = _SntpServer2IP_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 3, 2),
    _SntpServer2IP_Type()
)
sntpServer2IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer2IP.setStatus("mandatory")
_SntpServer3IP_Type = IpAddress
_SntpServer3IP_Object = MibScalar
sntpServer3IP = _SntpServer3IP_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 3, 3),
    _SntpServer3IP_Type()
)
sntpServer3IP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServer3IP.setStatus("mandatory")
_SntpSyncInterval_Type = Integer32
_SntpSyncInterval_Object = MibScalar
sntpSyncInterval = _SntpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 3, 4),
    _SntpSyncInterval_Type()
)
sntpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSyncInterval.setStatus("mandatory")


class _SntpSyncEnable_Type(Integer32):
    """Custom type sntpSyncEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SntpSyncEnable_Type.__name__ = "Integer32"
_SntpSyncEnable_Object = MibScalar
sntpSyncEnable = _SntpSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 3, 5),
    _SntpSyncEnable_Type()
)
sntpSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSyncEnable.setStatus("mandatory")
_UnitConfiguration_ObjectIdentity = ObjectIdentity
unitConfiguration = _UnitConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1)
)
_TxConfig_ObjectIdentity = ObjectIdentity
txConfig = _TxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1)
)
_Tx1Config_ObjectIdentity = ObjectIdentity
tx1Config = _Tx1Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 1)
)


class _Tx1Enable_Type(Integer32):
    """Custom type tx1Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_Tx1Enable_Type.__name__ = "Integer32"
_Tx1Enable_Object = MibScalar
tx1Enable = _Tx1Enable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 1, 1),
    _Tx1Enable_Type()
)
tx1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1Enable.setStatus("mandatory")


class _Tx1Priority_Type(Integer32):
    """Custom type tx1Priority based on Integer32"""
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
        *(("noPriority", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_Tx1Priority_Type.__name__ = "Integer32"
_Tx1Priority_Object = MibScalar
tx1Priority = _Tx1Priority_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 1, 2),
    _Tx1Priority_Type()
)
tx1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1Priority.setStatus("mandatory")
_Tx1TimePrev_Type = Integer32
_Tx1TimePrev_Object = MibScalar
tx1TimePrev = _Tx1TimePrev_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 1, 3),
    _Tx1TimePrev_Type()
)
tx1TimePrev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1TimePrev.setStatus("mandatory")
_Tx1TimePost_Type = Integer32
_Tx1TimePost_Object = MibScalar
tx1TimePost = _Tx1TimePost_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 1, 4),
    _Tx1TimePost_Type()
)
tx1TimePost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1TimePost.setStatus("mandatory")
_Tx2Config_ObjectIdentity = ObjectIdentity
tx2Config = _Tx2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 2)
)


class _Tx2Enable_Type(Integer32):
    """Custom type tx2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_Tx2Enable_Type.__name__ = "Integer32"
_Tx2Enable_Object = MibScalar
tx2Enable = _Tx2Enable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 2, 1),
    _Tx2Enable_Type()
)
tx2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2Enable.setStatus("mandatory")


class _Tx2Priority_Type(Integer32):
    """Custom type tx2Priority based on Integer32"""
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
        *(("noPriority", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_Tx2Priority_Type.__name__ = "Integer32"
_Tx2Priority_Object = MibScalar
tx2Priority = _Tx2Priority_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 2, 2),
    _Tx2Priority_Type()
)
tx2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2Priority.setStatus("mandatory")
_Tx2TimePrev_Type = Integer32
_Tx2TimePrev_Object = MibScalar
tx2TimePrev = _Tx2TimePrev_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 2, 3),
    _Tx2TimePrev_Type()
)
tx2TimePrev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2TimePrev.setStatus("mandatory")
_Tx2TimePost_Type = Integer32
_Tx2TimePost_Object = MibScalar
tx2TimePost = _Tx2TimePost_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 2, 4),
    _Tx2TimePost_Type()
)
tx2TimePost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2TimePost.setStatus("mandatory")
_Tx3Config_ObjectIdentity = ObjectIdentity
tx3Config = _Tx3Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 3)
)


class _Tx3Enable_Type(Integer32):
    """Custom type tx3Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_Tx3Enable_Type.__name__ = "Integer32"
_Tx3Enable_Object = MibScalar
tx3Enable = _Tx3Enable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 3, 1),
    _Tx3Enable_Type()
)
tx3Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3Enable.setStatus("mandatory")


class _Tx3Priority_Type(Integer32):
    """Custom type tx3Priority based on Integer32"""
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
        *(("noPriority", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_Tx3Priority_Type.__name__ = "Integer32"
_Tx3Priority_Object = MibScalar
tx3Priority = _Tx3Priority_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 3, 2),
    _Tx3Priority_Type()
)
tx3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3Priority.setStatus("mandatory")
_Tx3TimePrev_Type = Integer32
_Tx3TimePrev_Object = MibScalar
tx3TimePrev = _Tx3TimePrev_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 3, 3),
    _Tx3TimePrev_Type()
)
tx3TimePrev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3TimePrev.setStatus("mandatory")
_Tx3TimePost_Type = Integer32
_Tx3TimePost_Object = MibScalar
tx3TimePost = _Tx3TimePost_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 3, 4),
    _Tx3TimePost_Type()
)
tx3TimePost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3TimePost.setStatus("mandatory")
_Tx4Config_ObjectIdentity = ObjectIdentity
tx4Config = _Tx4Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 4)
)


class _Tx4Enable_Type(Integer32):
    """Custom type tx4Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_Tx4Enable_Type.__name__ = "Integer32"
_Tx4Enable_Object = MibScalar
tx4Enable = _Tx4Enable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 4, 1),
    _Tx4Enable_Type()
)
tx4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4Enable.setStatus("mandatory")


class _Tx4Priority_Type(Integer32):
    """Custom type tx4Priority based on Integer32"""
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
        *(("noPriority", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_Tx4Priority_Type.__name__ = "Integer32"
_Tx4Priority_Object = MibScalar
tx4Priority = _Tx4Priority_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 4, 2),
    _Tx4Priority_Type()
)
tx4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4Priority.setStatus("mandatory")
_Tx4TimePrev_Type = Integer32
_Tx4TimePrev_Object = MibScalar
tx4TimePrev = _Tx4TimePrev_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 4, 3),
    _Tx4TimePrev_Type()
)
tx4TimePrev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4TimePrev.setStatus("mandatory")
_Tx4TimePost_Type = Integer32
_Tx4TimePost_Object = MibScalar
tx4TimePost = _Tx4TimePost_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 4, 4),
    _Tx4TimePost_Type()
)
tx4TimePost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4TimePost.setStatus("mandatory")
_Tx5Config_ObjectIdentity = ObjectIdentity
tx5Config = _Tx5Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 5)
)


class _Tx5Enable_Type(Integer32):
    """Custom type tx5Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_Tx5Enable_Type.__name__ = "Integer32"
_Tx5Enable_Object = MibScalar
tx5Enable = _Tx5Enable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 5, 1),
    _Tx5Enable_Type()
)
tx5Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5Enable.setStatus("mandatory")


class _Tx5Priority_Type(Integer32):
    """Custom type tx5Priority based on Integer32"""
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
        *(("noPriority", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3))
    )


_Tx5Priority_Type.__name__ = "Integer32"
_Tx5Priority_Object = MibScalar
tx5Priority = _Tx5Priority_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 5, 2),
    _Tx5Priority_Type()
)
tx5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5Priority.setStatus("mandatory")
_Tx5TimePrev_Type = Integer32
_Tx5TimePrev_Object = MibScalar
tx5TimePrev = _Tx5TimePrev_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 5, 3),
    _Tx5TimePrev_Type()
)
tx5TimePrev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5TimePrev.setStatus("mandatory")
_Tx5TimePost_Type = Integer32
_Tx5TimePost_Object = MibScalar
tx5TimePost = _Tx5TimePost_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 5, 4),
    _Tx5TimePost_Type()
)
tx5TimePost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5TimePost.setStatus("mandatory")
_TxRvaConfig_ObjectIdentity = ObjectIdentity
txRvaConfig = _TxRvaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 6)
)


class _TxRvaProg_Type(Integer32):
    """Custom type txRvaProg based on Integer32"""
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
        *(("tx1", 1),
          ("tx2", 2),
          ("tx3", 3),
          ("tx4", 4),
          ("tx5", 5),
          ("txRva", 6))
    )


_TxRvaProg_Type.__name__ = "Integer32"
_TxRvaProg_Object = MibScalar
txRvaProg = _TxRvaProg_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 1, 6, 1),
    _TxRvaProg_Type()
)
txRvaProg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txRvaProg.setStatus("mandatory")
_UcaName_Type = DisplayString
_UcaName_Object = MibScalar
ucaName = _UcaName_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 2),
    _UcaName_Type()
)
ucaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaName.setStatus("mandatory")
_UcaSerialNumber_Type = DisplayString
_UcaSerialNumber_Object = MibScalar
ucaSerialNumber = _UcaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 3),
    _UcaSerialNumber_Type()
)
ucaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucaSerialNumber.setStatus("mandatory")
_UcaPassword_Type = DisplayString
_UcaPassword_Object = MibScalar
ucaPassword = _UcaPassword_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 4),
    _UcaPassword_Type()
)
ucaPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaPassword.setStatus("mandatory")


class _TxInstalledNumber_Type(Integer32):
    """Custom type txInstalledNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tx1andRVA", 1),
          ("tx2andRVA", 2),
          ("tx3andRVA", 3),
          ("tx4andRVA", 4),
          ("tx5andRVA", 5))
    )


_TxInstalledNumber_Type.__name__ = "Integer32"
_TxInstalledNumber_Object = MibScalar
txInstalledNumber = _TxInstalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 5),
    _TxInstalledNumber_Type()
)
txInstalledNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txInstalledNumber.setStatus("mandatory")


class _UcaPriorityEnable_Type(Integer32):
    """Custom type ucaPriorityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UcaPriorityEnable_Type.__name__ = "Integer32"
_UcaPriorityEnable_Object = MibScalar
ucaPriorityEnable = _UcaPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 6),
    _UcaPriorityEnable_Type()
)
ucaPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaPriorityEnable.setStatus("mandatory")
_MaxRetries_Type = Integer32
_MaxRetries_Object = MibScalar
maxRetries = _MaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 7),
    _MaxRetries_Type()
)
maxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxRetries.setStatus("mandatory")
_TimeBetweenRetries_Type = Integer32
_TimeBetweenRetries_Object = MibScalar
timeBetweenRetries = _TimeBetweenRetries_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 8),
    _TimeBetweenRetries_Type()
)
timeBetweenRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeBetweenRetries.setStatus("mandatory")


class _UcaAutoProgram_Type(Integer32):
    """Custom type ucaAutoProgram based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UcaAutoProgram_Type.__name__ = "Integer32"
_UcaAutoProgram_Object = MibScalar
ucaAutoProgram = _UcaAutoProgram_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 1, 9),
    _UcaAutoProgram_Type()
)
ucaAutoProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaAutoProgram.setStatus("mandatory")
_UnitControl_ObjectIdentity = ObjectIdentity
unitControl = _UnitControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2)
)
_TxControl_ObjectIdentity = ObjectIdentity
txControl = _TxControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1)
)
_Tx1Control_ObjectIdentity = ObjectIdentity
tx1Control = _Tx1Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 1)
)


class _Tx1ResetTX_Type(Integer32):
    """Custom type tx1ResetTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Tx1ResetTX_Type.__name__ = "Integer32"
_Tx1ResetTX_Object = MibScalar
tx1ResetTX = _Tx1ResetTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 1, 1),
    _Tx1ResetTX_Type()
)
tx1ResetTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1ResetTX.setStatus("mandatory")


class _Tx1StartStopTX_Type(Integer32):
    """Custom type tx1StartStopTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerOFF", 0),
          ("powerON", 1))
    )


_Tx1StartStopTX_Type.__name__ = "Integer32"
_Tx1StartStopTX_Object = MibScalar
tx1StartStopTX = _Tx1StartStopTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 1, 2),
    _Tx1StartStopTX_Type()
)
tx1StartStopTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1StartStopTX.setStatus("mandatory")


class _Tx1LoadTX_Type(Integer32):
    """Custom type tx1LoadTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_Tx1LoadTX_Type.__name__ = "Integer32"
_Tx1LoadTX_Object = MibScalar
tx1LoadTX = _Tx1LoadTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 1, 3),
    _Tx1LoadTX_Type()
)
tx1LoadTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx1LoadTX.setStatus("mandatory")
_Tx2Control_ObjectIdentity = ObjectIdentity
tx2Control = _Tx2Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 2)
)


class _Tx2ResetTX_Type(Integer32):
    """Custom type tx2ResetTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Tx2ResetTX_Type.__name__ = "Integer32"
_Tx2ResetTX_Object = MibScalar
tx2ResetTX = _Tx2ResetTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 2, 1),
    _Tx2ResetTX_Type()
)
tx2ResetTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2ResetTX.setStatus("mandatory")


class _Tx2StartStopTX_Type(Integer32):
    """Custom type tx2StartStopTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerOFF", 0),
          ("powerON", 1))
    )


_Tx2StartStopTX_Type.__name__ = "Integer32"
_Tx2StartStopTX_Object = MibScalar
tx2StartStopTX = _Tx2StartStopTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 2, 2),
    _Tx2StartStopTX_Type()
)
tx2StartStopTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2StartStopTX.setStatus("mandatory")


class _Tx2LoadTX_Type(Integer32):
    """Custom type tx2LoadTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_Tx2LoadTX_Type.__name__ = "Integer32"
_Tx2LoadTX_Object = MibScalar
tx2LoadTX = _Tx2LoadTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 2, 3),
    _Tx2LoadTX_Type()
)
tx2LoadTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx2LoadTX.setStatus("mandatory")
_Tx3Control_ObjectIdentity = ObjectIdentity
tx3Control = _Tx3Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 3)
)


class _Tx3ResetTX_Type(Integer32):
    """Custom type tx3ResetTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Tx3ResetTX_Type.__name__ = "Integer32"
_Tx3ResetTX_Object = MibScalar
tx3ResetTX = _Tx3ResetTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 3, 1),
    _Tx3ResetTX_Type()
)
tx3ResetTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3ResetTX.setStatus("mandatory")


class _Tx3StartStopTX_Type(Integer32):
    """Custom type tx3StartStopTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerOFF", 0),
          ("powerON", 1))
    )


_Tx3StartStopTX_Type.__name__ = "Integer32"
_Tx3StartStopTX_Object = MibScalar
tx3StartStopTX = _Tx3StartStopTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 3, 2),
    _Tx3StartStopTX_Type()
)
tx3StartStopTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3StartStopTX.setStatus("mandatory")


class _Tx3LoadTX_Type(Integer32):
    """Custom type tx3LoadTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_Tx3LoadTX_Type.__name__ = "Integer32"
_Tx3LoadTX_Object = MibScalar
tx3LoadTX = _Tx3LoadTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 3, 3),
    _Tx3LoadTX_Type()
)
tx3LoadTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx3LoadTX.setStatus("mandatory")
_Tx4Control_ObjectIdentity = ObjectIdentity
tx4Control = _Tx4Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 4)
)


class _Tx4ResetTX_Type(Integer32):
    """Custom type tx4ResetTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Tx4ResetTX_Type.__name__ = "Integer32"
_Tx4ResetTX_Object = MibScalar
tx4ResetTX = _Tx4ResetTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 4, 1),
    _Tx4ResetTX_Type()
)
tx4ResetTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4ResetTX.setStatus("mandatory")


class _Tx4StartStopTX_Type(Integer32):
    """Custom type tx4StartStopTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerOFF", 0),
          ("powerON", 1))
    )


_Tx4StartStopTX_Type.__name__ = "Integer32"
_Tx4StartStopTX_Object = MibScalar
tx4StartStopTX = _Tx4StartStopTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 4, 2),
    _Tx4StartStopTX_Type()
)
tx4StartStopTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4StartStopTX.setStatus("mandatory")


class _Tx4LoadTX_Type(Integer32):
    """Custom type tx4LoadTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_Tx4LoadTX_Type.__name__ = "Integer32"
_Tx4LoadTX_Object = MibScalar
tx4LoadTX = _Tx4LoadTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 4, 3),
    _Tx4LoadTX_Type()
)
tx4LoadTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx4LoadTX.setStatus("mandatory")
_Tx5Control_ObjectIdentity = ObjectIdentity
tx5Control = _Tx5Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 5)
)


class _Tx5ResetTX_Type(Integer32):
    """Custom type tx5ResetTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Tx5ResetTX_Type.__name__ = "Integer32"
_Tx5ResetTX_Object = MibScalar
tx5ResetTX = _Tx5ResetTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 5, 1),
    _Tx5ResetTX_Type()
)
tx5ResetTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5ResetTX.setStatus("mandatory")


class _Tx5StartStopTX_Type(Integer32):
    """Custom type tx5StartStopTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerOFF", 0),
          ("powerON", 1))
    )


_Tx5StartStopTX_Type.__name__ = "Integer32"
_Tx5StartStopTX_Object = MibScalar
tx5StartStopTX = _Tx5StartStopTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 5, 2),
    _Tx5StartStopTX_Type()
)
tx5StartStopTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5StartStopTX.setStatus("mandatory")


class _Tx5LoadTX_Type(Integer32):
    """Custom type tx5LoadTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_Tx5LoadTX_Type.__name__ = "Integer32"
_Tx5LoadTX_Object = MibScalar
tx5LoadTX = _Tx5LoadTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 5, 3),
    _Tx5LoadTX_Type()
)
tx5LoadTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tx5LoadTX.setStatus("mandatory")
_TxRvaControl_ObjectIdentity = ObjectIdentity
txRvaControl = _TxRvaControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 6)
)


class _TxRvaResetTX_Type(Integer32):
    """Custom type txRvaResetTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_TxRvaResetTX_Type.__name__ = "Integer32"
_TxRvaResetTX_Object = MibScalar
txRvaResetTX = _TxRvaResetTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 6, 1),
    _TxRvaResetTX_Type()
)
txRvaResetTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txRvaResetTX.setStatus("mandatory")


class _TxRvaStartStopTX_Type(Integer32):
    """Custom type txRvaStartStopTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerOFF", 0),
          ("powerON", 1))
    )


_TxRvaStartStopTX_Type.__name__ = "Integer32"
_TxRvaStartStopTX_Object = MibScalar
txRvaStartStopTX = _TxRvaStartStopTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 6, 2),
    _TxRvaStartStopTX_Type()
)
txRvaStartStopTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txRvaStartStopTX.setStatus("mandatory")


class _TxRvaLoadTX_Type(Integer32):
    """Custom type txRvaLoadTX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_TxRvaLoadTX_Type.__name__ = "Integer32"
_TxRvaLoadTX_Object = MibScalar
txRvaLoadTX = _TxRvaLoadTX_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 1, 6, 3),
    _TxRvaLoadTX_Type()
)
txRvaLoadTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    txRvaLoadTX.setStatus("mandatory")


class _UcaReset_Type(Integer32):
    """Custom type ucaReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_UcaReset_Type.__name__ = "Integer32"
_UcaReset_Object = MibScalar
ucaReset = _UcaReset_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 2),
    _UcaReset_Type()
)
ucaReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaReset.setStatus("mandatory")


class _UcaAutoManual_Type(Integer32):
    """Custom type ucaAutoManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manual", 1))
    )


_UcaAutoManual_Type.__name__ = "Integer32"
_UcaAutoManual_Object = MibScalar
ucaAutoManual = _UcaAutoManual_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 3),
    _UcaAutoManual_Type()
)
ucaAutoManual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaAutoManual.setStatus("mandatory")


class _UcaInitialize_Type(Integer32):
    """Custom type ucaInitialize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initialize", 1)
    )


_UcaInitialize_Type.__name__ = "Integer32"
_UcaInitialize_Object = MibScalar
ucaInitialize = _UcaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 4),
    _UcaInitialize_Type()
)
ucaInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaInitialize.setStatus("mandatory")


class _UcaForceRemote_Type(Integer32):
    """Custom type ucaForceRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("forceRemote", 1)
    )


_UcaForceRemote_Type.__name__ = "Integer32"
_UcaForceRemote_Object = MibScalar
ucaForceRemote = _UcaForceRemote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 2, 5),
    _UcaForceRemote_Type()
)
ucaForceRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ucaForceRemote.setStatus("mandatory")
_UnitStatus_ObjectIdentity = ObjectIdentity
unitStatus = _UnitStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3)
)
_TxStatus_ObjectIdentity = ObjectIdentity
txStatus = _TxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1)
)
_Tx1Status_ObjectIdentity = ObjectIdentity
tx1Status = _Tx1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1)
)


class _Tx1Start_Type(Integer32):
    """Custom type tx1Start based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_Tx1Start_Type.__name__ = "Integer32"
_Tx1Start_Object = MibScalar
tx1Start = _Tx1Start_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 1),
    _Tx1Start_Type()
)
tx1Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Start.setStatus("mandatory")


class _Tx1Remote_Type(Integer32):
    """Custom type tx1Remote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_Tx1Remote_Type.__name__ = "Integer32"
_Tx1Remote_Object = MibScalar
tx1Remote = _Tx1Remote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 2),
    _Tx1Remote_Type()
)
tx1Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Remote.setStatus("mandatory")


class _Tx1Warning_Type(Integer32):
    """Custom type tx1Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_Tx1Warning_Type.__name__ = "Integer32"
_Tx1Warning_Object = MibScalar
tx1Warning = _Tx1Warning_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 3),
    _Tx1Warning_Type()
)
tx1Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Warning.setStatus("mandatory")


class _Tx1PowerSupply_Type(Integer32):
    """Custom type tx1PowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_Tx1PowerSupply_Type.__name__ = "Integer32"
_Tx1PowerSupply_Object = MibScalar
tx1PowerSupply = _Tx1PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 4),
    _Tx1PowerSupply_Type()
)
tx1PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1PowerSupply.setStatus("mandatory")


class _Tx1Alarm_Type(Integer32):
    """Custom type tx1Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_Tx1Alarm_Type.__name__ = "Integer32"
_Tx1Alarm_Object = MibScalar
tx1Alarm = _Tx1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 5),
    _Tx1Alarm_Type()
)
tx1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Alarm.setStatus("mandatory")


class _Tx1OnAir_Type(Integer32):
    """Custom type tx1OnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overLoad", 0),
          ("onAir", 1))
    )


_Tx1OnAir_Type.__name__ = "Integer32"
_Tx1OnAir_Object = MibScalar
tx1OnAir = _Tx1OnAir_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 6),
    _Tx1OnAir_Type()
)
tx1OnAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1OnAir.setStatus("mandatory")


class _Tx1Available_Type(Integer32):
    """Custom type tx1Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 0),
          ("available", 1))
    )


_Tx1Available_Type.__name__ = "Integer32"
_Tx1Available_Object = MibScalar
tx1Available = _Tx1Available_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 7),
    _Tx1Available_Type()
)
tx1Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Available.setStatus("mandatory")


class _Tx1Commutation_Type(Integer32):
    """Custom type tx1Commutation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commutationFail", 0),
          ("commutationNotFail", 1))
    )


_Tx1Commutation_Type.__name__ = "Integer32"
_Tx1Commutation_Object = MibScalar
tx1Commutation = _Tx1Commutation_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 8),
    _Tx1Commutation_Type()
)
tx1Commutation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Commutation.setStatus("mandatory")


class _Tx1Interlock_Type(Integer32):
    """Custom type tx1Interlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_Tx1Interlock_Type.__name__ = "Integer32"
_Tx1Interlock_Object = MibScalar
tx1Interlock = _Tx1Interlock_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 9),
    _Tx1Interlock_Type()
)
tx1Interlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Interlock.setStatus("mandatory")


class _Tx1Clamp_Type(Integer32):
    """Custom type tx1Clamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_Tx1Clamp_Type.__name__ = "Integer32"
_Tx1Clamp_Object = MibScalar
tx1Clamp = _Tx1Clamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 1, 10),
    _Tx1Clamp_Type()
)
tx1Clamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx1Clamp.setStatus("mandatory")
_Tx2Status_ObjectIdentity = ObjectIdentity
tx2Status = _Tx2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2)
)


class _Tx2Start_Type(Integer32):
    """Custom type tx2Start based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_Tx2Start_Type.__name__ = "Integer32"
_Tx2Start_Object = MibScalar
tx2Start = _Tx2Start_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 1),
    _Tx2Start_Type()
)
tx2Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Start.setStatus("mandatory")


class _Tx2Remote_Type(Integer32):
    """Custom type tx2Remote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_Tx2Remote_Type.__name__ = "Integer32"
_Tx2Remote_Object = MibScalar
tx2Remote = _Tx2Remote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 2),
    _Tx2Remote_Type()
)
tx2Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Remote.setStatus("mandatory")


class _Tx2Warning_Type(Integer32):
    """Custom type tx2Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_Tx2Warning_Type.__name__ = "Integer32"
_Tx2Warning_Object = MibScalar
tx2Warning = _Tx2Warning_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 3),
    _Tx2Warning_Type()
)
tx2Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Warning.setStatus("mandatory")


class _Tx2PowerSupply_Type(Integer32):
    """Custom type tx2PowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_Tx2PowerSupply_Type.__name__ = "Integer32"
_Tx2PowerSupply_Object = MibScalar
tx2PowerSupply = _Tx2PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 4),
    _Tx2PowerSupply_Type()
)
tx2PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2PowerSupply.setStatus("mandatory")


class _Tx2Alarm_Type(Integer32):
    """Custom type tx2Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_Tx2Alarm_Type.__name__ = "Integer32"
_Tx2Alarm_Object = MibScalar
tx2Alarm = _Tx2Alarm_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 5),
    _Tx2Alarm_Type()
)
tx2Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Alarm.setStatus("mandatory")


class _Tx2OnAir_Type(Integer32):
    """Custom type tx2OnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overLoad", 0),
          ("onAir", 1))
    )


_Tx2OnAir_Type.__name__ = "Integer32"
_Tx2OnAir_Object = MibScalar
tx2OnAir = _Tx2OnAir_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 6),
    _Tx2OnAir_Type()
)
tx2OnAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2OnAir.setStatus("mandatory")


class _Tx2Available_Type(Integer32):
    """Custom type tx2Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 0),
          ("available", 1))
    )


_Tx2Available_Type.__name__ = "Integer32"
_Tx2Available_Object = MibScalar
tx2Available = _Tx2Available_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 7),
    _Tx2Available_Type()
)
tx2Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Available.setStatus("mandatory")


class _Tx2Commutation_Type(Integer32):
    """Custom type tx2Commutation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commutationFail", 0),
          ("commutationNotFail", 1))
    )


_Tx2Commutation_Type.__name__ = "Integer32"
_Tx2Commutation_Object = MibScalar
tx2Commutation = _Tx2Commutation_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 8),
    _Tx2Commutation_Type()
)
tx2Commutation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Commutation.setStatus("mandatory")


class _Tx2Interlock_Type(Integer32):
    """Custom type tx2Interlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_Tx2Interlock_Type.__name__ = "Integer32"
_Tx2Interlock_Object = MibScalar
tx2Interlock = _Tx2Interlock_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 9),
    _Tx2Interlock_Type()
)
tx2Interlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Interlock.setStatus("mandatory")


class _Tx2Clamp_Type(Integer32):
    """Custom type tx2Clamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_Tx2Clamp_Type.__name__ = "Integer32"
_Tx2Clamp_Object = MibScalar
tx2Clamp = _Tx2Clamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 2, 10),
    _Tx2Clamp_Type()
)
tx2Clamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx2Clamp.setStatus("mandatory")
_Tx3Status_ObjectIdentity = ObjectIdentity
tx3Status = _Tx3Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3)
)


class _Tx3Start_Type(Integer32):
    """Custom type tx3Start based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_Tx3Start_Type.__name__ = "Integer32"
_Tx3Start_Object = MibScalar
tx3Start = _Tx3Start_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 1),
    _Tx3Start_Type()
)
tx3Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Start.setStatus("mandatory")


class _Tx3Remote_Type(Integer32):
    """Custom type tx3Remote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_Tx3Remote_Type.__name__ = "Integer32"
_Tx3Remote_Object = MibScalar
tx3Remote = _Tx3Remote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 2),
    _Tx3Remote_Type()
)
tx3Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Remote.setStatus("mandatory")


class _Tx3Warning_Type(Integer32):
    """Custom type tx3Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_Tx3Warning_Type.__name__ = "Integer32"
_Tx3Warning_Object = MibScalar
tx3Warning = _Tx3Warning_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 3),
    _Tx3Warning_Type()
)
tx3Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Warning.setStatus("mandatory")


class _Tx3PowerSupply_Type(Integer32):
    """Custom type tx3PowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_Tx3PowerSupply_Type.__name__ = "Integer32"
_Tx3PowerSupply_Object = MibScalar
tx3PowerSupply = _Tx3PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 4),
    _Tx3PowerSupply_Type()
)
tx3PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3PowerSupply.setStatus("mandatory")


class _Tx3Alarm_Type(Integer32):
    """Custom type tx3Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_Tx3Alarm_Type.__name__ = "Integer32"
_Tx3Alarm_Object = MibScalar
tx3Alarm = _Tx3Alarm_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 5),
    _Tx3Alarm_Type()
)
tx3Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Alarm.setStatus("mandatory")


class _Tx3OnAir_Type(Integer32):
    """Custom type tx3OnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overLoad", 0),
          ("onAir", 1))
    )


_Tx3OnAir_Type.__name__ = "Integer32"
_Tx3OnAir_Object = MibScalar
tx3OnAir = _Tx3OnAir_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 6),
    _Tx3OnAir_Type()
)
tx3OnAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3OnAir.setStatus("mandatory")


class _Tx3Available_Type(Integer32):
    """Custom type tx3Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 0),
          ("available", 1))
    )


_Tx3Available_Type.__name__ = "Integer32"
_Tx3Available_Object = MibScalar
tx3Available = _Tx3Available_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 7),
    _Tx3Available_Type()
)
tx3Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Available.setStatus("mandatory")


class _Tx3Commutation_Type(Integer32):
    """Custom type tx3Commutation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commutationFail", 0),
          ("commutationNotFail", 1))
    )


_Tx3Commutation_Type.__name__ = "Integer32"
_Tx3Commutation_Object = MibScalar
tx3Commutation = _Tx3Commutation_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 8),
    _Tx3Commutation_Type()
)
tx3Commutation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Commutation.setStatus("mandatory")


class _Tx3Interlock_Type(Integer32):
    """Custom type tx3Interlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_Tx3Interlock_Type.__name__ = "Integer32"
_Tx3Interlock_Object = MibScalar
tx3Interlock = _Tx3Interlock_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 9),
    _Tx3Interlock_Type()
)
tx3Interlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Interlock.setStatus("mandatory")


class _Tx3Clamp_Type(Integer32):
    """Custom type tx3Clamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_Tx3Clamp_Type.__name__ = "Integer32"
_Tx3Clamp_Object = MibScalar
tx3Clamp = _Tx3Clamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 3, 10),
    _Tx3Clamp_Type()
)
tx3Clamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx3Clamp.setStatus("mandatory")
_Tx4Status_ObjectIdentity = ObjectIdentity
tx4Status = _Tx4Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4)
)


class _Tx4Start_Type(Integer32):
    """Custom type tx4Start based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_Tx4Start_Type.__name__ = "Integer32"
_Tx4Start_Object = MibScalar
tx4Start = _Tx4Start_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 1),
    _Tx4Start_Type()
)
tx4Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Start.setStatus("mandatory")


class _Tx4Remote_Type(Integer32):
    """Custom type tx4Remote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_Tx4Remote_Type.__name__ = "Integer32"
_Tx4Remote_Object = MibScalar
tx4Remote = _Tx4Remote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 2),
    _Tx4Remote_Type()
)
tx4Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Remote.setStatus("mandatory")


class _Tx4Warning_Type(Integer32):
    """Custom type tx4Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_Tx4Warning_Type.__name__ = "Integer32"
_Tx4Warning_Object = MibScalar
tx4Warning = _Tx4Warning_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 3),
    _Tx4Warning_Type()
)
tx4Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Warning.setStatus("mandatory")


class _Tx4PowerSupply_Type(Integer32):
    """Custom type tx4PowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_Tx4PowerSupply_Type.__name__ = "Integer32"
_Tx4PowerSupply_Object = MibScalar
tx4PowerSupply = _Tx4PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 4),
    _Tx4PowerSupply_Type()
)
tx4PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4PowerSupply.setStatus("mandatory")


class _Tx4Alarm_Type(Integer32):
    """Custom type tx4Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_Tx4Alarm_Type.__name__ = "Integer32"
_Tx4Alarm_Object = MibScalar
tx4Alarm = _Tx4Alarm_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 5),
    _Tx4Alarm_Type()
)
tx4Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Alarm.setStatus("mandatory")


class _Tx4OnAir_Type(Integer32):
    """Custom type tx4OnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overLoad", 0),
          ("onAir", 1))
    )


_Tx4OnAir_Type.__name__ = "Integer32"
_Tx4OnAir_Object = MibScalar
tx4OnAir = _Tx4OnAir_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 6),
    _Tx4OnAir_Type()
)
tx4OnAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4OnAir.setStatus("mandatory")


class _Tx4Available_Type(Integer32):
    """Custom type tx4Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 0),
          ("available", 1))
    )


_Tx4Available_Type.__name__ = "Integer32"
_Tx4Available_Object = MibScalar
tx4Available = _Tx4Available_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 7),
    _Tx4Available_Type()
)
tx4Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Available.setStatus("mandatory")


class _Tx4Commutation_Type(Integer32):
    """Custom type tx4Commutation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commutationFail", 0),
          ("commutationNotFail", 1))
    )


_Tx4Commutation_Type.__name__ = "Integer32"
_Tx4Commutation_Object = MibScalar
tx4Commutation = _Tx4Commutation_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 8),
    _Tx4Commutation_Type()
)
tx4Commutation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Commutation.setStatus("mandatory")


class _Tx4Interlock_Type(Integer32):
    """Custom type tx4Interlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_Tx4Interlock_Type.__name__ = "Integer32"
_Tx4Interlock_Object = MibScalar
tx4Interlock = _Tx4Interlock_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 9),
    _Tx4Interlock_Type()
)
tx4Interlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Interlock.setStatus("mandatory")


class _Tx4Clamp_Type(Integer32):
    """Custom type tx4Clamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_Tx4Clamp_Type.__name__ = "Integer32"
_Tx4Clamp_Object = MibScalar
tx4Clamp = _Tx4Clamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 4, 10),
    _Tx4Clamp_Type()
)
tx4Clamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx4Clamp.setStatus("mandatory")
_Tx5Status_ObjectIdentity = ObjectIdentity
tx5Status = _Tx5Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5)
)


class _Tx5Start_Type(Integer32):
    """Custom type tx5Start based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_Tx5Start_Type.__name__ = "Integer32"
_Tx5Start_Object = MibScalar
tx5Start = _Tx5Start_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 1),
    _Tx5Start_Type()
)
tx5Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Start.setStatus("mandatory")


class _Tx5Remote_Type(Integer32):
    """Custom type tx5Remote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_Tx5Remote_Type.__name__ = "Integer32"
_Tx5Remote_Object = MibScalar
tx5Remote = _Tx5Remote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 2),
    _Tx5Remote_Type()
)
tx5Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Remote.setStatus("mandatory")


class _Tx5Warning_Type(Integer32):
    """Custom type tx5Warning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_Tx5Warning_Type.__name__ = "Integer32"
_Tx5Warning_Object = MibScalar
tx5Warning = _Tx5Warning_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 3),
    _Tx5Warning_Type()
)
tx5Warning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Warning.setStatus("mandatory")


class _Tx5PowerSupply_Type(Integer32):
    """Custom type tx5PowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_Tx5PowerSupply_Type.__name__ = "Integer32"
_Tx5PowerSupply_Object = MibScalar
tx5PowerSupply = _Tx5PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 4),
    _Tx5PowerSupply_Type()
)
tx5PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5PowerSupply.setStatus("mandatory")


class _Tx5Alarm_Type(Integer32):
    """Custom type tx5Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_Tx5Alarm_Type.__name__ = "Integer32"
_Tx5Alarm_Object = MibScalar
tx5Alarm = _Tx5Alarm_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 5),
    _Tx5Alarm_Type()
)
tx5Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Alarm.setStatus("mandatory")


class _Tx5OnAir_Type(Integer32):
    """Custom type tx5OnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overLoad", 0),
          ("onAir", 1))
    )


_Tx5OnAir_Type.__name__ = "Integer32"
_Tx5OnAir_Object = MibScalar
tx5OnAir = _Tx5OnAir_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 6),
    _Tx5OnAir_Type()
)
tx5OnAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5OnAir.setStatus("mandatory")


class _Tx5Available_Type(Integer32):
    """Custom type tx5Available based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 0),
          ("available", 1))
    )


_Tx5Available_Type.__name__ = "Integer32"
_Tx5Available_Object = MibScalar
tx5Available = _Tx5Available_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 7),
    _Tx5Available_Type()
)
tx5Available.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Available.setStatus("mandatory")


class _Tx5Commutation_Type(Integer32):
    """Custom type tx5Commutation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commutationFail", 0),
          ("commutationNotFail", 1))
    )


_Tx5Commutation_Type.__name__ = "Integer32"
_Tx5Commutation_Object = MibScalar
tx5Commutation = _Tx5Commutation_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 8),
    _Tx5Commutation_Type()
)
tx5Commutation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Commutation.setStatus("mandatory")


class _Tx5Interlock_Type(Integer32):
    """Custom type tx5Interlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_Tx5Interlock_Type.__name__ = "Integer32"
_Tx5Interlock_Object = MibScalar
tx5Interlock = _Tx5Interlock_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 9),
    _Tx5Interlock_Type()
)
tx5Interlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Interlock.setStatus("mandatory")


class _Tx5Clamp_Type(Integer32):
    """Custom type tx5Clamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_Tx5Clamp_Type.__name__ = "Integer32"
_Tx5Clamp_Object = MibScalar
tx5Clamp = _Tx5Clamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 5, 10),
    _Tx5Clamp_Type()
)
tx5Clamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tx5Clamp.setStatus("mandatory")
_TxRvaStatus_ObjectIdentity = ObjectIdentity
txRvaStatus = _TxRvaStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6)
)


class _TxRvaStart_Type(Integer32):
    """Custom type txRvaStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_TxRvaStart_Type.__name__ = "Integer32"
_TxRvaStart_Object = MibScalar
txRvaStart = _TxRvaStart_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 1),
    _TxRvaStart_Type()
)
txRvaStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaStart.setStatus("mandatory")


class _TxRvaRemote_Type(Integer32):
    """Custom type txRvaRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_TxRvaRemote_Type.__name__ = "Integer32"
_TxRvaRemote_Object = MibScalar
txRvaRemote = _TxRvaRemote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 2),
    _TxRvaRemote_Type()
)
txRvaRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaRemote.setStatus("mandatory")


class _TxRvaWarning_Type(Integer32):
    """Custom type txRvaWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_TxRvaWarning_Type.__name__ = "Integer32"
_TxRvaWarning_Object = MibScalar
txRvaWarning = _TxRvaWarning_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 3),
    _TxRvaWarning_Type()
)
txRvaWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaWarning.setStatus("mandatory")


class _TxRvaPowerSupply_Type(Integer32):
    """Custom type txRvaPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_TxRvaPowerSupply_Type.__name__ = "Integer32"
_TxRvaPowerSupply_Object = MibScalar
txRvaPowerSupply = _TxRvaPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 4),
    _TxRvaPowerSupply_Type()
)
txRvaPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaPowerSupply.setStatus("mandatory")


class _TxRvaAlarm_Type(Integer32):
    """Custom type txRvaAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_TxRvaAlarm_Type.__name__ = "Integer32"
_TxRvaAlarm_Object = MibScalar
txRvaAlarm = _TxRvaAlarm_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 5),
    _TxRvaAlarm_Type()
)
txRvaAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaAlarm.setStatus("mandatory")


class _TxRvaOnAir_Type(Integer32):
    """Custom type txRvaOnAir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("overLoad", 0),
          ("onAir", 1))
    )


_TxRvaOnAir_Type.__name__ = "Integer32"
_TxRvaOnAir_Object = MibScalar
txRvaOnAir = _TxRvaOnAir_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 6),
    _TxRvaOnAir_Type()
)
txRvaOnAir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaOnAir.setStatus("mandatory")


class _TxRvaInterlock_Type(Integer32):
    """Custom type txRvaInterlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_TxRvaInterlock_Type.__name__ = "Integer32"
_TxRvaInterlock_Object = MibScalar
txRvaInterlock = _TxRvaInterlock_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 9),
    _TxRvaInterlock_Type()
)
txRvaInterlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaInterlock.setStatus("mandatory")


class _TxRvaClamp_Type(Integer32):
    """Custom type txRvaClamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_TxRvaClamp_Type.__name__ = "Integer32"
_TxRvaClamp_Object = MibScalar
txRvaClamp = _TxRvaClamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 6, 10),
    _TxRvaClamp_Type()
)
txRvaClamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRvaClamp.setStatus("mandatory")
_TxStatusTable_Object = MibTable
txStatusTable = _TxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    txStatusTable.setStatus("mandatory")
_TxStatusEntry_Object = MibTableRow
txStatusEntry = _TxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1)
)
txStatusEntry.setIndexNames(
    (0, "ASINTEL-UCA-SERATEL-MIB", "txStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    txStatusEntry.setStatus("mandatory")


class _TxStatusEntryIndex_Type(Integer32):
    """Custom type txStatusEntryIndex based on Integer32"""
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
        *(("tx1", 1),
          ("tx2", 2),
          ("tx3", 3),
          ("tx4", 4),
          ("tx5", 5),
          ("txRVA", 6))
    )


_TxStatusEntryIndex_Type.__name__ = "Integer32"
_TxStatusEntryIndex_Object = MibTableColumn
txStatusEntryIndex = _TxStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 1),
    _TxStatusEntryIndex_Type()
)
txStatusEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txStatusEntryIndex.setStatus("mandatory")


class _TxStartTXEntry_Type(Integer32):
    """Custom type txStartTXEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_TxStartTXEntry_Type.__name__ = "Integer32"
_TxStartTXEntry_Object = MibTableColumn
txStartTXEntry = _TxStartTXEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 2),
    _TxStartTXEntry_Type()
)
txStartTXEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txStartTXEntry.setStatus("mandatory")


class _TxRemoteEntry_Type(Integer32):
    """Custom type txRemoteEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_TxRemoteEntry_Type.__name__ = "Integer32"
_TxRemoteEntry_Object = MibTableColumn
txRemoteEntry = _TxRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 3),
    _TxRemoteEntry_Type()
)
txRemoteEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRemoteEntry.setStatus("mandatory")


class _TxWarningEntry_Type(Integer32):
    """Custom type txWarningEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("warning", 0),
          ("noWarning", 1))
    )


_TxWarningEntry_Type.__name__ = "Integer32"
_TxWarningEntry_Object = MibTableColumn
txWarningEntry = _TxWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 4),
    _TxWarningEntry_Type()
)
txWarningEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txWarningEntry.setStatus("mandatory")


class _TxPowerEntry_Type(Integer32):
    """Custom type txPowerEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noPowerSupply", 0),
          ("powerSupplyOK", 1))
    )


_TxPowerEntry_Type.__name__ = "Integer32"
_TxPowerEntry_Object = MibTableColumn
txPowerEntry = _TxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 5),
    _TxPowerEntry_Type()
)
txPowerEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPowerEntry.setStatus("mandatory")


class _TxAlarmEntry_Type(Integer32):
    """Custom type txAlarmEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("noAlarm", 1))
    )


_TxAlarmEntry_Type.__name__ = "Integer32"
_TxAlarmEntry_Object = MibTableColumn
txAlarmEntry = _TxAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 6),
    _TxAlarmEntry_Type()
)
txAlarmEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAlarmEntry.setStatus("mandatory")


class _TxOnAirEntry_Type(Integer32):
    """Custom type txOnAirEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onLoad", 0),
          ("onAir", 1))
    )


_TxOnAirEntry_Type.__name__ = "Integer32"
_TxOnAirEntry_Object = MibTableColumn
txOnAirEntry = _TxOnAirEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 7),
    _TxOnAirEntry_Type()
)
txOnAirEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOnAirEntry.setStatus("mandatory")


class _TxAvailableEntry_Type(Integer32):
    """Custom type txAvailableEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAvailable", 0),
          ("available", 1))
    )


_TxAvailableEntry_Type.__name__ = "Integer32"
_TxAvailableEntry_Object = MibTableColumn
txAvailableEntry = _TxAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 8),
    _TxAvailableEntry_Type()
)
txAvailableEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txAvailableEntry.setStatus("mandatory")


class _TxCommutationEntry_Type(Integer32):
    """Custom type txCommutationEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("commutationFail", 0),
          ("commutationNotFail", 1))
    )


_TxCommutationEntry_Type.__name__ = "Integer32"
_TxCommutationEntry_Object = MibTableColumn
txCommutationEntry = _TxCommutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 9),
    _TxCommutationEntry_Type()
)
txCommutationEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCommutationEntry.setStatus("mandatory")


class _TxInterlockEntry_Type(Integer32):
    """Custom type txInterlockEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlockFail", 0),
          ("interlockOK", 1))
    )


_TxInterlockEntry_Type.__name__ = "Integer32"
_TxInterlockEntry_Object = MibTableColumn
txInterlockEntry = _TxInterlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 10),
    _TxInterlockEntry_Type()
)
txInterlockEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txInterlockEntry.setStatus("mandatory")


class _TxClampEntry_Type(Integer32):
    """Custom type txClampEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clampFail", 0),
          ("clampOK", 1))
    )


_TxClampEntry_Type.__name__ = "Integer32"
_TxClampEntry_Object = MibTableColumn
txClampEntry = _TxClampEntry_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 1, 7, 1, 11),
    _TxClampEntry_Type()
)
txClampEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txClampEntry.setStatus("mandatory")


class _UcaManual_Type(Integer32):
    """Custom type ucaManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("manual", 1))
    )


_UcaManual_Type.__name__ = "Integer32"
_UcaManual_Object = MibScalar
ucaManual = _UcaManual_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 2),
    _UcaManual_Type()
)
ucaManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucaManual.setStatus("mandatory")


class _UcaRemote_Type(Integer32):
    """Custom type ucaRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("local", 1))
    )


_UcaRemote_Type.__name__ = "Integer32"
_UcaRemote_Object = MibScalar
ucaRemote = _UcaRemote_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 3),
    _UcaRemote_Type()
)
ucaRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucaRemote.setStatus("mandatory")


class _UcaPowerSupply_Type(Integer32):
    """Custom type ucaPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("noError", 1))
    )


_UcaPowerSupply_Type.__name__ = "Integer32"
_UcaPowerSupply_Object = MibScalar
ucaPowerSupply = _UcaPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 3, 4),
    _UcaPowerSupply_Type()
)
ucaPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucaPowerSupply.setStatus("mandatory")
_StatusSnmpInterface_ObjectIdentity = ObjectIdentity
statusSnmpInterface = _StatusSnmpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 5)
)


class _SpiStatus_Type(Integer32):
    """Custom type spiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 0),
          ("good", 1))
    )


_SpiStatus_Type.__name__ = "Integer32"
_SpiStatus_Object = MibScalar
spiStatus = _SpiStatus_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 5, 1),
    _SpiStatus_Type()
)
spiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiStatus.setStatus("mandatory")


class _ResetSw_Type(Integer32):
    """Custom type resetSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ResetSw_Type.__name__ = "Integer32"
_ResetSw_Object = MibScalar
resetSw = _ResetSw_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 5, 2),
    _ResetSw_Type()
)
resetSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetSw.setStatus("mandatory")
_GeneralInformation_ObjectIdentity = ObjectIdentity
generalInformation = _GeneralInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 6)
)
_FabricadoPor_Type = DisplayString
_FabricadoPor_Object = MibScalar
fabricadoPor = _FabricadoPor_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 6, 1),
    _FabricadoPor_Type()
)
fabricadoPor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fabricadoPor.setStatus("mandatory")
_NombreDisp_Type = DisplayString
_NombreDisp_Object = MibScalar
nombreDisp = _NombreDisp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 6, 2),
    _NombreDisp_Type()
)
nombreDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nombreDisp.setStatus("mandatory")
_NumeroModelo_Type = DisplayString
_NumeroModelo_Object = MibScalar
numeroModelo = _NumeroModelo_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 6, 3),
    _NumeroModelo_Type()
)
numeroModelo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numeroModelo.setStatus("mandatory")
_VersionFirmware_Type = DisplayString
_VersionFirmware_Object = MibScalar
versionFirmware = _VersionFirmware_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 6, 4),
    _VersionFirmware_Type()
)
versionFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionFirmware.setStatus("mandatory")
_TrapsVariables_ObjectIdentity = ObjectIdentity
trapsVariables = _TrapsVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47333, 1, 7)
)
_TrapSequence_Type = Integer32
_TrapSequence_Object = MibScalar
trapSequence = _TrapSequence_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 7, 1),
    _TrapSequence_Type()
)
trapSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequence.setStatus("mandatory")
_TrapTimeStamp_Type = DisplayString
_TrapTimeStamp_Object = MibScalar
trapTimeStamp = _TrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 47333, 1, 7, 2),
    _TrapTimeStamp_Type()
)
trapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapUcaSeratel = NotificationType(
    (1, 3, 6, 1, 4, 1, 47333, 1, 0, 1)
)
if mibBuilder.loadTexts:
    trapUcaSeratel.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASINTEL-UCA-SERATEL-MIB",
    **{"asintel": asintel,
       "ucaSeratel": ucaSeratel,
       "networkConfiguration": networkConfiguration,
       "ipConfig": ipConfig,
       "trapUcaSeratel": trapUcaSeratel,
       "ipConfiguration": ipConfiguration,
       "maskConfiguration": maskConfiguration,
       "gatewayConfiguration": gatewayConfiguration,
       "dnsAddressConfiguration": dnsAddressConfiguration,
       "snmpConfig": snmpConfig,
       "trapRemoteHostIP1": trapRemoteHostIP1,
       "trapRemoteHostIP2": trapRemoteHostIP2,
       "trapRemoteHostIP3": trapRemoteHostIP3,
       "trapRemoteHostIP4": trapRemoteHostIP4,
       "aliveInterval": aliveInterval,
       "aliveEnable": aliveEnable,
       "trapsEnable": trapsEnable,
       "passwordRead": passwordRead,
       "passwordWrite": passwordWrite,
       "sntpConfig": sntpConfig,
       "sntpServer1IP": sntpServer1IP,
       "sntpServer2IP": sntpServer2IP,
       "sntpServer3IP": sntpServer3IP,
       "sntpSyncInterval": sntpSyncInterval,
       "sntpSyncEnable": sntpSyncEnable,
       "unitConfiguration": unitConfiguration,
       "txConfig": txConfig,
       "tx1Config": tx1Config,
       "tx1Enable": tx1Enable,
       "tx1Priority": tx1Priority,
       "tx1TimePrev": tx1TimePrev,
       "tx1TimePost": tx1TimePost,
       "tx2Config": tx2Config,
       "tx2Enable": tx2Enable,
       "tx2Priority": tx2Priority,
       "tx2TimePrev": tx2TimePrev,
       "tx2TimePost": tx2TimePost,
       "tx3Config": tx3Config,
       "tx3Enable": tx3Enable,
       "tx3Priority": tx3Priority,
       "tx3TimePrev": tx3TimePrev,
       "tx3TimePost": tx3TimePost,
       "tx4Config": tx4Config,
       "tx4Enable": tx4Enable,
       "tx4Priority": tx4Priority,
       "tx4TimePrev": tx4TimePrev,
       "tx4TimePost": tx4TimePost,
       "tx5Config": tx5Config,
       "tx5Enable": tx5Enable,
       "tx5Priority": tx5Priority,
       "tx5TimePrev": tx5TimePrev,
       "tx5TimePost": tx5TimePost,
       "txRvaConfig": txRvaConfig,
       "txRvaProg": txRvaProg,
       "ucaName": ucaName,
       "ucaSerialNumber": ucaSerialNumber,
       "ucaPassword": ucaPassword,
       "txInstalledNumber": txInstalledNumber,
       "ucaPriorityEnable": ucaPriorityEnable,
       "maxRetries": maxRetries,
       "timeBetweenRetries": timeBetweenRetries,
       "ucaAutoProgram": ucaAutoProgram,
       "unitControl": unitControl,
       "txControl": txControl,
       "tx1Control": tx1Control,
       "tx1ResetTX": tx1ResetTX,
       "tx1StartStopTX": tx1StartStopTX,
       "tx1LoadTX": tx1LoadTX,
       "tx2Control": tx2Control,
       "tx2ResetTX": tx2ResetTX,
       "tx2StartStopTX": tx2StartStopTX,
       "tx2LoadTX": tx2LoadTX,
       "tx3Control": tx3Control,
       "tx3ResetTX": tx3ResetTX,
       "tx3StartStopTX": tx3StartStopTX,
       "tx3LoadTX": tx3LoadTX,
       "tx4Control": tx4Control,
       "tx4ResetTX": tx4ResetTX,
       "tx4StartStopTX": tx4StartStopTX,
       "tx4LoadTX": tx4LoadTX,
       "tx5Control": tx5Control,
       "tx5ResetTX": tx5ResetTX,
       "tx5StartStopTX": tx5StartStopTX,
       "tx5LoadTX": tx5LoadTX,
       "txRvaControl": txRvaControl,
       "txRvaResetTX": txRvaResetTX,
       "txRvaStartStopTX": txRvaStartStopTX,
       "txRvaLoadTX": txRvaLoadTX,
       "ucaReset": ucaReset,
       "ucaAutoManual": ucaAutoManual,
       "ucaInitialize": ucaInitialize,
       "ucaForceRemote": ucaForceRemote,
       "unitStatus": unitStatus,
       "txStatus": txStatus,
       "tx1Status": tx1Status,
       "tx1Start": tx1Start,
       "tx1Remote": tx1Remote,
       "tx1Warning": tx1Warning,
       "tx1PowerSupply": tx1PowerSupply,
       "tx1Alarm": tx1Alarm,
       "tx1OnAir": tx1OnAir,
       "tx1Available": tx1Available,
       "tx1Commutation": tx1Commutation,
       "tx1Interlock": tx1Interlock,
       "tx1Clamp": tx1Clamp,
       "tx2Status": tx2Status,
       "tx2Start": tx2Start,
       "tx2Remote": tx2Remote,
       "tx2Warning": tx2Warning,
       "tx2PowerSupply": tx2PowerSupply,
       "tx2Alarm": tx2Alarm,
       "tx2OnAir": tx2OnAir,
       "tx2Available": tx2Available,
       "tx2Commutation": tx2Commutation,
       "tx2Interlock": tx2Interlock,
       "tx2Clamp": tx2Clamp,
       "tx3Status": tx3Status,
       "tx3Start": tx3Start,
       "tx3Remote": tx3Remote,
       "tx3Warning": tx3Warning,
       "tx3PowerSupply": tx3PowerSupply,
       "tx3Alarm": tx3Alarm,
       "tx3OnAir": tx3OnAir,
       "tx3Available": tx3Available,
       "tx3Commutation": tx3Commutation,
       "tx3Interlock": tx3Interlock,
       "tx3Clamp": tx3Clamp,
       "tx4Status": tx4Status,
       "tx4Start": tx4Start,
       "tx4Remote": tx4Remote,
       "tx4Warning": tx4Warning,
       "tx4PowerSupply": tx4PowerSupply,
       "tx4Alarm": tx4Alarm,
       "tx4OnAir": tx4OnAir,
       "tx4Available": tx4Available,
       "tx4Commutation": tx4Commutation,
       "tx4Interlock": tx4Interlock,
       "tx4Clamp": tx4Clamp,
       "tx5Status": tx5Status,
       "tx5Start": tx5Start,
       "tx5Remote": tx5Remote,
       "tx5Warning": tx5Warning,
       "tx5PowerSupply": tx5PowerSupply,
       "tx5Alarm": tx5Alarm,
       "tx5OnAir": tx5OnAir,
       "tx5Available": tx5Available,
       "tx5Commutation": tx5Commutation,
       "tx5Interlock": tx5Interlock,
       "tx5Clamp": tx5Clamp,
       "txRvaStatus": txRvaStatus,
       "txRvaStart": txRvaStart,
       "txRvaRemote": txRvaRemote,
       "txRvaWarning": txRvaWarning,
       "txRvaPowerSupply": txRvaPowerSupply,
       "txRvaAlarm": txRvaAlarm,
       "txRvaOnAir": txRvaOnAir,
       "txRvaInterlock": txRvaInterlock,
       "txRvaClamp": txRvaClamp,
       "txStatusTable": txStatusTable,
       "txStatusEntry": txStatusEntry,
       "txStatusEntryIndex": txStatusEntryIndex,
       "txStartTXEntry": txStartTXEntry,
       "txRemoteEntry": txRemoteEntry,
       "txWarningEntry": txWarningEntry,
       "txPowerEntry": txPowerEntry,
       "txAlarmEntry": txAlarmEntry,
       "txOnAirEntry": txOnAirEntry,
       "txAvailableEntry": txAvailableEntry,
       "txCommutationEntry": txCommutationEntry,
       "txInterlockEntry": txInterlockEntry,
       "txClampEntry": txClampEntry,
       "ucaManual": ucaManual,
       "ucaRemote": ucaRemote,
       "ucaPowerSupply": ucaPowerSupply,
       "statusSnmpInterface": statusSnmpInterface,
       "spiStatus": spiStatus,
       "resetSw": resetSw,
       "generalInformation": generalInformation,
       "fabricadoPor": fabricadoPor,
       "nombreDisp": nombreDisp,
       "numeroModelo": numeroModelo,
       "versionFirmware": versionFirmware,
       "trapsVariables": trapsVariables,
       "trapSequence": trapSequence,
       "trapTimeStamp": trapTimeStamp}
)
