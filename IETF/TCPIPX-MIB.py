# SNMP MIB module (TCPIPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/TCPIPX-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:21:51 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



class IpxAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixedLength = 10



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Tcpx_ObjectIdentity = ObjectIdentity
tcpx = _Tcpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 29)
)
_TcpxTcp_ObjectIdentity = ObjectIdentity
tcpxTcp = _TcpxTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1)
)
_TcpIpxConnTable_Object = MibTable
tcpIpxConnTable = _TcpIpxConnTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1)
)
if mibBuilder.loadTexts:
    tcpIpxConnTable.setStatus("mandatory")
_TcpIpxConnEntry_Object = MibTableRow
tcpIpxConnEntry = _TcpIpxConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1)
)
tcpIpxConnEntry.setIndexNames(
    (0, "TCPIPX-MIB", "tcpIpxConnLocalAddress"),
    (0, "TCPIPX-MIB", "tcpIpxConnLocalPort"),
    (0, "TCPIPX-MIB", "tcpIpxConnRemAddress"),
    (0, "TCPIPX-MIB", "tcpIpxConnRemPort"),
)
if mibBuilder.loadTexts:
    tcpIpxConnEntry.setStatus("mandatory")


class _TcpIpxConnState_Type(Integer32):
    """Custom type tcpIpxConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("listen", 2),
          ("synSent", 3),
          ("synReceived", 4),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("closeWait", 8),
          ("lastAck", 9),
          ("closing", 10),
          ("timeWait", 11),
          ("deleteTCB", 12))
    )


_TcpIpxConnState_Type.__name__ = "Integer32"
_TcpIpxConnState_Object = MibTableColumn
tcpIpxConnState = _TcpIpxConnState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 1),
    _TcpIpxConnState_Type()
)
tcpIpxConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpIpxConnState.setStatus("mandatory")
_TcpIpxConnLocalAddress_Type = IpxAddress
_TcpIpxConnLocalAddress_Object = MibTableColumn
tcpIpxConnLocalAddress = _TcpIpxConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 2),
    _TcpIpxConnLocalAddress_Type()
)
tcpIpxConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIpxConnLocalAddress.setStatus("mandatory")


class _TcpIpxConnLocalPort_Type(Integer32):
    """Custom type tcpIpxConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpIpxConnLocalPort_Type.__name__ = "Integer32"
_TcpIpxConnLocalPort_Object = MibTableColumn
tcpIpxConnLocalPort = _TcpIpxConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 3),
    _TcpIpxConnLocalPort_Type()
)
tcpIpxConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIpxConnLocalPort.setStatus("mandatory")
_TcpIpxConnRemAddress_Type = IpxAddress
_TcpIpxConnRemAddress_Object = MibTableColumn
tcpIpxConnRemAddress = _TcpIpxConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 4),
    _TcpIpxConnRemAddress_Type()
)
tcpIpxConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIpxConnRemAddress.setStatus("mandatory")


class _TcpIpxConnRemPort_Type(Integer32):
    """Custom type tcpIpxConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpIpxConnRemPort_Type.__name__ = "Integer32"
_TcpIpxConnRemPort_Object = MibTableColumn
tcpIpxConnRemPort = _TcpIpxConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 5),
    _TcpIpxConnRemPort_Type()
)
tcpIpxConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpIpxConnRemPort.setStatus("mandatory")
_TcpUnspecConnTable_Object = MibTable
tcpUnspecConnTable = _TcpUnspecConnTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    tcpUnspecConnTable.setStatus("mandatory")
_TcpUnspecConnEntry_Object = MibTableRow
tcpUnspecConnEntry = _TcpUnspecConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1)
)
tcpUnspecConnEntry.setIndexNames(
    (0, "TCPIPX-MIB", "tcpUnspecConnLocalPort"),
)
if mibBuilder.loadTexts:
    tcpUnspecConnEntry.setStatus("mandatory")


class _TcpUnspecConnState_Type(Integer32):
    """Custom type tcpUnspecConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("listen", 2),
          ("deleteTCB", 12))
    )


_TcpUnspecConnState_Type.__name__ = "Integer32"
_TcpUnspecConnState_Object = MibTableColumn
tcpUnspecConnState = _TcpUnspecConnState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 1),
    _TcpUnspecConnState_Type()
)
tcpUnspecConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpUnspecConnState.setStatus("mandatory")


