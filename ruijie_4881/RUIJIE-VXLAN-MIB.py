# SNMP MIB module (RUIJIE-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-VXLAN-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieVxlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161)
)
if mibBuilder.loadTexts:
    ruijieVxlanMIB.setRevisions(
        ("2019-04-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieVxlanMIBObjects_ObjectIdentity = ObjectIdentity
ruijieVxlanMIBObjects = _RuijieVxlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1)
)
_RuijieVxlanVniStatisticTable_Object = MibTable
ruijieVxlanVniStatisticTable = _RuijieVxlanVniStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticTable.setStatus("current")
_RuijieVxlanVniStatisticEntry_Object = MibTableRow
ruijieVxlanVniStatisticEntry = _RuijieVxlanVniStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1)
)
ruijieVxlanVniStatisticEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticVni"),
)
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticEntry.setStatus("current")


class _RuijieVxlanVniStatisticVni_Type(Unsigned32):
    """Custom type ruijieVxlanVniStatisticVni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RuijieVxlanVniStatisticVni_Type.__name__ = "Unsigned32"
_RuijieVxlanVniStatisticVni_Object = MibTableColumn
ruijieVxlanVniStatisticVni = _RuijieVxlanVniStatisticVni_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 1),
    _RuijieVxlanVniStatisticVni_Type()
)
ruijieVxlanVniStatisticVni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticVni.setStatus("current")
_RuijieVxlanVniStatisticInPackets_Type = Counter64
_RuijieVxlanVniStatisticInPackets_Object = MibTableColumn
ruijieVxlanVniStatisticInPackets = _RuijieVxlanVniStatisticInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 2),
    _RuijieVxlanVniStatisticInPackets_Type()
)
ruijieVxlanVniStatisticInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticInPackets.setStatus("current")
_RuijieVxlanVniStatisticOutPackets_Type = Counter64
_RuijieVxlanVniStatisticOutPackets_Object = MibTableColumn
ruijieVxlanVniStatisticOutPackets = _RuijieVxlanVniStatisticOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 3),
    _RuijieVxlanVniStatisticOutPackets_Type()
)
ruijieVxlanVniStatisticOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticOutPackets.setStatus("current")
_RuijieVxlanVniStatisticInBytes_Type = Counter64
_RuijieVxlanVniStatisticInBytes_Object = MibTableColumn
ruijieVxlanVniStatisticInBytes = _RuijieVxlanVniStatisticInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 4),
    _RuijieVxlanVniStatisticInBytes_Type()
)
ruijieVxlanVniStatisticInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticInBytes.setStatus("current")
_RuijieVxlanVniStatisticOutBytes_Type = Counter64
_RuijieVxlanVniStatisticOutBytes_Object = MibTableColumn
ruijieVxlanVniStatisticOutBytes = _RuijieVxlanVniStatisticOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 5),
    _RuijieVxlanVniStatisticOutBytes_Type()
)
ruijieVxlanVniStatisticOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticOutBytes.setStatus("current")
_RuijieVxlanVniStatisticInPps_Type = Counter64
_RuijieVxlanVniStatisticInPps_Object = MibTableColumn
ruijieVxlanVniStatisticInPps = _RuijieVxlanVniStatisticInPps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 6),
    _RuijieVxlanVniStatisticInPps_Type()
)
ruijieVxlanVniStatisticInPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticInPps.setStatus("current")
_RuijieVxlanVniStatisticOutPps_Type = Counter64
_RuijieVxlanVniStatisticOutPps_Object = MibTableColumn
ruijieVxlanVniStatisticOutPps = _RuijieVxlanVniStatisticOutPps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 7),
    _RuijieVxlanVniStatisticOutPps_Type()
)
ruijieVxlanVniStatisticOutPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticOutPps.setStatus("current")
_RuijieVxlanVniStatisticInBps_Type = Counter64
_RuijieVxlanVniStatisticInBps_Object = MibTableColumn
ruijieVxlanVniStatisticInBps = _RuijieVxlanVniStatisticInBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 8),
    _RuijieVxlanVniStatisticInBps_Type()
)
ruijieVxlanVniStatisticInBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticInBps.setStatus("current")
_RuijieVxlanVniStatisticOutBps_Type = Counter64
_RuijieVxlanVniStatisticOutBps_Object = MibTableColumn
ruijieVxlanVniStatisticOutBps = _RuijieVxlanVniStatisticOutBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 1, 1, 9),
    _RuijieVxlanVniStatisticOutBps_Type()
)
ruijieVxlanVniStatisticOutBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticOutBps.setStatus("current")
_RuijieVxlanStaticTnlTable_Object = MibTable
ruijieVxlanStaticTnlTable = _RuijieVxlanStaticTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlTable.setStatus("current")
_RuijieVxlanStaticTnlEntry_Object = MibTableRow
ruijieVxlanStaticTnlEntry = _RuijieVxlanStaticTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 2, 1)
)
ruijieVxlanStaticTnlEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlSourceIp"),
)
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlEntry.setStatus("current")
_RuijieVxlanStaticTnlDestIp_Type = IpAddress
_RuijieVxlanStaticTnlDestIp_Object = MibTableColumn
ruijieVxlanStaticTnlDestIp = _RuijieVxlanStaticTnlDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 2, 1, 1),
    _RuijieVxlanStaticTnlDestIp_Type()
)
ruijieVxlanStaticTnlDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlDestIp.setStatus("current")
_RuijieVxlanStaticTnlSourceIp_Type = IpAddress
_RuijieVxlanStaticTnlSourceIp_Object = MibTableColumn
ruijieVxlanStaticTnlSourceIp = _RuijieVxlanStaticTnlSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 2, 1, 2),
    _RuijieVxlanStaticTnlSourceIp_Type()
)
ruijieVxlanStaticTnlSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlSourceIp.setStatus("current")


class _RuijieVxlanStaticTnlRowStatus_Type(RowStatus):
    """Custom type ruijieVxlanStaticTnlRowStatus based on RowStatus"""
    defaultValue = 1


_RuijieVxlanStaticTnlRowStatus_Type.__name__ = "RowStatus"
_RuijieVxlanStaticTnlRowStatus_Object = MibTableColumn
ruijieVxlanStaticTnlRowStatus = _RuijieVxlanStaticTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 2, 1, 3),
    _RuijieVxlanStaticTnlRowStatus_Type()
)
ruijieVxlanStaticTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlRowStatus.setStatus("current")
_RuijieVxlanVniTnlTable_Object = MibTable
ruijieVxlanVniTnlTable = _RuijieVxlanVniTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlTable.setStatus("current")
_RuijieVxlanVniTnlEntry_Object = MibTableRow
ruijieVxlanVniTnlEntry = _RuijieVxlanVniTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 3, 1)
)
ruijieVxlanVniTnlEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlVni"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlSourceIp"),
)
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlEntry.setStatus("current")


class _RuijieVxlanVniTnlVni_Type(Unsigned32):
    """Custom type ruijieVxlanVniTnlVni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RuijieVxlanVniTnlVni_Type.__name__ = "Unsigned32"
