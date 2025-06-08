# SNMP MIB module (RUIJIE-MPLS-L3VPN-RES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MPLS-L3VPN-RES-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsL3VpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfName")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ruijiemplsL3VpnResMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123)
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResMIB.setRevisions(
        ("2013-02-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiemplsL3VpnResMIBObjects_ObjectIdentity = ObjectIdentity
ruijiemplsL3VpnResMIBObjects = _RuijiemplsL3VpnResMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1)
)
_RuijiemplsL3VpnResTable_Object = MibTable
ruijiemplsL3VpnResTable = _RuijiemplsL3VpnResTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResTable.setStatus("current")
_RuijiemplsL3VpnResEntry_Object = MibTableRow
ruijiemplsL3VpnResEntry = _RuijiemplsL3VpnResEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1)
)
ruijiemplsL3VpnResEntry.setIndexNames(
    (0, "RUIJIE-MPLS-L3VPN-RES-MIB", "ruijiemplsL3VpnResPeAddr"),
    (0, "RUIJIE-MPLS-L3VPN-RES-MIB", "ruijiemplsL3VpnResVrfName"),
)
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResEntry.setStatus("current")
_RuijiemplsL3VpnResPeAddr_Type = InetAddress
_RuijiemplsL3VpnResPeAddr_Object = MibTableColumn
ruijiemplsL3VpnResPeAddr = _RuijiemplsL3VpnResPeAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 1),
    _RuijiemplsL3VpnResPeAddr_Type()
)
ruijiemplsL3VpnResPeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResPeAddr.setStatus("current")
_RuijiemplsL3VpnResVrfName_Type = DisplayString
_RuijiemplsL3VpnResVrfName_Object = MibTableColumn
ruijiemplsL3VpnResVrfName = _RuijiemplsL3VpnResVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 2),
    _RuijiemplsL3VpnResVrfName_Type()
)
ruijiemplsL3VpnResVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResVrfName.setStatus("current")
_RuijiemplsL3VpnResRtCollect_Type = DisplayString
_RuijiemplsL3VpnResRtCollect_Object = MibTableColumn
ruijiemplsL3VpnResRtCollect = _RuijiemplsL3VpnResRtCollect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 3),
    _RuijiemplsL3VpnResRtCollect_Type()
)
ruijiemplsL3VpnResRtCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResRtCollect.setStatus("current")
_RuijiemplsL3VpnResRdCollect_Type = DisplayString
_RuijiemplsL3VpnResRdCollect_Object = MibTableColumn
ruijiemplsL3VpnResRdCollect = _RuijiemplsL3VpnResRdCollect_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 4),
    _RuijiemplsL3VpnResRdCollect_Type()
)
ruijiemplsL3VpnResRdCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResRdCollect.setStatus("current")
_RuijiemplsL3VpnResIntfAddr_Type = InetAddress
_RuijiemplsL3VpnResIntfAddr_Object = MibTableColumn
ruijiemplsL3VpnResIntfAddr = _RuijiemplsL3VpnResIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 5),
    _RuijiemplsL3VpnResIntfAddr_Type()
)
ruijiemplsL3VpnResIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResIntfAddr.setStatus("current")
_RuijiemplsL3VpnResImptRt_Type = DisplayString
_RuijiemplsL3VpnResImptRt_Object = MibTableColumn
ruijiemplsL3VpnResImptRt = _RuijiemplsL3VpnResImptRt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 6),
    _RuijiemplsL3VpnResImptRt_Type()
)
ruijiemplsL3VpnResImptRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResImptRt.setStatus("current")
_RuijiemplsL3VpnResExptRt_Type = DisplayString
_RuijiemplsL3VpnResExptRt_Object = MibTableColumn
ruijiemplsL3VpnResExptRt = _RuijiemplsL3VpnResExptRt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 123, 1, 1, 1, 7),
    _RuijiemplsL3VpnResExptRt_Type()
)
ruijiemplsL3VpnResExptRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiemplsL3VpnResExptRt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MPLS-L3VPN-RES-MIB",
    **{"ruijiemplsL3VpnResMIB": ruijiemplsL3VpnResMIB,
       "ruijiemplsL3VpnResMIBObjects": ruijiemplsL3VpnResMIBObjects,
       "ruijiemplsL3VpnResTable": ruijiemplsL3VpnResTable,
       "ruijiemplsL3VpnResEntry": ruijiemplsL3VpnResEntry,
       "ruijiemplsL3VpnResPeAddr": ruijiemplsL3VpnResPeAddr,
       "ruijiemplsL3VpnResVrfName": ruijiemplsL3VpnResVrfName,
       "ruijiemplsL3VpnResRtCollect": ruijiemplsL3VpnResRtCollect,
       "ruijiemplsL3VpnResRdCollect": ruijiemplsL3VpnResRdCollect,
       "ruijiemplsL3VpnResIntfAddr": ruijiemplsL3VpnResIntfAddr,
       "ruijiemplsL3VpnResImptRt": ruijiemplsL3VpnResImptRt,
       "ruijiemplsL3VpnResExptRt": ruijiemplsL3VpnResExptRt}
)
