# SNMP MIB module (BELAIR-IEEE802DOT11-CLIENT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-IEEE802DOT11-CLIENT.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairDot11SsidIndex,) = mibBuilder.importSymbols(
    "BELAIR-IEEE802DOT11",
    "belairDot11SsidIndex")

(belairInterfaces,
 belairModules) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairInterfaces",
    "belairModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

belairIeeeDot11ClientMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7)
)
if mibBuilder.loadTexts:
    belairIeeeDot11ClientMib.setRevisions(
        ("2009-09-10 10:30",
         "2009-07-31 10:45",
         "2008-09-22 13:45",
         "2008-05-28 12:00",
         "2007-11-06 14:25")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairDot11ClientObjects_ObjectIdentity = ObjectIdentity
belairDot11ClientObjects = _BelairDot11ClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1)
)
_BelairDot11ClientTable_Object = MibTable
belairDot11ClientTable = _BelairDot11ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    belairDot11ClientTable.setStatus("current")
_BelairDot11ClientEntry_Object = MibTableRow
belairDot11ClientEntry = _BelairDot11ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1)
)
belairDot11ClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BELAIR-IEEE802DOT11", "belairDot11SsidIndex"),
    (0, "BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientMacAddress"),
)
if mibBuilder.loadTexts:
    belairDot11ClientEntry.setStatus("current")
_BelairDot11ClientMacAddress_Type = MacAddress
_BelairDot11ClientMacAddress_Object = MibTableColumn
belairDot11ClientMacAddress = _BelairDot11ClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 1),
    _BelairDot11ClientMacAddress_Type()
)
belairDot11ClientMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairDot11ClientMacAddress.setStatus("current")
_BelairDot11ClientRssi_Type = Integer32
_BelairDot11ClientRssi_Object = MibTableColumn
belairDot11ClientRssi = _BelairDot11ClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 2),
    _BelairDot11ClientRssi_Type()
)
belairDot11ClientRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRssi.setStatus("current")
_BelairDot11ClientVlan_Type = Integer32
_BelairDot11ClientVlan_Object = MibTableColumn
belairDot11ClientVlan = _BelairDot11ClientVlan_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 3),
    _BelairDot11ClientVlan_Type()
)
belairDot11ClientVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientVlan.setStatus("current")
_BelairDot11ClientConnectedTime_Type = Integer32
_BelairDot11ClientConnectedTime_Object = MibTableColumn
belairDot11ClientConnectedTime = _BelairDot11ClientConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 4),
    _BelairDot11ClientConnectedTime_Type()
)
belairDot11ClientConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientConnectedTime.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11ClientConnectedTime.setUnits("Seconds")
_BelairDot11ClientSecsSinceLastFrame_Type = Integer32
_BelairDot11ClientSecsSinceLastFrame_Object = MibTableColumn
belairDot11ClientSecsSinceLastFrame = _BelairDot11ClientSecsSinceLastFrame_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 5),
    _BelairDot11ClientSecsSinceLastFrame_Type()
)
belairDot11ClientSecsSinceLastFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientSecsSinceLastFrame.setStatus("current")
if mibBuilder.loadTexts:
    belairDot11ClientSecsSinceLastFrame.setUnits("Seconds")


class _BelairDot11ClientIdentity_Type(OctetString):
    """Custom type belairDot11ClientIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BelairDot11ClientIdentity_Type.__name__ = "OctetString"
_BelairDot11ClientIdentity_Object = MibTableColumn
belairDot11ClientIdentity = _BelairDot11ClientIdentity_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 6),
    _BelairDot11ClientIdentity_Type()
)
belairDot11ClientIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientIdentity.setStatus("current")


class _BelairDot11ClientAuthenState_Type(Integer32):
    """Custom type belairDot11ClientAuthenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unauthenticated", 0),
          ("authenticated", 1),
          ("eapAuthenticated", 2),
          ("wepError", 3),
          ("pskError", 4),
          ("radiusTimeout", 5),
          ("clientTimeout", 6))
    )