_RuijieVxlanVniTnlVni_Object = MibTableColumn
ruijieVxlanVniTnlVni = _RuijieVxlanVniTnlVni_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 3, 1, 1),
    _RuijieVxlanVniTnlVni_Type()
)
ruijieVxlanVniTnlVni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlVni.setStatus("current")
_RuijieVxlanVniTnlDestIp_Type = IpAddress
_RuijieVxlanVniTnlDestIp_Object = MibTableColumn
ruijieVxlanVniTnlDestIp = _RuijieVxlanVniTnlDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 3, 1, 2),
    _RuijieVxlanVniTnlDestIp_Type()
)
ruijieVxlanVniTnlDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlDestIp.setStatus("current")
_RuijieVxlanVniTnlSourceIp_Type = IpAddress
_RuijieVxlanVniTnlSourceIp_Object = MibTableColumn
ruijieVxlanVniTnlSourceIp = _RuijieVxlanVniTnlSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 3, 1, 3),
    _RuijieVxlanVniTnlSourceIp_Type()
)
ruijieVxlanVniTnlSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlSourceIp.setStatus("current")
_RuijieVxlanVniTnlRowStatus_Type = RowStatus
_RuijieVxlanVniTnlRowStatus_Object = MibTableColumn
ruijieVxlanVniTnlRowStatus = _RuijieVxlanVniTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 3, 1, 4),
    _RuijieVxlanVniTnlRowStatus_Type()
)
ruijieVxlanVniTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlRowStatus.setStatus("current")
_RuijieVxlanTnlTable_Object = MibTable
ruijieVxlanTnlTable = _RuijieVxlanTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlTable.setStatus("current")
_RuijieVxlanTnlEntry_Object = MibTableRow
ruijieVxlanTnlEntry = _RuijieVxlanTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 4, 1)
)
ruijieVxlanTnlEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlSourceIp"),
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlEntry.setStatus("current")
_RuijieVxlanTnlDestIp_Type = IpAddress
_RuijieVxlanTnlDestIp_Object = MibTableColumn
ruijieVxlanTnlDestIp = _RuijieVxlanTnlDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 4, 1, 1),
    _RuijieVxlanTnlDestIp_Type()
)
ruijieVxlanTnlDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlDestIp.setStatus("current")
_RuijieVxlanTnlSourceIp_Type = IpAddress
_RuijieVxlanTnlSourceIp_Object = MibTableColumn
ruijieVxlanTnlSourceIp = _RuijieVxlanTnlSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 4, 1, 2),
    _RuijieVxlanTnlSourceIp_Type()
)
ruijieVxlanTnlSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlSourceIp.setStatus("current")
_RuijieVxlanTnlPortNum_Type = Unsigned32
_RuijieVxlanTnlPortNum_Object = MibTableColumn
ruijieVxlanTnlPortNum = _RuijieVxlanTnlPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 4, 1, 3),
    _RuijieVxlanTnlPortNum_Type()
)
ruijieVxlanTnlPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlPortNum.setStatus("current")


class _RuijieVxlanTnlStatus_Type(Integer32):
    """Custom type ruijieVxlanTnlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RuijieVxlanTnlStatus_Type.__name__ = "Integer32"
_RuijieVxlanTnlStatus_Object = MibTableColumn
ruijieVxlanTnlStatus = _RuijieVxlanTnlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 4, 1, 4),
    _RuijieVxlanTnlStatus_Type()
)
ruijieVxlanTnlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlStatus.setStatus("current")
_RuijieVxlanTnlVniStatisticTable_Object = MibTable
ruijieVxlanTnlVniStatisticTable = _RuijieVxlanTnlVniStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticTable.setStatus("current")
_RuijieVxlanTnlVniStatisticEntry_Object = MibTableRow
ruijieVxlanTnlVniStatisticEntry = _RuijieVxlanTnlVniStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1)
)
ruijieVxlanTnlVniStatisticEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticSourceIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticVni"),
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticEntry.setStatus("current")
_RuijieVxlanTnlVniStatisticDestIp_Type = IpAddress
_RuijieVxlanTnlVniStatisticDestIp_Object = MibTableColumn
ruijieVxlanTnlVniStatisticDestIp = _RuijieVxlanTnlVniStatisticDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 1),
    _RuijieVxlanTnlVniStatisticDestIp_Type()
)
ruijieVxlanTnlVniStatisticDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticDestIp.setStatus("current")
_RuijieVxlanTnlVniStatisticSourceIp_Type = IpAddress
_RuijieVxlanTnlVniStatisticSourceIp_Object = MibTableColumn
ruijieVxlanTnlVniStatisticSourceIp = _RuijieVxlanTnlVniStatisticSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 2),
    _RuijieVxlanTnlVniStatisticSourceIp_Type()
)
ruijieVxlanTnlVniStatisticSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticSourceIp.setStatus("current")


class _RuijieVxlanTnlVniStatisticVni_Type(Unsigned32):
    """Custom type ruijieVxlanTnlVniStatisticVni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RuijieVxlanTnlVniStatisticVni_Type.__name__ = "Unsigned32"