class _TcpUnspecConnLocalPort_Type(Integer32):
    """Custom type tcpUnspecConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpUnspecConnLocalPort_Type.__name__ = "Integer32"
_TcpUnspecConnLocalPort_Object = MibTableColumn
tcpUnspecConnLocalPort = _TcpUnspecConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 2),
    _TcpUnspecConnLocalPort_Type()
)
tcpUnspecConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpUnspecConnLocalPort.setStatus("mandatory")
_TcpxUdp_ObjectIdentity = ObjectIdentity
tcpxUdp = _TcpxUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2)
)
_UdpIpxTable_Object = MibTable
udpIpxTable = _UdpIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1)
)
if mibBuilder.loadTexts:
    udpIpxTable.setStatus("mandatory")
_UdpIpxEntry_Object = MibTableRow
udpIpxEntry = _UdpIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1)
)
udpIpxEntry.setIndexNames(
    (0, "TCPIPX-MIB", "udpIpxLocalAddress"),
    (0, "TCPIPX-MIB", "udpIpxLocalPort"),
)
if mibBuilder.loadTexts:
    udpIpxEntry.setStatus("mandatory")
_UdpIpxLocalAddress_Type = IpxAddress
_UdpIpxLocalAddress_Object = MibTableColumn
udpIpxLocalAddress = _UdpIpxLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 1),
    _UdpIpxLocalAddress_Type()
)
udpIpxLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpIpxLocalAddress.setStatus("mandatory")


class _UdpIpxLocalPort_Type(Integer32):
    """Custom type udpIpxLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UdpIpxLocalPort_Type.__name__ = "Integer32"
_UdpIpxLocalPort_Object = MibTableColumn
udpIpxLocalPort = _UdpIpxLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 2),
    _UdpIpxLocalPort_Type()
)
udpIpxLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpIpxLocalPort.setStatus("mandatory")
_UdpUnspecTable_Object = MibTable
udpUnspecTable = _UdpUnspecTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2)
)
if mibBuilder.loadTexts:
    udpUnspecTable.setStatus("mandatory")
_UdpUnspecEntry_Object = MibTableRow
udpUnspecEntry = _UdpUnspecEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1)
)
udpUnspecEntry.setIndexNames(
    (0, "TCPIPX-MIB", "udpUnspecLocalPort"),
)
if mibBuilder.loadTexts:
    udpUnspecEntry.setStatus("mandatory")


class _UdpUnspecLocalPort_Type(Integer32):
    """Custom type udpUnspecLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UdpUnspecLocalPort_Type.__name__ = "Integer32"
_UdpUnspecLocalPort_Object = MibTableColumn
udpUnspecLocalPort = _UdpUnspecLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1, 1),
    _UdpUnspecLocalPort_Type()
)
udpUnspecLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpUnspecLocalPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TCPIPX-MIB",
    **{"IpxAddress": IpxAddress,
       "novell": novell,
       "mibDoc": mibDoc,
       "tcpx": tcpx,
       "tcpxTcp": tcpxTcp,
       "tcpIpxConnTable": tcpIpxConnTable,
       "tcpIpxConnEntry": tcpIpxConnEntry,
       "tcpIpxConnState": tcpIpxConnState,
       "tcpIpxConnLocalAddress": tcpIpxConnLocalAddress,
       "tcpIpxConnLocalPort": tcpIpxConnLocalPort,
       "tcpIpxConnRemAddress": tcpIpxConnRemAddress,
       "tcpIpxConnRemPort": tcpIpxConnRemPort,
       "tcpUnspecConnTable": tcpUnspecConnTable,
       "tcpUnspecConnEntry": tcpUnspecConnEntry,
       "tcpUnspecConnState": tcpUnspecConnState,
       "tcpUnspecConnLocalPort": tcpUnspecConnLocalPort,
       "tcpxUdp": tcpxUdp,
       "udpIpxTable": udpIpxTable,
       "udpIpxEntry": udpIpxEntry,
       "udpIpxLocalAddress": udpIpxLocalAddress,
       "udpIpxLocalPort": udpIpxLocalPort,
       "udpUnspecTable": udpUnspecTable,
       "udpUnspecEntry": udpUnspecEntry,
       "udpUnspecLocalPort": udpUnspecLocalPort}
)