_BelairDot11ClientAuthenState_Type.__name__ = "Integer32"
_BelairDot11ClientAuthenState_Object = MibTableColumn
belairDot11ClientAuthenState = _BelairDot11ClientAuthenState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 7),
    _BelairDot11ClientAuthenState_Type()
)
belairDot11ClientAuthenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientAuthenState.setStatus("current")
_BelairDot11ClientIpAddress_Type = IpAddress
_BelairDot11ClientIpAddress_Object = MibTableColumn
belairDot11ClientIpAddress = _BelairDot11ClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 8),
    _BelairDot11ClientIpAddress_Type()
)
belairDot11ClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientIpAddress.setStatus("current")


class _BelairDot11ClientDhcpState_Type(Integer32):
    """Custom type belairDot11ClientDhcpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("discover", 1),
          ("offer", 2),
          ("request", 3),
          ("decline", 4),
          ("ack", 5),
          ("nack", 6),
          ("release", 7),
          ("inform", 8),
          ("arpResolve", 9),
          ("static", 10))
    )


_BelairDot11ClientDhcpState_Type.__name__ = "Integer32"
_BelairDot11ClientDhcpState_Object = MibTableColumn
belairDot11ClientDhcpState = _BelairDot11ClientDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 9),
    _BelairDot11ClientDhcpState_Type()
)
belairDot11ClientDhcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientDhcpState.setStatus("current")
_BelairDot11ClientRxBytesPerSec_Type = Unsigned32
_BelairDot11ClientRxBytesPerSec_Object = MibTableColumn
belairDot11ClientRxBytesPerSec = _BelairDot11ClientRxBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 10),
    _BelairDot11ClientRxBytesPerSec_Type()
)
belairDot11ClientRxBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRxBytesPerSec.setStatus("current")
_BelairDot11ClientRxPktsPerSec_Type = Unsigned32
_BelairDot11ClientRxPktsPerSec_Object = MibTableColumn
belairDot11ClientRxPktsPerSec = _BelairDot11ClientRxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 11),
    _BelairDot11ClientRxPktsPerSec_Type()
)
belairDot11ClientRxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRxPktsPerSec.setStatus("current")
_BelairDot11ClientTxBytesPerSec_Type = Unsigned32
_BelairDot11ClientTxBytesPerSec_Object = MibTableColumn
belairDot11ClientTxBytesPerSec = _BelairDot11ClientTxBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 12),
    _BelairDot11ClientTxBytesPerSec_Type()
)
belairDot11ClientTxBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientTxBytesPerSec.setStatus("current")
_BelairDot11ClientTxPktsPerSec_Type = Unsigned32
_BelairDot11ClientTxPktsPerSec_Object = MibTableColumn
belairDot11ClientTxPktsPerSec = _BelairDot11ClientTxPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 13),
    _BelairDot11ClientTxPktsPerSec_Type()
)
belairDot11ClientTxPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientTxPktsPerSec.setStatus("current")
_BelairDot11ClientRxBytes_Type = Counter32
_BelairDot11ClientRxBytes_Object = MibTableColumn
belairDot11ClientRxBytes = _BelairDot11ClientRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 14),
    _BelairDot11ClientRxBytes_Type()
)
belairDot11ClientRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRxBytes.setStatus("current")
_BelairDot11ClientTxBytes_Type = Counter32
_BelairDot11ClientTxBytes_Object = MibTableColumn
belairDot11ClientTxBytes = _BelairDot11ClientTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 15),
    _BelairDot11ClientTxBytes_Type()
)
belairDot11ClientTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientTxBytes.setStatus("current")
_BelairDot11ClientRxPkts_Type = Counter32
_BelairDot11ClientRxPkts_Object = MibTableColumn
belairDot11ClientRxPkts = _BelairDot11ClientRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 16),
    _BelairDot11ClientRxPkts_Type()
)
belairDot11ClientRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRxPkts.setStatus("current")
_BelairDot11ClientTxPkts_Type = Counter32
_BelairDot11ClientTxPkts_Object = MibTableColumn
belairDot11ClientTxPkts = _BelairDot11ClientTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 17),
    _BelairDot11ClientTxPkts_Type()
)
belairDot11ClientTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientTxPkts.setStatus("current")
_BelairDot11ClientAgedOut_Type = TruthValue
_BelairDot11ClientAgedOut_Object = MibTableColumn
belairDot11ClientAgedOut = _BelairDot11ClientAgedOut_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 1, 1, 18),
    _BelairDot11ClientAgedOut_Type()
)
belairDot11ClientAgedOut.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    belairDot11ClientAgedOut.setStatus("current")
_BelairDot11ClientRecordTable_Object = MibTable
belairDot11ClientRecordTable = _BelairDot11ClientRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 2)
)
if mibBuilder.loadTexts:
    belairDot11ClientRecordTable.setStatus("current")
_BelairDot11ClientRecordEntry_Object = MibTableRow
belairDot11ClientRecordEntry = _BelairDot11ClientRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 2, 1)
)
belairDot11ClientRecordEntry.setIndexNames(
    (0, "BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRecordIndex"),
)
if mibBuilder.loadTexts:
    belairDot11ClientRecordEntry.setStatus("current")


class _BelairDot11ClientRecordIndex_Type(Unsigned32):
    """Custom type belairDot11ClientRecordIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BelairDot11ClientRecordIndex_Type.__name__ = "Unsigned32"