_RuijieVxlanTnlVniStatisticVni_Object = MibTableColumn
ruijieVxlanTnlVniStatisticVni = _RuijieVxlanTnlVniStatisticVni_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 3),
    _RuijieVxlanTnlVniStatisticVni_Type()
)
ruijieVxlanTnlVniStatisticVni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticVni.setStatus("current")
_RuijieVxlanTnlVniStatisticInPackets_Type = Counter64
_RuijieVxlanTnlVniStatisticInPackets_Object = MibTableColumn
ruijieVxlanTnlVniStatisticInPackets = _RuijieVxlanTnlVniStatisticInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 4),
    _RuijieVxlanTnlVniStatisticInPackets_Type()
)
ruijieVxlanTnlVniStatisticInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticInPackets.setStatus("current")
_RuijieVxlanTnlVniStatisticOutPackets_Type = Counter64
_RuijieVxlanTnlVniStatisticOutPackets_Object = MibTableColumn
ruijieVxlanTnlVniStatisticOutPackets = _RuijieVxlanTnlVniStatisticOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 5),
    _RuijieVxlanTnlVniStatisticOutPackets_Type()
)
ruijieVxlanTnlVniStatisticOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticOutPackets.setStatus("current")
_RuijieVxlanTnlVniStatisticInBytes_Type = Counter64
_RuijieVxlanTnlVniStatisticInBytes_Object = MibTableColumn
ruijieVxlanTnlVniStatisticInBytes = _RuijieVxlanTnlVniStatisticInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 6),
    _RuijieVxlanTnlVniStatisticInBytes_Type()
)
ruijieVxlanTnlVniStatisticInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticInBytes.setStatus("current")
_RuijieVxlanTnlVniStatisticOutBytes_Type = Counter64
_RuijieVxlanTnlVniStatisticOutBytes_Object = MibTableColumn
ruijieVxlanTnlVniStatisticOutBytes = _RuijieVxlanTnlVniStatisticOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 7),
    _RuijieVxlanTnlVniStatisticOutBytes_Type()
)
ruijieVxlanTnlVniStatisticOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticOutBytes.setStatus("current")
_RuijieVxlanTnlVniStatisticInPps_Type = Counter64
_RuijieVxlanTnlVniStatisticInPps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticInPps = _RuijieVxlanTnlVniStatisticInPps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 8),
    _RuijieVxlanTnlVniStatisticInPps_Type()
)
ruijieVxlanTnlVniStatisticInPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticInPps.setStatus("current")
_RuijieVxlanTnlVniStatisticOutPps_Type = Counter64
_RuijieVxlanTnlVniStatisticOutPps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticOutPps = _RuijieVxlanTnlVniStatisticOutPps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 9),
    _RuijieVxlanTnlVniStatisticOutPps_Type()
)
ruijieVxlanTnlVniStatisticOutPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticOutPps.setStatus("current")
_RuijieVxlanTnlVniStatisticInBps_Type = Counter64
_RuijieVxlanTnlVniStatisticInBps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticInBps = _RuijieVxlanTnlVniStatisticInBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 10),
    _RuijieVxlanTnlVniStatisticInBps_Type()
)
ruijieVxlanTnlVniStatisticInBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticInBps.setStatus("current")
_RuijieVxlanTnlVniStatisticOutBps_Type = Counter64
_RuijieVxlanTnlVniStatisticOutBps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticOutBps = _RuijieVxlanTnlVniStatisticOutBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 5, 1, 11),
    _RuijieVxlanTnlVniStatisticOutBps_Type()
)
ruijieVxlanTnlVniStatisticOutBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticOutBps.setStatus("current")
_RuijieVxlanVtepTable_Object = MibTable
ruijieVxlanVtepTable = _RuijieVxlanVtepTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieVxlanVtepTable.setStatus("current")
_RuijieVxlanVtepEntry_Object = MibTableRow
ruijieVxlanVtepEntry = _RuijieVxlanVtepEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 6, 1)
)
ruijieVxlanVtepEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVtepId"),
)
if mibBuilder.loadTexts:
    ruijieVxlanVtepEntry.setStatus("current")


class _RuijieVxlanVtepId_Type(Unsigned32):
    """Custom type ruijieVxlanVtepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RuijieVxlanVtepId_Type.__name__ = "Unsigned32"
_RuijieVxlanVtepId_Object = MibTableColumn
ruijieVxlanVtepId = _RuijieVxlanVtepId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 6, 1, 1),
    _RuijieVxlanVtepId_Type()
)
ruijieVxlanVtepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVtepId.setStatus("current")


class _RuijieVxlanVtepSourceLoopbackNum_Type(Integer32):
    """Custom type ruijieVxlanVtepSourceLoopbackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RuijieVxlanVtepSourceLoopbackNum_Type.__name__ = "Integer32"
_RuijieVxlanVtepSourceLoopbackNum_Object = MibTableColumn
ruijieVxlanVtepSourceLoopbackNum = _RuijieVxlanVtepSourceLoopbackNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 6, 1, 2),
    _RuijieVxlanVtepSourceLoopbackNum_Type()
)
ruijieVxlanVtepSourceLoopbackNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVxlanVtepSourceLoopbackNum.setStatus("current")
_RuijieVxlanVtepSourceIPv4Addr_Type = IpAddress
_RuijieVxlanVtepSourceIPv4Addr_Object = MibTableColumn
ruijieVxlanVtepSourceIPv4Addr = _RuijieVxlanVtepSourceIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 6, 1, 3),
    _RuijieVxlanVtepSourceIPv4Addr_Type()
)
ruijieVxlanVtepSourceIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVxlanVtepSourceIPv4Addr.setStatus("current")
_RuijieVxlanVtepSourceIPv6Addr_Type = InetAddressIPv6
_RuijieVxlanVtepSourceIPv6Addr_Object = MibTableColumn
ruijieVxlanVtepSourceIPv6Addr = _RuijieVxlanVtepSourceIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 6, 1, 4),
    _RuijieVxlanVtepSourceIPv6Addr_Type()
)
ruijieVxlanVtepSourceIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieVxlanVtepSourceIPv6Addr.setStatus("current")
_RuijieVxlanVlanAssoTable_Object = MibTable
ruijieVxlanVlanAssoTable = _RuijieVxlanVlanAssoTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieVxlanVlanAssoTable.setStatus("current")
_RuijieVxlanVlanAssoEntry_Object = MibTableRow
ruijieVxlanVlanAssoEntry = _RuijieVxlanVlanAssoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 7, 1)
)
ruijieVxlanVlanAssoEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVlanAssoVid"),
)
if mibBuilder.loadTexts:
    ruijieVxlanVlanAssoEntry.setStatus("current")
_RuijieVxlanVlanAssoVid_Type = VlanId
_RuijieVxlanVlanAssoVid_Object = MibTableColumn
ruijieVxlanVlanAssoVid = _RuijieVxlanVlanAssoVid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 7, 1, 1),
    _RuijieVxlanVlanAssoVid_Type()
)
ruijieVxlanVlanAssoVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVlanAssoVid.setStatus("current")


