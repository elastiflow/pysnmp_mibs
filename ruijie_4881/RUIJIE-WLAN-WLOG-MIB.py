# SNMP MIB module (RUIJIE-WLAN-WLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WLAN-WLOG-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:52:30 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieWlanWlogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118)
)
if mibBuilder.loadTexts:
    ruijieWlanWlogMIB.setRevisions(
        ("2012-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWlanWlogNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWlanWlogNotificationsMIBObjects = _RuijieWlanWlogNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1)
)
_RuijieWlanWlogNtfObjects_ObjectIdentity = ObjectIdentity
ruijieWlanWlogNtfObjects = _RuijieWlanWlogNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1)
)
_RuijieWlogNotifyApName_Type = DisplayString
_RuijieWlogNotifyApName_Object = MibScalar
ruijieWlogNotifyApName = _RuijieWlogNotifyApName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 1),
    _RuijieWlogNotifyApName_Type()
)
ruijieWlogNotifyApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApName.setStatus("current")
_RuijieWlogNotifyApMac_Type = MacAddress
_RuijieWlogNotifyApMac_Object = MibScalar
ruijieWlogNotifyApMac = _RuijieWlogNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 2),
    _RuijieWlogNotifyApMac_Type()
)
ruijieWlogNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApMac.setStatus("current")
_RuijieWlogNotifyApIp_Type = InetAddress
_RuijieWlogNotifyApIp_Object = MibScalar
ruijieWlogNotifyApIp = _RuijieWlogNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 3),
    _RuijieWlogNotifyApIp_Type()
)
ruijieWlogNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIp.setStatus("current")
_RuijieWlogNotifyApCwDownId_Type = Integer32
_RuijieWlogNotifyApCwDownId_Object = MibScalar
ruijieWlogNotifyApCwDownId = _RuijieWlogNotifyApCwDownId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 4),
    _RuijieWlogNotifyApCwDownId_Type()
)
ruijieWlogNotifyApCwDownId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApCwDownId.setStatus("current")
_RuijieWlogNotifyApCwDownReason_Type = DisplayString
_RuijieWlogNotifyApCwDownReason_Object = MibScalar
ruijieWlogNotifyApCwDownReason = _RuijieWlogNotifyApCwDownReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 5),
    _RuijieWlogNotifyApCwDownReason_Type()
)
ruijieWlogNotifyApCwDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApCwDownReason.setStatus("current")
_RuijieWlogNotifyApIntfStatTable_Object = MibTable
ruijieWlogNotifyApIntfStatTable = _RuijieWlogNotifyApIntfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfStatTable.setStatus("current")
_RuijieWlogNotifyApIntfStatEntry_Object = MibTableRow
ruijieWlogNotifyApIntfStatEntry = _RuijieWlogNotifyApIntfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1)
)
ruijieWlogNotifyApIntfStatEntry.setIndexNames(
    (0, "RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfName"),
)
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfStatEntry.setStatus("current")
_RuijieWlogNotifyApIntfName_Type = DisplayString
_RuijieWlogNotifyApIntfName_Object = MibTableColumn
ruijieWlogNotifyApIntfName = _RuijieWlogNotifyApIntfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 1),
    _RuijieWlogNotifyApIntfName_Type()
)
ruijieWlogNotifyApIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfName.setStatus("current")
_RuijieWlogNotifyApIntfInputRate_Type = Integer32
_RuijieWlogNotifyApIntfInputRate_Object = MibTableColumn
ruijieWlogNotifyApIntfInputRate = _RuijieWlogNotifyApIntfInputRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 2),
    _RuijieWlogNotifyApIntfInputRate_Type()
)
ruijieWlogNotifyApIntfInputRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfInputRate.setStatus("current")
_RuijieWlogNotifyApIntfOutputRate_Type = Integer32
_RuijieWlogNotifyApIntfOutputRate_Object = MibTableColumn
ruijieWlogNotifyApIntfOutputRate = _RuijieWlogNotifyApIntfOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 3),
    _RuijieWlogNotifyApIntfOutputRate_Type()
)
ruijieWlogNotifyApIntfOutputRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfOutputRate.setStatus("current")
_RuijieWlogNotifyApIntfUnicastInputPkts_Type = Integer32
_RuijieWlogNotifyApIntfUnicastInputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfUnicastInputPkts = _RuijieWlogNotifyApIntfUnicastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 4),
    _RuijieWlogNotifyApIntfUnicastInputPkts_Type()
)
ruijieWlogNotifyApIntfUnicastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfUnicastInputPkts.setStatus("current")
_RuijieWlogNotifyApIntfUnicastOutputPkts_Type = Integer32
_RuijieWlogNotifyApIntfUnicastOutputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfUnicastOutputPkts = _RuijieWlogNotifyApIntfUnicastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 5),
    _RuijieWlogNotifyApIntfUnicastOutputPkts_Type()
)
ruijieWlogNotifyApIntfUnicastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfUnicastOutputPkts.setStatus("current")
_RuijieWlogNotifyApIntfMulticastInputPkts_Type = Integer32
_RuijieWlogNotifyApIntfMulticastInputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfMulticastInputPkts = _RuijieWlogNotifyApIntfMulticastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 6),
    _RuijieWlogNotifyApIntfMulticastInputPkts_Type()
)
ruijieWlogNotifyApIntfMulticastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfMulticastInputPkts.setStatus("current")
_RuijieWlogNotifyApIntfMulticastOutputPkts_Type = Integer32
_RuijieWlogNotifyApIntfMulticastOutputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfMulticastOutputPkts = _RuijieWlogNotifyApIntfMulticastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 7),
    _RuijieWlogNotifyApIntfMulticastOutputPkts_Type()
)
ruijieWlogNotifyApIntfMulticastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfMulticastOutputPkts.setStatus("current")
_RuijieWlogNotifyApIntfBroadcastInputPkts_Type = Integer32
_RuijieWlogNotifyApIntfBroadcastInputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfBroadcastInputPkts = _RuijieWlogNotifyApIntfBroadcastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 8),
    _RuijieWlogNotifyApIntfBroadcastInputPkts_Type()
)
ruijieWlogNotifyApIntfBroadcastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfBroadcastInputPkts.setStatus("current")
_RuijieWlogNotifyApIntfBroadcastOutputPkts_Type = Integer32
_RuijieWlogNotifyApIntfBroadcastOutputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfBroadcastOutputPkts = _RuijieWlogNotifyApIntfBroadcastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 9),
    _RuijieWlogNotifyApIntfBroadcastOutputPkts_Type()
)
ruijieWlogNotifyApIntfBroadcastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfBroadcastOutputPkts.setStatus("current")
_RuijieWlogNotifyApIntfErrorInputPkts_Type = Integer32
_RuijieWlogNotifyApIntfErrorInputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfErrorInputPkts = _RuijieWlogNotifyApIntfErrorInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 10),
    _RuijieWlogNotifyApIntfErrorInputPkts_Type()
)
ruijieWlogNotifyApIntfErrorInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfErrorInputPkts.setStatus("current")
_RuijieWlogNotifyApIntfErrorOutputPkts_Type = Integer32
_RuijieWlogNotifyApIntfErrorOutputPkts_Object = MibTableColumn
ruijieWlogNotifyApIntfErrorOutputPkts = _RuijieWlogNotifyApIntfErrorOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 6, 1, 11),
    _RuijieWlogNotifyApIntfErrorOutputPkts_Type()
)
ruijieWlogNotifyApIntfErrorOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApIntfErrorOutputPkts.setStatus("current")
_RuijieWlogNotifyApRadioStatTable_Object = MibTable
ruijieWlogNotifyApRadioStatTable = _RuijieWlogNotifyApRadioStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioStatTable.setStatus("current")
_RuijieWlogNotifyApRadioStatEntry_Object = MibTableRow
ruijieWlogNotifyApRadioStatEntry = _RuijieWlogNotifyApRadioStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1)
)
ruijieWlogNotifyApRadioStatEntry.setIndexNames(
    (0, "RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioId"),
)
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioStatEntry.setStatus("current")
_RuijieWlogNotifyApRadioId_Type = Integer32
_RuijieWlogNotifyApRadioId_Object = MibTableColumn
ruijieWlogNotifyApRadioId = _RuijieWlogNotifyApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 1),
    _RuijieWlogNotifyApRadioId_Type()
)
ruijieWlogNotifyApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioId.setStatus("current")
_RuijieWlogNotifyApRadioWorkChnl_Type = Integer32
_RuijieWlogNotifyApRadioWorkChnl_Object = MibTableColumn
ruijieWlogNotifyApRadioWorkChnl = _RuijieWlogNotifyApRadioWorkChnl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 2),
    _RuijieWlogNotifyApRadioWorkChnl_Type()
)
ruijieWlogNotifyApRadioWorkChnl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioWorkChnl.setStatus("current")
_RuijieWlogNotifyApRadioPower_Type = Integer32
_RuijieWlogNotifyApRadioPower_Object = MibTableColumn
ruijieWlogNotifyApRadioPower = _RuijieWlogNotifyApRadioPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 3),
    _RuijieWlogNotifyApRadioPower_Type()
)
ruijieWlogNotifyApRadioPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioPower.setStatus("current")
_RuijieWlogNotifyApRadioRssi_Type = Integer32
_RuijieWlogNotifyApRadioRssi_Object = MibTableColumn
ruijieWlogNotifyApRadioRssi = _RuijieWlogNotifyApRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 4),
    _RuijieWlogNotifyApRadioRssi_Type()
)
ruijieWlogNotifyApRadioRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioRssi.setStatus("current")
_RuijieWlogNotifyApRadioErrFrame_Type = Integer32
_RuijieWlogNotifyApRadioErrFrame_Object = MibTableColumn
ruijieWlogNotifyApRadioErrFrame = _RuijieWlogNotifyApRadioErrFrame_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 5),
    _RuijieWlogNotifyApRadioErrFrame_Type()
)
ruijieWlogNotifyApRadioErrFrame.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioErrFrame.setStatus("current")
_RuijieWlogNotifyApRadioRetrsmit_Type = Integer32
_RuijieWlogNotifyApRadioRetrsmit_Object = MibTableColumn
ruijieWlogNotifyApRadioRetrsmit = _RuijieWlogNotifyApRadioRetrsmit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 6),
    _RuijieWlogNotifyApRadioRetrsmit_Type()
)
ruijieWlogNotifyApRadioRetrsmit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioRetrsmit.setStatus("current")
_RuijieWlogNotifyApRadioTotalStaNum_Type = Integer32
_RuijieWlogNotifyApRadioTotalStaNum_Object = MibTableColumn
ruijieWlogNotifyApRadioTotalStaNum = _RuijieWlogNotifyApRadioTotalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 7),
    _RuijieWlogNotifyApRadioTotalStaNum_Type()
)
ruijieWlogNotifyApRadioTotalStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioTotalStaNum.setStatus("current")
_RuijieWlogNotifyApRadioWebStaNum_Type = Integer32
_RuijieWlogNotifyApRadioWebStaNum_Object = MibTableColumn
ruijieWlogNotifyApRadioWebStaNum = _RuijieWlogNotifyApRadioWebStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 8),
    _RuijieWlogNotifyApRadioWebStaNum_Type()
)
ruijieWlogNotifyApRadioWebStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioWebStaNum.setStatus("current")
_RuijieWlogNotifyApRadioD1xStaNum_Type = Integer32
_RuijieWlogNotifyApRadioD1xStaNum_Object = MibTableColumn
ruijieWlogNotifyApRadioD1xStaNum = _RuijieWlogNotifyApRadioD1xStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 7, 1, 9),
    _RuijieWlogNotifyApRadioD1xStaNum_Type()
)
ruijieWlogNotifyApRadioD1xStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyApRadioD1xStaNum.setStatus("current")
_RuijieWlogNotifyStaMac_Type = MacAddress
_RuijieWlogNotifyStaMac_Object = MibScalar
ruijieWlogNotifyStaMac = _RuijieWlogNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 8),
    _RuijieWlogNotifyStaMac_Type()
)
ruijieWlogNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaMac.setStatus("current")
_RuijieWlogNotifyStaIp_Type = IpAddress
_RuijieWlogNotifyStaIp_Object = MibScalar
ruijieWlogNotifyStaIp = _RuijieWlogNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 9),
    _RuijieWlogNotifyStaIp_Type()
)
ruijieWlogNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaIp.setStatus("current")
_RuijieWlogNotifyStaIpv6_Type = InetAddress
_RuijieWlogNotifyStaIpv6_Object = MibScalar
ruijieWlogNotifyStaIpv6 = _RuijieWlogNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 10),
    _RuijieWlogNotifyStaIpv6_Type()
)
ruijieWlogNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaIpv6.setStatus("current")
_RuijieWlogNotifySsid_Type = DisplayString
_RuijieWlogNotifySsid_Object = MibScalar
ruijieWlogNotifySsid = _RuijieWlogNotifySsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 11),
    _RuijieWlogNotifySsid_Type()
)
ruijieWlogNotifySsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifySsid.setStatus("current")
_RuijieWlogNotifyStaRssi_Type = Integer32
_RuijieWlogNotifyStaRssi_Object = MibScalar
ruijieWlogNotifyStaRssi = _RuijieWlogNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 12),
    _RuijieWlogNotifyStaRssi_Type()
)
ruijieWlogNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaRssi.setStatus("current")
_RuijieWlogNotifyStaLinkrate_Type = Integer32
_RuijieWlogNotifyStaLinkrate_Object = MibScalar
ruijieWlogNotifyStaLinkrate = _RuijieWlogNotifyStaLinkrate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 13),
    _RuijieWlogNotifyStaLinkrate_Type()
)
ruijieWlogNotifyStaLinkrate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaLinkrate.setStatus("current")
_RuijieWlogNotifyStaOperType_Type = Integer32
_RuijieWlogNotifyStaOperType_Object = MibScalar
ruijieWlogNotifyStaOperType = _RuijieWlogNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 14),
    _RuijieWlogNotifyStaOperType_Type()
)
ruijieWlogNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaOperType.setStatus("current")
_RuijieWlogNotifyStaAbnormalOperType_Type = Integer32
_RuijieWlogNotifyStaAbnormalOperType_Object = MibScalar
ruijieWlogNotifyStaAbnormalOperType = _RuijieWlogNotifyStaAbnormalOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 15),
    _RuijieWlogNotifyStaAbnormalOperType_Type()
)
ruijieWlogNotifyStaAbnormalOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaAbnormalOperType.setStatus("current")
_RuijieWlogNotifyStaOperReason_Type = DisplayString
_RuijieWlogNotifyStaOperReason_Object = MibScalar
ruijieWlogNotifyStaOperReason = _RuijieWlogNotifyStaOperReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 1, 16),
    _RuijieWlogNotifyStaOperReason_Type()
)
ruijieWlogNotifyStaOperReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWlogNotifyStaOperReason.setStatus("current")
_RuijieWlanWlogNotifications_ObjectIdentity = ObjectIdentity
ruijieWlanWlogNotifications = _RuijieWlanWlogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 2)
)