_BelairDot11ClientRecordIndex_Object = MibTableColumn
belairDot11ClientRecordIndex = _BelairDot11ClientRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 2, 1, 1),
    _BelairDot11ClientRecordIndex_Type()
)
belairDot11ClientRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    belairDot11ClientRecordIndex.setStatus("current")


class _BelairDot11ClientRecordInfo_Type(OctetString):
    """Custom type belairDot11ClientRecordInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_BelairDot11ClientRecordInfo_Type.__name__ = "OctetString"
_BelairDot11ClientRecordInfo_Object = MibTableColumn
belairDot11ClientRecordInfo = _BelairDot11ClientRecordInfo_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 2, 1, 2),
    _BelairDot11ClientRecordInfo_Type()
)
belairDot11ClientRecordInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRecordInfo.setStatus("current")


class _BelairDot11ClientRecordLastIndex_Type(Unsigned32):
    """Custom type belairDot11ClientRecordLastIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BelairDot11ClientRecordLastIndex_Type.__name__ = "Unsigned32"
_BelairDot11ClientRecordLastIndex_Object = MibScalar
belairDot11ClientRecordLastIndex = _BelairDot11ClientRecordLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 1, 3),
    _BelairDot11ClientRecordLastIndex_Type()
)
belairDot11ClientRecordLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    belairDot11ClientRecordLastIndex.setStatus("current")
_BelairDot11ClientTraps_ObjectIdentity = ObjectIdentity
belairDot11ClientTraps = _BelairDot11ClientTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 2)
)
_BelairDot11ClientTrapsV2_ObjectIdentity = ObjectIdentity
belairDot11ClientTrapsV2 = _BelairDot11ClientTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 2, 0)
)
_BelairDot11ClientConformance_ObjectIdentity = ObjectIdentity
belairDot11ClientConformance = _BelairDot11ClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 3)
)

# Managed Objects groups

belairDot11ClientObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 3, 1)
)
belairDot11ClientObjGroup.setObjects(
      *(("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRssi"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientVlan"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientSecsSinceLastFrame"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientAuthenState"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientIpAddress"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRecordLastIndex"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRecordInfo"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientTxBytes"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRxBytes"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientTxPktsPerSec"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientTxBytesPerSec"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRxPktsPerSec"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRxBytesPerSec"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientAgedOut"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientTxPkts"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRxPkts"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientDhcpState"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientConnectedTime"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientIdentity"))
)
if mibBuilder.loadTexts:
    belairDot11ClientObjGroup.setStatus("current")