class _RuijieVxlanVlanAssoVni_Type(Unsigned32):
    """Custom type ruijieVxlanVlanAssoVni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RuijieVxlanVlanAssoVni_Type.__name__ = "Unsigned32"
_RuijieVxlanVlanAssoVni_Object = MibTableColumn
ruijieVxlanVlanAssoVni = _RuijieVxlanVlanAssoVni_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 7, 1, 2),
    _RuijieVxlanVlanAssoVni_Type()
)
ruijieVxlanVlanAssoVni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanVlanAssoVni.setStatus("current")
_RuijieVxlanStaticTnlExtTable_Object = MibTable
ruijieVxlanStaticTnlExtTable = _RuijieVxlanStaticTnlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtTable.setStatus("current")
_RuijieVxlanStaticTnlExtEntry_Object = MibTableRow
ruijieVxlanStaticTnlExtEntry = _RuijieVxlanStaticTnlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8, 1)
)
ruijieVxlanStaticTnlExtEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlExtDestIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlExtDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlExtSourceIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlExtSourceIp"),
)
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtEntry.setStatus("current")


class _RuijieVxlanStaticTnlExtDestIpType_Type(InetAddressType):
    """Custom type ruijieVxlanStaticTnlExtDestIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanStaticTnlExtDestIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanStaticTnlExtDestIpType_Object = MibTableColumn
ruijieVxlanStaticTnlExtDestIpType = _RuijieVxlanStaticTnlExtDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8, 1, 1),
    _RuijieVxlanStaticTnlExtDestIpType_Type()
)
ruijieVxlanStaticTnlExtDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtDestIpType.setStatus("current")
_RuijieVxlanStaticTnlExtDestIp_Type = InetAddress
_RuijieVxlanStaticTnlExtDestIp_Object = MibTableColumn
ruijieVxlanStaticTnlExtDestIp = _RuijieVxlanStaticTnlExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8, 1, 2),
    _RuijieVxlanStaticTnlExtDestIp_Type()
)
ruijieVxlanStaticTnlExtDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtDestIp.setStatus("current")


class _RuijieVxlanStaticTnlExtSourceIpType_Type(InetAddressType):
    """Custom type ruijieVxlanStaticTnlExtSourceIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanStaticTnlExtSourceIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanStaticTnlExtSourceIpType_Object = MibTableColumn
ruijieVxlanStaticTnlExtSourceIpType = _RuijieVxlanStaticTnlExtSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8, 1, 3),
    _RuijieVxlanStaticTnlExtSourceIpType_Type()
)
ruijieVxlanStaticTnlExtSourceIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtSourceIpType.setStatus("current")
_RuijieVxlanStaticTnlExtSourceIp_Type = IpAddress
_RuijieVxlanStaticTnlExtSourceIp_Object = MibTableColumn
ruijieVxlanStaticTnlExtSourceIp = _RuijieVxlanStaticTnlExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8, 1, 4),
    _RuijieVxlanStaticTnlExtSourceIp_Type()
)
ruijieVxlanStaticTnlExtSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtSourceIp.setStatus("current")


class _RuijieVxlanStaticTnlExtRowStatus_Type(RowStatus):
    """Custom type ruijieVxlanStaticTnlExtRowStatus based on RowStatus"""
    defaultValue = 1


_RuijieVxlanStaticTnlExtRowStatus_Type.__name__ = "RowStatus"
_RuijieVxlanStaticTnlExtRowStatus_Object = MibTableColumn
ruijieVxlanStaticTnlExtRowStatus = _RuijieVxlanStaticTnlExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 8, 1, 5),
    _RuijieVxlanStaticTnlExtRowStatus_Type()
)
ruijieVxlanStaticTnlExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlExtRowStatus.setStatus("current")
_RuijieVxlanVniTnlExtTable_Object = MibTable
ruijieVxlanVniTnlExtTable = _RuijieVxlanVniTnlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtTable.setStatus("current")
_RuijieVxlanVniTnlExtEntry_Object = MibTableRow
ruijieVxlanVniTnlExtEntry = _RuijieVxlanVniTnlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1)
)
ruijieVxlanVniTnlExtEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlExtVni"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlExtDestIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlExtDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlExtSourceIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlExtSourceIp"),
)
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtEntry.setStatus("current")


class _RuijieVxlanVniTnlExtVni_Type(Unsigned32):
    """Custom type ruijieVxlanVniTnlExtVni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RuijieVxlanVniTnlExtVni_Type.__name__ = "Unsigned32"
_RuijieVxlanVniTnlExtVni_Object = MibTableColumn
ruijieVxlanVniTnlExtVni = _RuijieVxlanVniTnlExtVni_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1, 1),
    _RuijieVxlanVniTnlExtVni_Type()
)
ruijieVxlanVniTnlExtVni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtVni.setStatus("current")


class _RuijieVxlanVniTnlExtDestIpType_Type(InetAddressType):
    """Custom type ruijieVxlanVniTnlExtDestIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanVniTnlExtDestIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanVniTnlExtDestIpType_Object = MibTableColumn
ruijieVxlanVniTnlExtDestIpType = _RuijieVxlanVniTnlExtDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1, 2),
    _RuijieVxlanVniTnlExtDestIpType_Type()
)
ruijieVxlanVniTnlExtDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtDestIpType.setStatus("current")
_RuijieVxlanVniTnlExtDestIp_Type = InetAddress
_RuijieVxlanVniTnlExtDestIp_Object = MibTableColumn
ruijieVxlanVniTnlExtDestIp = _RuijieVxlanVniTnlExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1, 3),
    _RuijieVxlanVniTnlExtDestIp_Type()
)
ruijieVxlanVniTnlExtDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtDestIp.setStatus("current")


class _RuijieVxlanVniTnlExtSourceIpType_Type(InetAddressType):
    """Custom type ruijieVxlanVniTnlExtSourceIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanVniTnlExtSourceIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanVniTnlExtSourceIpType_Object = MibTableColumn