# Managed Objects groups


# Notification objects

ruijieNotifyApCapwapDownReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 2, 1)
)
ruijieNotifyApCapwapDownReason.setObjects(
      *(("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApName"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApMac"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIp"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApCwDownId"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApCwDownReason"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApCapwapDownReason.setStatus(
        "current"
    )

ruijieNotifyApCapwapDownIntf = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 2, 2)
)
ruijieNotifyApCapwapDownIntf.setObjects(
      *(("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApName"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApMac"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIp"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApCwDownId"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfName"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfInputRate"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfOutputRate"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfUnicastInputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfUnicastOutputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfMulticastInputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfMulticastOutputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfBroadcastInputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfBroadcastOutputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfErrorInputPkts"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIntfErrorOutputPkts"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApCapwapDownIntf.setStatus(
        "current"
    )

ruijieNotifyApCapwapDownRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 2, 3)
)
ruijieNotifyApCapwapDownRadio.setObjects(
      *(("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApName"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApMac"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApIp"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApCwDownId"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioId"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioWorkChnl"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioPower"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioRssi"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioErrFrame"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioRetrsmit"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioTotalStaNum"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioWebStaNum"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApRadioD1xStaNum"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApCapwapDownRadio.setStatus(
        "current"
    )

ruijieNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 2, 4)
)
ruijieNotifyStaOper.setObjects(
      *(("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaMac"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaIp"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaIpv6"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaRssi"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaLinkrate"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyApName"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifySsid"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaOperType"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaOper.setStatus(
        "current"
    )

ruijieNotifyStaAbnormalOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 118, 1, 2, 5)
)
ruijieNotifyStaAbnormalOper.setObjects(
      *(("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaMac"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaIp"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaIpv6"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaAbnormalOperType"),
        ("RUIJIE-WLAN-WLOG-MIB", "ruijieWlogNotifyStaOperReason"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaAbnormalOper.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WLAN-WLOG-MIB",
    **{"ruijieWlanWlogMIB": ruijieWlanWlogMIB,
       "ruijieWlanWlogNotificationsMIBObjects": ruijieWlanWlogNotificationsMIBObjects,
       "ruijieWlanWlogNtfObjects": ruijieWlanWlogNtfObjects,
       "ruijieWlogNotifyApName": ruijieWlogNotifyApName,
       "ruijieWlogNotifyApMac": ruijieWlogNotifyApMac,
       "ruijieWlogNotifyApIp": ruijieWlogNotifyApIp,
       "ruijieWlogNotifyApCwDownId": ruijieWlogNotifyApCwDownId,
       "ruijieWlogNotifyApCwDownReason": ruijieWlogNotifyApCwDownReason,
       "ruijieWlogNotifyApIntfStatTable": ruijieWlogNotifyApIntfStatTable,
       "ruijieWlogNotifyApIntfStatEntry": ruijieWlogNotifyApIntfStatEntry,
       "ruijieWlogNotifyApIntfName": ruijieWlogNotifyApIntfName,
       "ruijieWlogNotifyApIntfInputRate": ruijieWlogNotifyApIntfInputRate,
       "ruijieWlogNotifyApIntfOutputRate": ruijieWlogNotifyApIntfOutputRate,
       "ruijieWlogNotifyApIntfUnicastInputPkts": ruijieWlogNotifyApIntfUnicastInputPkts,
       "ruijieWlogNotifyApIntfUnicastOutputPkts": ruijieWlogNotifyApIntfUnicastOutputPkts,
       "ruijieWlogNotifyApIntfMulticastInputPkts": ruijieWlogNotifyApIntfMulticastInputPkts,
       "ruijieWlogNotifyApIntfMulticastOutputPkts": ruijieWlogNotifyApIntfMulticastOutputPkts,
       "ruijieWlogNotifyApIntfBroadcastInputPkts": ruijieWlogNotifyApIntfBroadcastInputPkts,
       "ruijieWlogNotifyApIntfBroadcastOutputPkts": ruijieWlogNotifyApIntfBroadcastOutputPkts,
       "ruijieWlogNotifyApIntfErrorInputPkts": ruijieWlogNotifyApIntfErrorInputPkts,
       "ruijieWlogNotifyApIntfErrorOutputPkts": ruijieWlogNotifyApIntfErrorOutputPkts,
       "ruijieWlogNotifyApRadioStatTable": ruijieWlogNotifyApRadioStatTable,
       "ruijieWlogNotifyApRadioStatEntry": ruijieWlogNotifyApRadioStatEntry,
       "ruijieWlogNotifyApRadioId": ruijieWlogNotifyApRadioId,
       "ruijieWlogNotifyApRadioWorkChnl": ruijieWlogNotifyApRadioWorkChnl,
       "ruijieWlogNotifyApRadioPower": ruijieWlogNotifyApRadioPower,
       "ruijieWlogNotifyApRadioRssi": ruijieWlogNotifyApRadioRssi,
       "ruijieWlogNotifyApRadioErrFrame": ruijieWlogNotifyApRadioErrFrame,
       "ruijieWlogNotifyApRadioRetrsmit": ruijieWlogNotifyApRadioRetrsmit,
       "ruijieWlogNotifyApRadioTotalStaNum": ruijieWlogNotifyApRadioTotalStaNum,
       "ruijieWlogNotifyApRadioWebStaNum": ruijieWlogNotifyApRadioWebStaNum,
       "ruijieWlogNotifyApRadioD1xStaNum": ruijieWlogNotifyApRadioD1xStaNum,
       "ruijieWlogNotifyStaMac": ruijieWlogNotifyStaMac,
       "ruijieWlogNotifyStaIp": ruijieWlogNotifyStaIp,
       "ruijieWlogNotifyStaIpv6": ruijieWlogNotifyStaIpv6,
       "ruijieWlogNotifySsid": ruijieWlogNotifySsid,
       "ruijieWlogNotifyStaRssi": ruijieWlogNotifyStaRssi,
       "ruijieWlogNotifyStaLinkrate": ruijieWlogNotifyStaLinkrate,
       "ruijieWlogNotifyStaOperType": ruijieWlogNotifyStaOperType,
       "ruijieWlogNotifyStaAbnormalOperType": ruijieWlogNotifyStaAbnormalOperType,
       "ruijieWlogNotifyStaOperReason": ruijieWlogNotifyStaOperReason,
       "ruijieWlanWlogNotifications": ruijieWlanWlogNotifications,
       "ruijieNotifyApCapwapDownReason": ruijieNotifyApCapwapDownReason,
       "ruijieNotifyApCapwapDownIntf": ruijieNotifyApCapwapDownIntf,
       "ruijieNotifyApCapwapDownRadio": ruijieNotifyApCapwapDownRadio,
       "ruijieNotifyStaOper": ruijieNotifyStaOper,
       "ruijieNotifyStaAbnormalOper": ruijieNotifyStaAbnormalOper}
)