# Notification objects

belairDot11ClientAuthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 2, 0, 1)
)
belairDot11ClientAuthenticated.setObjects(
      *(("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRssi"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientVlan"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientIdentity"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientAuthenState"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientIpAddress"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientDhcpState"))
)
if mibBuilder.loadTexts:
    belairDot11ClientAuthenticated.setStatus(
        "current"
    )

belairDot11ClientDeauthenticated = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 2, 0, 2)
)
belairDot11ClientDeauthenticated.setObjects(
      *(("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientConnectedTime"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRxBytes"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientTxBytes"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientRxPkts"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientTxPkts"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientAgedOut"))
)
if mibBuilder.loadTexts:
    belairDot11ClientDeauthenticated.setStatus(
        "current"
    )


# Notifications groups

belairDot11ClientTrapObjGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 4, 7, 3, 2)
)
belairDot11ClientTrapObjGroup.setObjects(
      *(("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientAuthenticated"),
        ("BELAIR-IEEE802DOT11-CLIENT", "belairDot11ClientDeauthenticated"))
)
if mibBuilder.loadTexts:
    belairDot11ClientTrapObjGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-IEEE802DOT11-CLIENT",
    **{"belairIeeeDot11ClientMib": belairIeeeDot11ClientMib,
       "belairDot11ClientObjects": belairDot11ClientObjects,
       "belairDot11ClientTable": belairDot11ClientTable,
       "belairDot11ClientEntry": belairDot11ClientEntry,
       "belairDot11ClientMacAddress": belairDot11ClientMacAddress,
       "belairDot11ClientRssi": belairDot11ClientRssi,
       "belairDot11ClientVlan": belairDot11ClientVlan,
       "belairDot11ClientConnectedTime": belairDot11ClientConnectedTime,
       "belairDot11ClientSecsSinceLastFrame": belairDot11ClientSecsSinceLastFrame,
       "belairDot11ClientIdentity": belairDot11ClientIdentity,
       "belairDot11ClientAuthenState": belairDot11ClientAuthenState,
       "belairDot11ClientIpAddress": belairDot11ClientIpAddress,
       "belairDot11ClientDhcpState": belairDot11ClientDhcpState,
       "belairDot11ClientRxBytesPerSec": belairDot11ClientRxBytesPerSec,
       "belairDot11ClientRxPktsPerSec": belairDot11ClientRxPktsPerSec,
       "belairDot11ClientTxBytesPerSec": belairDot11ClientTxBytesPerSec,
       "belairDot11ClientTxPktsPerSec": belairDot11ClientTxPktsPerSec,
       "belairDot11ClientRxBytes": belairDot11ClientRxBytes,
       "belairDot11ClientTxBytes": belairDot11ClientTxBytes,
       "belairDot11ClientRxPkts": belairDot11ClientRxPkts,
       "belairDot11ClientTxPkts": belairDot11ClientTxPkts,
       "belairDot11ClientAgedOut": belairDot11ClientAgedOut,
       "belairDot11ClientRecordTable": belairDot11ClientRecordTable,
       "belairDot11ClientRecordEntry": belairDot11ClientRecordEntry,
       "belairDot11ClientRecordIndex": belairDot11ClientRecordIndex,
       "belairDot11ClientRecordInfo": belairDot11ClientRecordInfo,
       "belairDot11ClientRecordLastIndex": belairDot11ClientRecordLastIndex,
       "belairDot11ClientTraps": belairDot11ClientTraps,
       "belairDot11ClientTrapsV2": belairDot11ClientTrapsV2,
       "belairDot11ClientAuthenticated": belairDot11ClientAuthenticated,
       "belairDot11ClientDeauthenticated": belairDot11ClientDeauthenticated,
       "belairDot11ClientConformance": belairDot11ClientConformance,
       "belairDot11ClientObjGroup": belairDot11ClientObjGroup,
       "belairDot11ClientTrapObjGroup": belairDot11ClientTrapObjGroup}
)