ruijieVxlanVniTnlExtSourceIpType = _RuijieVxlanVniTnlExtSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1, 4),
    _RuijieVxlanVniTnlExtSourceIpType_Type()
)
ruijieVxlanVniTnlExtSourceIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtSourceIpType.setStatus("current")
_RuijieVxlanVniTnlExtSourceIp_Type = InetAddress
_RuijieVxlanVniTnlExtSourceIp_Object = MibTableColumn
ruijieVxlanVniTnlExtSourceIp = _RuijieVxlanVniTnlExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1, 5),
    _RuijieVxlanVniTnlExtSourceIp_Type()
)
ruijieVxlanVniTnlExtSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtSourceIp.setStatus("current")
_RuijieVxlanVniTnlExtRowStatus_Type = RowStatus
_RuijieVxlanVniTnlExtRowStatus_Object = MibTableColumn
ruijieVxlanVniTnlExtRowStatus = _RuijieVxlanVniTnlExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 9, 1, 6),
    _RuijieVxlanVniTnlExtRowStatus_Type()
)
ruijieVxlanVniTnlExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieVxlanVniTnlExtRowStatus.setStatus("current")
_RuijieVxlanTnlExtTable_Object = MibTable
ruijieVxlanTnlExtTable = _RuijieVxlanTnlExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtTable.setStatus("current")
_RuijieVxlanTnlExtEntry_Object = MibTableRow
ruijieVxlanTnlExtEntry = _RuijieVxlanTnlExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1)
)
ruijieVxlanTnlExtEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtDestIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtSourceIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtSourceIp"),
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtEntry.setStatus("current")


class _RuijieVxlanTnlExtDestIpType_Type(InetAddressType):
    """Custom type ruijieVxlanTnlExtDestIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanTnlExtDestIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanTnlExtDestIpType_Object = MibTableColumn
ruijieVxlanTnlExtDestIpType = _RuijieVxlanTnlExtDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1, 1),
    _RuijieVxlanTnlExtDestIpType_Type()
)
ruijieVxlanTnlExtDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtDestIpType.setStatus("current")
_RuijieVxlanTnlExtDestIp_Type = InetAddress
_RuijieVxlanTnlExtDestIp_Object = MibTableColumn
ruijieVxlanTnlExtDestIp = _RuijieVxlanTnlExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1, 2),
    _RuijieVxlanTnlExtDestIp_Type()
)
ruijieVxlanTnlExtDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtDestIp.setStatus("current")


class _RuijieVxlanTnlExtSourceIpType_Type(InetAddressType):
    """Custom type ruijieVxlanTnlExtSourceIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanTnlExtSourceIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanTnlExtSourceIpType_Object = MibTableColumn
ruijieVxlanTnlExtSourceIpType = _RuijieVxlanTnlExtSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1, 3),
    _RuijieVxlanTnlExtSourceIpType_Type()
)
ruijieVxlanTnlExtSourceIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtSourceIpType.setStatus("current")
_RuijieVxlanTnlExtSourceIp_Type = InetAddress
_RuijieVxlanTnlExtSourceIp_Object = MibTableColumn
ruijieVxlanTnlExtSourceIp = _RuijieVxlanTnlExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1, 4),
    _RuijieVxlanTnlExtSourceIp_Type()
)
ruijieVxlanTnlExtSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtSourceIp.setStatus("current")
_RuijieVxlanTnlExtPortNum_Type = Unsigned32
_RuijieVxlanTnlExtPortNum_Object = MibTableColumn
ruijieVxlanTnlExtPortNum = _RuijieVxlanTnlExtPortNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1, 5),
    _RuijieVxlanTnlExtPortNum_Type()
)
ruijieVxlanTnlExtPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtPortNum.setStatus("current")


class _RuijieVxlanTnlExtStatus_Type(Integer32):
    """Custom type ruijieVxlanTnlExtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RuijieVxlanTnlExtStatus_Type.__name__ = "Integer32"
_RuijieVxlanTnlExtStatus_Object = MibTableColumn
ruijieVxlanTnlExtStatus = _RuijieVxlanTnlExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 10, 1, 6),
    _RuijieVxlanTnlExtStatus_Type()
)
ruijieVxlanTnlExtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlExtStatus.setStatus("current")
_RuijieVxlanTnlVniStatisticExtTable_Object = MibTable
ruijieVxlanTnlVniStatisticExtTable = _RuijieVxlanTnlVniStatisticExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtTable.setStatus("current")
_RuijieVxlanTnlVniStatisticExtEntry_Object = MibTableRow
ruijieVxlanTnlVniStatisticExtEntry = _RuijieVxlanTnlVniStatisticExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1)
)
ruijieVxlanTnlVniStatisticExtEntry.setIndexNames(
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtDestIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtDestIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtSourceIpType"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtSourceIp"),
    (0, "RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtVni"),
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtEntry.setStatus("current")


class _RuijieVxlanTnlVniStatisticExtDestIpType_Type(InetAddressType):
    """Custom type ruijieVxlanTnlVniStatisticExtDestIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanTnlVniStatisticExtDestIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanTnlVniStatisticExtDestIpType_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtDestIpType = _RuijieVxlanTnlVniStatisticExtDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 1),
    _RuijieVxlanTnlVniStatisticExtDestIpType_Type()
)
ruijieVxlanTnlVniStatisticExtDestIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtDestIpType.setStatus("current")
_RuijieVxlanTnlVniStatisticExtDestIp_Type = InetAddress
_RuijieVxlanTnlVniStatisticExtDestIp_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtDestIp = _RuijieVxlanTnlVniStatisticExtDestIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 2),
    _RuijieVxlanTnlVniStatisticExtDestIp_Type()
)
ruijieVxlanTnlVniStatisticExtDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtDestIp.setStatus("current")


class _RuijieVxlanTnlVniStatisticExtSourceIpType_Type(InetAddressType):
    """Custom type ruijieVxlanTnlVniStatisticExtSourceIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieVxlanTnlVniStatisticExtSourceIpType_Type.__name__ = "InetAddressType"
_RuijieVxlanTnlVniStatisticExtSourceIpType_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtSourceIpType = _RuijieVxlanTnlVniStatisticExtSourceIpType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 3),
    _RuijieVxlanTnlVniStatisticExtSourceIpType_Type()
)
ruijieVxlanTnlVniStatisticExtSourceIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtSourceIpType.setStatus("current")
_RuijieVxlanTnlVniStatisticExtSourceIp_Type = InetAddress
_RuijieVxlanTnlVniStatisticExtSourceIp_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtSourceIp = _RuijieVxlanTnlVniStatisticExtSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 4),
    _RuijieVxlanTnlVniStatisticExtSourceIp_Type()
)
ruijieVxlanTnlVniStatisticExtSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtSourceIp.setStatus("current")


class _RuijieVxlanTnlVniStatisticExtVni_Type(Unsigned32):
    """Custom type ruijieVxlanTnlVniStatisticExtVni based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RuijieVxlanTnlVniStatisticExtVni_Type.__name__ = "Unsigned32"
_RuijieVxlanTnlVniStatisticExtVni_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtVni = _RuijieVxlanTnlVniStatisticExtVni_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 5),
    _RuijieVxlanTnlVniStatisticExtVni_Type()
)
ruijieVxlanTnlVniStatisticExtVni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtVni.setStatus("current")
_RuijieVxlanTnlVniStatisticExtInPackets_Type = Counter64
_RuijieVxlanTnlVniStatisticExtInPackets_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtInPackets = _RuijieVxlanTnlVniStatisticExtInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 6),
    _RuijieVxlanTnlVniStatisticExtInPackets_Type()
)
ruijieVxlanTnlVniStatisticExtInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtInPackets.setStatus("current")
_RuijieVxlanTnlVniStatisticExtOutPackets_Type = Counter64
_RuijieVxlanTnlVniStatisticExtOutPackets_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtOutPackets = _RuijieVxlanTnlVniStatisticExtOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 7),
    _RuijieVxlanTnlVniStatisticExtOutPackets_Type()
)
ruijieVxlanTnlVniStatisticExtOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtOutPackets.setStatus("current")
_RuijieVxlanTnlVniStatisticExtInBytes_Type = Counter64
_RuijieVxlanTnlVniStatisticExtInBytes_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtInBytes = _RuijieVxlanTnlVniStatisticExtInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 8),
    _RuijieVxlanTnlVniStatisticExtInBytes_Type()
)
ruijieVxlanTnlVniStatisticExtInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtInBytes.setStatus("current")
_RuijieVxlanTnlVniStatisticExtOutBytes_Type = Counter64
_RuijieVxlanTnlVniStatisticExtOutBytes_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtOutBytes = _RuijieVxlanTnlVniStatisticExtOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 9),
    _RuijieVxlanTnlVniStatisticExtOutBytes_Type()
)
ruijieVxlanTnlVniStatisticExtOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtOutBytes.setStatus("current")
_RuijieVxlanTnlVniStatisticExtInPps_Type = Counter64
_RuijieVxlanTnlVniStatisticExtInPps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtInPps = _RuijieVxlanTnlVniStatisticExtInPps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 10),
    _RuijieVxlanTnlVniStatisticExtInPps_Type()
)
ruijieVxlanTnlVniStatisticExtInPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtInPps.setStatus("current")
_RuijieVxlanTnlVniStatisticExtOutPps_Type = Counter64
_RuijieVxlanTnlVniStatisticExtOutPps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtOutPps = _RuijieVxlanTnlVniStatisticExtOutPps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 11),
    _RuijieVxlanTnlVniStatisticExtOutPps_Type()
)
ruijieVxlanTnlVniStatisticExtOutPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtOutPps.setStatus("current")
_RuijieVxlanTnlVniStatisticExtInBps_Type = Counter64
_RuijieVxlanTnlVniStatisticExtInBps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtInBps = _RuijieVxlanTnlVniStatisticExtInBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 12),
    _RuijieVxlanTnlVniStatisticExtInBps_Type()
)
ruijieVxlanTnlVniStatisticExtInBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtInBps.setStatus("current")
_RuijieVxlanTnlVniStatisticExtOutBps_Type = Counter64
_RuijieVxlanTnlVniStatisticExtOutBps_Object = MibTableColumn
ruijieVxlanTnlVniStatisticExtOutBps = _RuijieVxlanTnlVniStatisticExtOutBps_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 1, 11, 1, 13),
    _RuijieVxlanTnlVniStatisticExtOutBps_Type()
)
ruijieVxlanTnlVniStatisticExtOutBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticExtOutBps.setStatus("current")
_RuijieVxlanMIBTraps_ObjectIdentity = ObjectIdentity
ruijieVxlanMIBTraps = _RuijieVxlanMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 2)
)
_RuijieVxlanMIBConformance_ObjectIdentity = ObjectIdentity
ruijieVxlanMIBConformance = _RuijieVxlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3)
)
_RuijieVxlanCompliances_ObjectIdentity = ObjectIdentity
ruijieVxlanCompliances = _RuijieVxlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 1)
)
_RuijieVxlanGroups_ObjectIdentity = ObjectIdentity
ruijieVxlanGroups = _RuijieVxlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2)
)

# Managed Objects groups

ruijieVxlanVniStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 1)
)
ruijieVxlanVniStatisticGroup.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticInPackets"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticOutPackets"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticInBytes"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticOutBytes"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticInPps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticOutPps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticInBps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticOutBps"))
)
if mibBuilder.loadTexts:
    ruijieVxlanVniStatisticGroup.setStatus("current")

ruijieVxlanStaticTnlCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 2)
)
ruijieVxlanStaticTnlCfgGroup.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlRowStatus"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlRowStatus"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlExtRowStatus"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniTnlExtRowStatus"))
)
if mibBuilder.loadTexts:
    ruijieVxlanStaticTnlCfgGroup.setStatus("current")

ruijieVxlanTnlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 3)
)
ruijieVxlanTnlGroup.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlPortNum"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlStatus"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtPortNum"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtStatus"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlGroup.setStatus("current")

ruijieVxlanTnlVniStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 4)
)
ruijieVxlanTnlVniStatisticGroup.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticInPackets"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticOutPackets"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticInBytes"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticOutBytes"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticInPps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticOutPps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticInBps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticOutBps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtInPackets"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtOutPackets"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtInBytes"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtOutBytes"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtInPps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtOutPps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtInBps"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticExtOutBps"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTnlVniStatisticGroup.setStatus("current")

ruijieVxlanVtepCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 5)
)
ruijieVxlanVtepCfgGroup.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanVtepSourceLoopbackNum"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVtepSourceIPv4Addr"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVtepSourceIPv6Addr"))
)
if mibBuilder.loadTexts:
    ruijieVxlanVtepCfgGroup.setStatus("current")

ruijieVxlanVlanAssoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 7)
)
ruijieVxlanVlanAssoGroup.setObjects(
    ("RUIJIE-VXLAN-MIB", "ruijieVxlanVlanAssoVni")
)
if mibBuilder.loadTexts:
    ruijieVxlanVlanAssoGroup.setStatus("current")


# Notification objects

ruijieVxlanTrapTnlUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 2, 1)
)
ruijieVxlanTrapTnlUp.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlDestIp"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlSourceIp"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTrapTnlUp.setStatus(
        "current"
    )

ruijieVxlanTrapTnlDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 2, 2)
)
ruijieVxlanTrapTnlDown.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlDestIp"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlSourceIp"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTrapTnlDown.setStatus(
        "current"
    )

ruijieVxlanTrapTnlExtUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 2, 3)
)
ruijieVxlanTrapTnlExtUp.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtDestIpType"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtDestIp"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtSourceIpType"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtSourceIp"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTrapTnlExtUp.setStatus(
        "current"
    )

ruijieVxlanTrapTnlExtDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 2, 4)
)
ruijieVxlanTrapTnlExtDown.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtDestIpType"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtDestIp"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtSourceIpType"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlExtSourceIp"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTrapTnlExtDown.setStatus(
        "current"
    )


# Notifications groups

ruijieVxlanTrapTnlStatusGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 2, 6)
)
ruijieVxlanTrapTnlStatusGroup.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanTrapTnlUp"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTrapTnlDown"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTrapTnlExtUp"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTrapTnlExtDown"))
)
if mibBuilder.loadTexts:
    ruijieVxlanTrapTnlStatusGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieVxlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 161, 3, 1, 1)
)
ruijieVxlanCompliance.setObjects(
      *(("RUIJIE-VXLAN-MIB", "ruijieVxlanStaticTnlCfgGroup"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlGroup"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVtepCfgGroup"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTrapTnlStatusGroup"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVlanAssoGroup"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanVniStatisticGroup"),
        ("RUIJIE-VXLAN-MIB", "ruijieVxlanTnlVniStatisticGroup"))
)
if mibBuilder.loadTexts:
    ruijieVxlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-VXLAN-MIB",
    **{"ruijieVxlanMIB": ruijieVxlanMIB,
       "ruijieVxlanMIBObjects": ruijieVxlanMIBObjects,
       "ruijieVxlanVniStatisticTable": ruijieVxlanVniStatisticTable,
       "ruijieVxlanVniStatisticEntry": ruijieVxlanVniStatisticEntry,
       "ruijieVxlanVniStatisticVni": ruijieVxlanVniStatisticVni,
       "ruijieVxlanVniStatisticInPackets": ruijieVxlanVniStatisticInPackets,
       "ruijieVxlanVniStatisticOutPackets": ruijieVxlanVniStatisticOutPackets,
       "ruijieVxlanVniStatisticInBytes": ruijieVxlanVniStatisticInBytes,
       "ruijieVxlanVniStatisticOutBytes": ruijieVxlanVniStatisticOutBytes,
       "ruijieVxlanVniStatisticInPps": ruijieVxlanVniStatisticInPps,
       "ruijieVxlanVniStatisticOutPps": ruijieVxlanVniStatisticOutPps,
       "ruijieVxlanVniStatisticInBps": ruijieVxlanVniStatisticInBps,
       "ruijieVxlanVniStatisticOutBps": ruijieVxlanVniStatisticOutBps,
       "ruijieVxlanStaticTnlTable": ruijieVxlanStaticTnlTable,
       "ruijieVxlanStaticTnlEntry": ruijieVxlanStaticTnlEntry,
       "ruijieVxlanStaticTnlDestIp": ruijieVxlanStaticTnlDestIp,
       "ruijieVxlanStaticTnlSourceIp": ruijieVxlanStaticTnlSourceIp,
       "ruijieVxlanStaticTnlRowStatus": ruijieVxlanStaticTnlRowStatus,
       "ruijieVxlanVniTnlTable": ruijieVxlanVniTnlTable,
       "ruijieVxlanVniTnlEntry": ruijieVxlanVniTnlEntry,
       "ruijieVxlanVniTnlVni": ruijieVxlanVniTnlVni,
       "ruijieVxlanVniTnlDestIp": ruijieVxlanVniTnlDestIp,
       "ruijieVxlanVniTnlSourceIp": ruijieVxlanVniTnlSourceIp,
       "ruijieVxlanVniTnlRowStatus": ruijieVxlanVniTnlRowStatus,
       "ruijieVxlanTnlTable": ruijieVxlanTnlTable,
       "ruijieVxlanTnlEntry": ruijieVxlanTnlEntry,
       "ruijieVxlanTnlDestIp": ruijieVxlanTnlDestIp,
       "ruijieVxlanTnlSourceIp": ruijieVxlanTnlSourceIp,
       "ruijieVxlanTnlPortNum": ruijieVxlanTnlPortNum,
       "ruijieVxlanTnlStatus": ruijieVxlanTnlStatus,
       "ruijieVxlanTnlVniStatisticTable": ruijieVxlanTnlVniStatisticTable,
       "ruijieVxlanTnlVniStatisticEntry": ruijieVxlanTnlVniStatisticEntry,
       "ruijieVxlanTnlVniStatisticDestIp": ruijieVxlanTnlVniStatisticDestIp,
       "ruijieVxlanTnlVniStatisticSourceIp": ruijieVxlanTnlVniStatisticSourceIp,
       "ruijieVxlanTnlVniStatisticVni": ruijieVxlanTnlVniStatisticVni,
       "ruijieVxlanTnlVniStatisticInPackets": ruijieVxlanTnlVniStatisticInPackets,
       "ruijieVxlanTnlVniStatisticOutPackets": ruijieVxlanTnlVniStatisticOutPackets,
       "ruijieVxlanTnlVniStatisticInBytes": ruijieVxlanTnlVniStatisticInBytes,
       "ruijieVxlanTnlVniStatisticOutBytes": ruijieVxlanTnlVniStatisticOutBytes,
       "ruijieVxlanTnlVniStatisticInPps": ruijieVxlanTnlVniStatisticInPps,
       "ruijieVxlanTnlVniStatisticOutPps": ruijieVxlanTnlVniStatisticOutPps,
       "ruijieVxlanTnlVniStatisticInBps": ruijieVxlanTnlVniStatisticInBps,
       "ruijieVxlanTnlVniStatisticOutBps": ruijieVxlanTnlVniStatisticOutBps,
       "ruijieVxlanVtepTable": ruijieVxlanVtepTable,
       "ruijieVxlanVtepEntry": ruijieVxlanVtepEntry,
       "ruijieVxlanVtepId": ruijieVxlanVtepId,
       "ruijieVxlanVtepSourceLoopbackNum": ruijieVxlanVtepSourceLoopbackNum,
       "ruijieVxlanVtepSourceIPv4Addr": ruijieVxlanVtepSourceIPv4Addr,
       "ruijieVxlanVtepSourceIPv6Addr": ruijieVxlanVtepSourceIPv6Addr,
       "ruijieVxlanVlanAssoTable": ruijieVxlanVlanAssoTable,
       "ruijieVxlanVlanAssoEntry": ruijieVxlanVlanAssoEntry,
       "ruijieVxlanVlanAssoVid": ruijieVxlanVlanAssoVid,
       "ruijieVxlanVlanAssoVni": ruijieVxlanVlanAssoVni,
       "ruijieVxlanStaticTnlExtTable": ruijieVxlanStaticTnlExtTable,
       "ruijieVxlanStaticTnlExtEntry": ruijieVxlanStaticTnlExtEntry,
       "ruijieVxlanStaticTnlExtDestIpType": ruijieVxlanStaticTnlExtDestIpType,
       "ruijieVxlanStaticTnlExtDestIp": ruijieVxlanStaticTnlExtDestIp,
       "ruijieVxlanStaticTnlExtSourceIpType": ruijieVxlanStaticTnlExtSourceIpType,
       "ruijieVxlanStaticTnlExtSourceIp": ruijieVxlanStaticTnlExtSourceIp,
       "ruijieVxlanStaticTnlExtRowStatus": ruijieVxlanStaticTnlExtRowStatus,
       "ruijieVxlanVniTnlExtTable": ruijieVxlanVniTnlExtTable,
       "ruijieVxlanVniTnlExtEntry": ruijieVxlanVniTnlExtEntry,
       "ruijieVxlanVniTnlExtVni": ruijieVxlanVniTnlExtVni,
       "ruijieVxlanVniTnlExtDestIpType": ruijieVxlanVniTnlExtDestIpType,
       "ruijieVxlanVniTnlExtDestIp": ruijieVxlanVniTnlExtDestIp,
       "ruijieVxlanVniTnlExtSourceIpType": ruijieVxlanVniTnlExtSourceIpType,
       "ruijieVxlanVniTnlExtSourceIp": ruijieVxlanVniTnlExtSourceIp,
       "ruijieVxlanVniTnlExtRowStatus": ruijieVxlanVniTnlExtRowStatus,
       "ruijieVxlanTnlExtTable": ruijieVxlanTnlExtTable,
       "ruijieVxlanTnlExtEntry": ruijieVxlanTnlExtEntry,
       "ruijieVxlanTnlExtDestIpType": ruijieVxlanTnlExtDestIpType,
       "ruijieVxlanTnlExtDestIp": ruijieVxlanTnlExtDestIp,
       "ruijieVxlanTnlExtSourceIpType": ruijieVxlanTnlExtSourceIpType,
       "ruijieVxlanTnlExtSourceIp": ruijieVxlanTnlExtSourceIp,
       "ruijieVxlanTnlExtPortNum": ruijieVxlanTnlExtPortNum,
       "ruijieVxlanTnlExtStatus": ruijieVxlanTnlExtStatus,
       "ruijieVxlanTnlVniStatisticExtTable": ruijieVxlanTnlVniStatisticExtTable,
       "ruijieVxlanTnlVniStatisticExtEntry": ruijieVxlanTnlVniStatisticExtEntry,
       "ruijieVxlanTnlVniStatisticExtDestIpType": ruijieVxlanTnlVniStatisticExtDestIpType,
       "ruijieVxlanTnlVniStatisticExtDestIp": ruijieVxlanTnlVniStatisticExtDestIp,
       "ruijieVxlanTnlVniStatisticExtSourceIpType": ruijieVxlanTnlVniStatisticExtSourceIpType,
       "ruijieVxlanTnlVniStatisticExtSourceIp": ruijieVxlanTnlVniStatisticExtSourceIp,
       "ruijieVxlanTnlVniStatisticExtVni": ruijieVxlanTnlVniStatisticExtVni,
       "ruijieVxlanTnlVniStatisticExtInPackets": ruijieVxlanTnlVniStatisticExtInPackets,
       "ruijieVxlanTnlVniStatisticExtOutPackets": ruijieVxlanTnlVniStatisticExtOutPackets,
       "ruijieVxlanTnlVniStatisticExtInBytes": ruijieVxlanTnlVniStatisticExtInBytes,
       "ruijieVxlanTnlVniStatisticExtOutBytes": ruijieVxlanTnlVniStatisticExtOutBytes,
       "ruijieVxlanTnlVniStatisticExtInPps": ruijieVxlanTnlVniStatisticExtInPps,
       "ruijieVxlanTnlVniStatisticExtOutPps": ruijieVxlanTnlVniStatisticExtOutPps,
       "ruijieVxlanTnlVniStatisticExtInBps": ruijieVxlanTnlVniStatisticExtInBps,
       "ruijieVxlanTnlVniStatisticExtOutBps": ruijieVxlanTnlVniStatisticExtOutBps,
       "ruijieVxlanMIBTraps": ruijieVxlanMIBTraps,
       "ruijieVxlanTrapTnlUp": ruijieVxlanTrapTnlUp,
       "ruijieVxlanTrapTnlDown": ruijieVxlanTrapTnlDown,
       "ruijieVxlanTrapTnlExtUp": ruijieVxlanTrapTnlExtUp,
       "ruijieVxlanTrapTnlExtDown": ruijieVxlanTrapTnlExtDown,
       "ruijieVxlanMIBConformance": ruijieVxlanMIBConformance,
       "ruijieVxlanCompliances": ruijieVxlanCompliances,
       "ruijieVxlanCompliance": ruijieVxlanCompliance,
       "ruijieVxlanGroups": ruijieVxlanGroups,
       "ruijieVxlanVniStatisticGroup": ruijieVxlanVniStatisticGroup,
       "ruijieVxlanStaticTnlCfgGroup": ruijieVxlanStaticTnlCfgGroup,
       "ruijieVxlanTnlGroup": ruijieVxlanTnlGroup,
       "ruijieVxlanTnlVniStatisticGroup": ruijieVxlanTnlVniStatisticGroup,
       "ruijieVxlanVtepCfgGroup": ruijieVxlanVtepCfgGroup,
       "ruijieVxlanTrapTnlStatusGroup": ruijieVxlanTrapTnlStatusGroup,
       "ruijieVxlanVlanAssoGroup": ruijieVxlanVlanAssoGroup}
)
