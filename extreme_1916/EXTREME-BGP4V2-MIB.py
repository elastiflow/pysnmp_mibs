# SNMP MIB module (EXTREME-BGP4V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-BGP4V2-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:22:20 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(ExtremeBgp4V2AddressFamilyIdentifierTC,
 ExtremeBgp4V2IdentifierTC,
 ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC) = mibBuilder.importSymbols(
    "EXTREME-BGP4V2-TC-MIB",
    "ExtremeBgp4V2AddressFamilyIdentifierTC",
    "ExtremeBgp4V2IdentifierTC",
    "ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

extremeBgp4V2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51)
)
if mibBuilder.loadTexts:
    extremeBgp4V2.setRevisions(
        ("2018-11-02 00:00",
         "2014-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeBgp4V2Notifications_ObjectIdentity = ObjectIdentity
extremeBgp4V2Notifications = _ExtremeBgp4V2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 0)
)
_ExtremeBgp4V2Objects_ObjectIdentity = ObjectIdentity
extremeBgp4V2Objects = _ExtremeBgp4V2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1)
)
_ExtremeBgp4V2DiscontinuityTable_Object = MibTable
extremeBgp4V2DiscontinuityTable = _ExtremeBgp4V2DiscontinuityTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 1)
)
if mibBuilder.loadTexts:
    extremeBgp4V2DiscontinuityTable.setStatus("current")
_ExtremeBgp4V2DiscontinuityEntry_Object = MibTableRow
extremeBgp4V2DiscontinuityEntry = _ExtremeBgp4V2DiscontinuityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 1, 1)
)
extremeBgp4V2DiscontinuityEntry.setIndexNames(
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInstance"),
)
if mibBuilder.loadTexts:
    extremeBgp4V2DiscontinuityEntry.setStatus("current")
_ExtremeBgp4V2DiscontinuityTime_Type = TimeStamp
_ExtremeBgp4V2DiscontinuityTime_Object = MibTableColumn
extremeBgp4V2DiscontinuityTime = _ExtremeBgp4V2DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 1, 1, 1),
    _ExtremeBgp4V2DiscontinuityTime_Type()
)
extremeBgp4V2DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2DiscontinuityTime.setStatus("current")
_ExtremeBgp4V2PeerTable_Object = MibTable
extremeBgp4V2PeerTable = _ExtremeBgp4V2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerTable.setStatus("current")
_ExtremeBgp4V2PeerEntry_Object = MibTableRow
extremeBgp4V2PeerEntry = _ExtremeBgp4V2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1)
)
extremeBgp4V2PeerEntry.setIndexNames(
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInstance"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddrType"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerEntry.setStatus("current")


class _ExtremeBgp4V2PeerInstance_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExtremeBgp4V2PeerInstance_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerInstance_Object = MibTableColumn
extremeBgp4V2PeerInstance = _ExtremeBgp4V2PeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 1),
    _ExtremeBgp4V2PeerInstance_Type()
)
extremeBgp4V2PeerInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerInstance.setStatus("current")
_ExtremeBgp4V2PeerLocalAddrType_Type = InetAddressType
_ExtremeBgp4V2PeerLocalAddrType_Object = MibTableColumn
extremeBgp4V2PeerLocalAddrType = _ExtremeBgp4V2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 2),
    _ExtremeBgp4V2PeerLocalAddrType_Type()
)
extremeBgp4V2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLocalAddrType.setStatus("current")
_ExtremeBgp4V2PeerLocalAddr_Type = InetAddress
_ExtremeBgp4V2PeerLocalAddr_Object = MibTableColumn
extremeBgp4V2PeerLocalAddr = _ExtremeBgp4V2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 3),
    _ExtremeBgp4V2PeerLocalAddr_Type()
)
extremeBgp4V2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLocalAddr.setStatus("current")
_ExtremeBgp4V2PeerRemoteAddrType_Type = InetAddressType
_ExtremeBgp4V2PeerRemoteAddrType_Object = MibTableColumn
extremeBgp4V2PeerRemoteAddrType = _ExtremeBgp4V2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 4),
    _ExtremeBgp4V2PeerRemoteAddrType_Type()
)
extremeBgp4V2PeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerRemoteAddrType.setStatus("current")
_ExtremeBgp4V2PeerRemoteAddr_Type = InetAddress
_ExtremeBgp4V2PeerRemoteAddr_Object = MibTableColumn
extremeBgp4V2PeerRemoteAddr = _ExtremeBgp4V2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 5),
    _ExtremeBgp4V2PeerRemoteAddr_Type()
)
extremeBgp4V2PeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerRemoteAddr.setStatus("current")
_ExtremeBgp4V2PeerLocalPort_Type = InetPortNumber
_ExtremeBgp4V2PeerLocalPort_Object = MibTableColumn
extremeBgp4V2PeerLocalPort = _ExtremeBgp4V2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 6),
    _ExtremeBgp4V2PeerLocalPort_Type()
)
extremeBgp4V2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLocalPort.setStatus("current")
_ExtremeBgp4V2PeerLocalAs_Type = InetAutonomousSystemNumber
_ExtremeBgp4V2PeerLocalAs_Object = MibTableColumn
extremeBgp4V2PeerLocalAs = _ExtremeBgp4V2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 7),
    _ExtremeBgp4V2PeerLocalAs_Type()
)
extremeBgp4V2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLocalAs.setStatus("current")
_ExtremeBgp4V2PeerLocalIdentifier_Type = ExtremeBgp4V2IdentifierTC
_ExtremeBgp4V2PeerLocalIdentifier_Object = MibTableColumn
extremeBgp4V2PeerLocalIdentifier = _ExtremeBgp4V2PeerLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 8),
    _ExtremeBgp4V2PeerLocalIdentifier_Type()
)
extremeBgp4V2PeerLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLocalIdentifier.setStatus("current")
_ExtremeBgp4V2PeerRemotePort_Type = InetPortNumber
_ExtremeBgp4V2PeerRemotePort_Object = MibTableColumn
extremeBgp4V2PeerRemotePort = _ExtremeBgp4V2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 9),
    _ExtremeBgp4V2PeerRemotePort_Type()
)
extremeBgp4V2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerRemotePort.setStatus("current")
_ExtremeBgp4V2PeerRemoteAs_Type = InetAutonomousSystemNumber
_ExtremeBgp4V2PeerRemoteAs_Object = MibTableColumn
extremeBgp4V2PeerRemoteAs = _ExtremeBgp4V2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 10),
    _ExtremeBgp4V2PeerRemoteAs_Type()
)
extremeBgp4V2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerRemoteAs.setStatus("current")
_ExtremeBgp4V2PeerRemoteIdentifier_Type = ExtremeBgp4V2IdentifierTC
_ExtremeBgp4V2PeerRemoteIdentifier_Object = MibTableColumn
extremeBgp4V2PeerRemoteIdentifier = _ExtremeBgp4V2PeerRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 11),
    _ExtremeBgp4V2PeerRemoteIdentifier_Type()
)
extremeBgp4V2PeerRemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerRemoteIdentifier.setStatus("current")


class _ExtremeBgp4V2PeerAdminStatus_Type(Integer32):
    """Custom type extremeBgp4V2PeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halted", 1),
          ("running", 2))
    )


_ExtremeBgp4V2PeerAdminStatus_Type.__name__ = "Integer32"
_ExtremeBgp4V2PeerAdminStatus_Object = MibTableColumn
extremeBgp4V2PeerAdminStatus = _ExtremeBgp4V2PeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 12),
    _ExtremeBgp4V2PeerAdminStatus_Type()
)
extremeBgp4V2PeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerAdminStatus.setStatus("current")


class _ExtremeBgp4V2PeerState_Type(Integer32):
    """Custom type extremeBgp4V2PeerState based on Integer32"""
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_ExtremeBgp4V2PeerState_Type.__name__ = "Integer32"
_ExtremeBgp4V2PeerState_Object = MibTableColumn
extremeBgp4V2PeerState = _ExtremeBgp4V2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 13),
    _ExtremeBgp4V2PeerState_Type()
)
extremeBgp4V2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerState.setStatus("current")
_ExtremeBgp4V2PeerDescription_Type = SnmpAdminString
_ExtremeBgp4V2PeerDescription_Object = MibTableColumn
extremeBgp4V2PeerDescription = _ExtremeBgp4V2PeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 2, 1, 14),
    _ExtremeBgp4V2PeerDescription_Type()
)
extremeBgp4V2PeerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerDescription.setStatus("current")
_ExtremeBgp4V2PeerErrorsTable_Object = MibTable
extremeBgp4V2PeerErrorsTable = _ExtremeBgp4V2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerErrorsTable.setStatus("current")
_ExtremeBgp4V2PeerErrorsEntry_Object = MibTableRow
extremeBgp4V2PeerErrorsEntry = _ExtremeBgp4V2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerErrorsEntry.setStatus("current")


class _ExtremeBgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerLastErrorCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeBgp4V2PeerLastErrorCodeReceived_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerLastErrorCodeReceived_Object = MibTableColumn
extremeBgp4V2PeerLastErrorCodeReceived = _ExtremeBgp4V2PeerLastErrorCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 1),
    _ExtremeBgp4V2PeerLastErrorCodeReceived_Type()
)
extremeBgp4V2PeerLastErrorCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorCodeReceived.setStatus("current")


class _ExtremeBgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerLastErrorSubCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeBgp4V2PeerLastErrorSubCodeReceived_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerLastErrorSubCodeReceived_Object = MibTableColumn
extremeBgp4V2PeerLastErrorSubCodeReceived = _ExtremeBgp4V2PeerLastErrorSubCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 2),
    _ExtremeBgp4V2PeerLastErrorSubCodeReceived_Type()
)
extremeBgp4V2PeerLastErrorSubCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorSubCodeReceived.setStatus("current")
_ExtremeBgp4V2PeerLastErrorReceivedTime_Type = TimeStamp
_ExtremeBgp4V2PeerLastErrorReceivedTime_Object = MibTableColumn
extremeBgp4V2PeerLastErrorReceivedTime = _ExtremeBgp4V2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 3),
    _ExtremeBgp4V2PeerLastErrorReceivedTime_Type()
)
extremeBgp4V2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorReceivedTime.setStatus("current")
_ExtremeBgp4V2PeerLastErrorReceivedText_Type = SnmpAdminString
_ExtremeBgp4V2PeerLastErrorReceivedText_Object = MibTableColumn
extremeBgp4V2PeerLastErrorReceivedText = _ExtremeBgp4V2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 4),
    _ExtremeBgp4V2PeerLastErrorReceivedText_Type()
)
extremeBgp4V2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorReceivedText.setStatus("current")


class _ExtremeBgp4V2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type extremeBgp4V2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_ExtremeBgp4V2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_ExtremeBgp4V2PeerLastErrorReceivedData_Object = MibTableColumn
extremeBgp4V2PeerLastErrorReceivedData = _ExtremeBgp4V2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 5),
    _ExtremeBgp4V2PeerLastErrorReceivedData_Type()
)
extremeBgp4V2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorReceivedData.setStatus("current")


class _ExtremeBgp4V2PeerLastErrorCodeSent_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerLastErrorCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeBgp4V2PeerLastErrorCodeSent_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerLastErrorCodeSent_Object = MibTableColumn
extremeBgp4V2PeerLastErrorCodeSent = _ExtremeBgp4V2PeerLastErrorCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 6),
    _ExtremeBgp4V2PeerLastErrorCodeSent_Type()
)
extremeBgp4V2PeerLastErrorCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorCodeSent.setStatus("current")


class _ExtremeBgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerLastErrorSubCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtremeBgp4V2PeerLastErrorSubCodeSent_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerLastErrorSubCodeSent_Object = MibTableColumn
extremeBgp4V2PeerLastErrorSubCodeSent = _ExtremeBgp4V2PeerLastErrorSubCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 7),
    _ExtremeBgp4V2PeerLastErrorSubCodeSent_Type()
)
extremeBgp4V2PeerLastErrorSubCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorSubCodeSent.setStatus("current")
_ExtremeBgp4V2PeerLastErrorSentTime_Type = TimeStamp
_ExtremeBgp4V2PeerLastErrorSentTime_Object = MibTableColumn
extremeBgp4V2PeerLastErrorSentTime = _ExtremeBgp4V2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 8),
    _ExtremeBgp4V2PeerLastErrorSentTime_Type()
)
extremeBgp4V2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorSentTime.setStatus("current")
_ExtremeBgp4V2PeerLastErrorSentText_Type = SnmpAdminString
_ExtremeBgp4V2PeerLastErrorSentText_Object = MibTableColumn
extremeBgp4V2PeerLastErrorSentText = _ExtremeBgp4V2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 9),
    _ExtremeBgp4V2PeerLastErrorSentText_Type()
)
extremeBgp4V2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorSentText.setStatus("current")


class _ExtremeBgp4V2PeerLastErrorSentData_Type(OctetString):
    """Custom type extremeBgp4V2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_ExtremeBgp4V2PeerLastErrorSentData_Type.__name__ = "OctetString"
_ExtremeBgp4V2PeerLastErrorSentData_Object = MibTableColumn
extremeBgp4V2PeerLastErrorSentData = _ExtremeBgp4V2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 3, 1, 10),
    _ExtremeBgp4V2PeerLastErrorSentData_Type()
)
extremeBgp4V2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerLastErrorSentData.setStatus("current")
_ExtremeBgp4V2PeerEventTimesTable_Object = MibTable
extremeBgp4V2PeerEventTimesTable = _ExtremeBgp4V2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 4)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerEventTimesTable.setStatus("current")
_ExtremeBgp4V2PeerEventTimesEntry_Object = MibTableRow
extremeBgp4V2PeerEventTimesEntry = _ExtremeBgp4V2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 4, 1)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerEventTimesEntry.setStatus("current")
_ExtremeBgp4V2PeerFsmEstablishedTime_Type = Gauge32
_ExtremeBgp4V2PeerFsmEstablishedTime_Object = MibTableColumn
extremeBgp4V2PeerFsmEstablishedTime = _ExtremeBgp4V2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 4, 1, 1),
    _ExtremeBgp4V2PeerFsmEstablishedTime_Type()
)
extremeBgp4V2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerFsmEstablishedTime.setUnits("seconds")
_ExtremeBgp4V2PeerInUpdatesElapsedTime_Type = Gauge32
_ExtremeBgp4V2PeerInUpdatesElapsedTime_Object = MibTableColumn
extremeBgp4V2PeerInUpdatesElapsedTime = _ExtremeBgp4V2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 4, 1, 2),
    _ExtremeBgp4V2PeerInUpdatesElapsedTime_Type()
)
extremeBgp4V2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerInUpdatesElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerInUpdatesElapsedTime.setUnits("seconds")
_ExtremeBgp4V2PeerConfiguredTimersTable_Object = MibTable
extremeBgp4V2PeerConfiguredTimersTable = _ExtremeBgp4V2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerConfiguredTimersTable.setStatus("current")
_ExtremeBgp4V2PeerConfiguredTimersEntry_Object = MibTableRow
extremeBgp4V2PeerConfiguredTimersEntry = _ExtremeBgp4V2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5, 1)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerConfiguredTimersEntry.setStatus("current")


class _ExtremeBgp4V2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeBgp4V2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerConnectRetryInterval_Object = MibTableColumn
extremeBgp4V2PeerConnectRetryInterval = _ExtremeBgp4V2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5, 1, 1),
    _ExtremeBgp4V2PeerConnectRetryInterval_Type()
)
extremeBgp4V2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerConnectRetryInterval.setUnits("seconds")


class _ExtremeBgp4V2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_ExtremeBgp4V2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerHoldTimeConfigured_Object = MibTableColumn
extremeBgp4V2PeerHoldTimeConfigured = _ExtremeBgp4V2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5, 1, 2),
    _ExtremeBgp4V2PeerHoldTimeConfigured_Type()
)
extremeBgp4V2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerHoldTimeConfigured.setUnits("seconds")


class _ExtremeBgp4V2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_ExtremeBgp4V2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerKeepAliveConfigured_Object = MibTableColumn
extremeBgp4V2PeerKeepAliveConfigured = _ExtremeBgp4V2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5, 1, 3),
    _ExtremeBgp4V2PeerKeepAliveConfigured_Type()
)
extremeBgp4V2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerKeepAliveConfigured.setUnits("seconds")


class _ExtremeBgp4V2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeBgp4V2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerMinASOrigInterval_Object = MibTableColumn
extremeBgp4V2PeerMinASOrigInterval = _ExtremeBgp4V2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5, 1, 4),
    _ExtremeBgp4V2PeerMinASOrigInterval_Type()
)
extremeBgp4V2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerMinASOrigInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerMinASOrigInterval.setUnits("seconds")


class _ExtremeBgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeBgp4V2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerMinRouteAdverInterval_Object = MibTableColumn
extremeBgp4V2PeerMinRouteAdverInterval = _ExtremeBgp4V2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 5, 1, 5),
    _ExtremeBgp4V2PeerMinRouteAdverInterval_Type()
)
extremeBgp4V2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerMinRouteAdverInterval.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerMinRouteAdverInterval.setUnits("seconds")
_ExtremeBgp4V2PeerNegotiatedTimersTable_Object = MibTable
extremeBgp4V2PeerNegotiatedTimersTable = _ExtremeBgp4V2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 6)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerNegotiatedTimersTable.setStatus("current")
_ExtremeBgp4V2PeerNegotiatedTimersEntry_Object = MibTableRow
extremeBgp4V2PeerNegotiatedTimersEntry = _ExtremeBgp4V2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 6, 1)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerNegotiatedTimersEntry.setStatus("current")


class _ExtremeBgp4V2PeerHoldTime_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_ExtremeBgp4V2PeerHoldTime_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerHoldTime_Object = MibTableColumn
extremeBgp4V2PeerHoldTime = _ExtremeBgp4V2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 6, 1, 1),
    _ExtremeBgp4V2PeerHoldTime_Type()
)
extremeBgp4V2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerHoldTime.setUnits("seconds")


class _ExtremeBgp4V2PeerKeepAlive_Type(Unsigned32):
    """Custom type extremeBgp4V2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_ExtremeBgp4V2PeerKeepAlive_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2PeerKeepAlive_Object = MibTableColumn
extremeBgp4V2PeerKeepAlive = _ExtremeBgp4V2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 6, 1, 2),
    _ExtremeBgp4V2PeerKeepAlive_Type()
)
extremeBgp4V2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerKeepAlive.setUnits("seconds")
_ExtremeBgp4V2PeerCountersTable_Object = MibTable
extremeBgp4V2PeerCountersTable = _ExtremeBgp4V2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerCountersTable.setStatus("current")
_ExtremeBgp4V2PeerCountersEntry_Object = MibTableRow
extremeBgp4V2PeerCountersEntry = _ExtremeBgp4V2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7, 1)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PeerCountersEntry.setStatus("current")
_ExtremeBgp4V2PeerInUpdates_Type = Counter32
_ExtremeBgp4V2PeerInUpdates_Object = MibTableColumn
extremeBgp4V2PeerInUpdates = _ExtremeBgp4V2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7, 1, 1),
    _ExtremeBgp4V2PeerInUpdates_Type()
)
extremeBgp4V2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerInUpdates.setStatus("current")
_ExtremeBgp4V2PeerOutUpdates_Type = Counter32
_ExtremeBgp4V2PeerOutUpdates_Object = MibTableColumn
extremeBgp4V2PeerOutUpdates = _ExtremeBgp4V2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7, 1, 2),
    _ExtremeBgp4V2PeerOutUpdates_Type()
)
extremeBgp4V2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerOutUpdates.setStatus("current")
_ExtremeBgp4V2PeerInTotalMessages_Type = Counter32
_ExtremeBgp4V2PeerInTotalMessages_Object = MibTableColumn
extremeBgp4V2PeerInTotalMessages = _ExtremeBgp4V2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7, 1, 3),
    _ExtremeBgp4V2PeerInTotalMessages_Type()
)
extremeBgp4V2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerInTotalMessages.setStatus("current")
_ExtremeBgp4V2PeerOutTotalMessages_Type = Counter32
_ExtremeBgp4V2PeerOutTotalMessages_Object = MibTableColumn
extremeBgp4V2PeerOutTotalMessages = _ExtremeBgp4V2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7, 1, 4),
    _ExtremeBgp4V2PeerOutTotalMessages_Type()
)
extremeBgp4V2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerOutTotalMessages.setStatus("current")
_ExtremeBgp4V2PeerFsmEstablishedTransitions_Type = Counter32
_ExtremeBgp4V2PeerFsmEstablishedTransitions_Object = MibTableColumn
extremeBgp4V2PeerFsmEstablishedTransitions = _ExtremeBgp4V2PeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 7, 1, 5),
    _ExtremeBgp4V2PeerFsmEstablishedTransitions_Type()
)
extremeBgp4V2PeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PeerFsmEstablishedTransitions.setStatus("current")
_ExtremeBgp4V2PrefixGaugesTable_Object = MibTable
extremeBgp4V2PrefixGaugesTable = _ExtremeBgp4V2PrefixGaugesTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8)
)
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixGaugesTable.setStatus("current")
_ExtremeBgp4V2PrefixGaugesEntry_Object = MibTableRow
extremeBgp4V2PrefixGaugesEntry = _ExtremeBgp4V2PrefixGaugesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8, 1)
)
extremeBgp4V2PrefixGaugesEntry.setIndexNames(
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInstance"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddrType"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddr"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PrefixGaugesAfi"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PrefixGaugesSafi"),
)
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixGaugesEntry.setStatus("current")
_ExtremeBgp4V2PrefixGaugesAfi_Type = ExtremeBgp4V2AddressFamilyIdentifierTC
_ExtremeBgp4V2PrefixGaugesAfi_Object = MibTableColumn
extremeBgp4V2PrefixGaugesAfi = _ExtremeBgp4V2PrefixGaugesAfi_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8, 1, 1),
    _ExtremeBgp4V2PrefixGaugesAfi_Type()
)
extremeBgp4V2PrefixGaugesAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixGaugesAfi.setStatus("current")
_ExtremeBgp4V2PrefixGaugesSafi_Type = ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC
_ExtremeBgp4V2PrefixGaugesSafi_Object = MibTableColumn
extremeBgp4V2PrefixGaugesSafi = _ExtremeBgp4V2PrefixGaugesSafi_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8, 1, 2),
    _ExtremeBgp4V2PrefixGaugesSafi_Type()
)
extremeBgp4V2PrefixGaugesSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixGaugesSafi.setStatus("current")
_ExtremeBgp4V2PrefixInPrefixes_Type = Gauge32
_ExtremeBgp4V2PrefixInPrefixes_Object = MibTableColumn
extremeBgp4V2PrefixInPrefixes = _ExtremeBgp4V2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8, 1, 3),
    _ExtremeBgp4V2PrefixInPrefixes_Type()
)
extremeBgp4V2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixInPrefixes.setStatus("current")
_ExtremeBgp4V2PrefixInPrefixesAccepted_Type = Gauge32
_ExtremeBgp4V2PrefixInPrefixesAccepted_Object = MibTableColumn
extremeBgp4V2PrefixInPrefixesAccepted = _ExtremeBgp4V2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8, 1, 4),
    _ExtremeBgp4V2PrefixInPrefixesAccepted_Type()
)
extremeBgp4V2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixInPrefixesAccepted.setStatus("current")
_ExtremeBgp4V2PrefixOutPrefixes_Type = Gauge32
_ExtremeBgp4V2PrefixOutPrefixes_Object = MibTableColumn
extremeBgp4V2PrefixOutPrefixes = _ExtremeBgp4V2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 8, 1, 5),
    _ExtremeBgp4V2PrefixOutPrefixes_Type()
)
extremeBgp4V2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2PrefixOutPrefixes.setStatus("current")
_ExtremeBgp4V2NlriTable_Object = MibTable
extremeBgp4V2NlriTable = _ExtremeBgp4V2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9)
)
if mibBuilder.loadTexts:
    extremeBgp4V2NlriTable.setStatus("current")
_ExtremeBgp4V2NlriEntry_Object = MibTableRow
extremeBgp4V2NlriEntry = _ExtremeBgp4V2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1)
)
extremeBgp4V2NlriEntry.setIndexNames(
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInstance"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAfi"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriSafi"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPrefixType"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPrefix"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPrefixLen"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddrType"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddr"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriIndex"),
)
if mibBuilder.loadTexts:
    extremeBgp4V2NlriEntry.setStatus("current")


class _ExtremeBgp4V2NlriIndex_Type(Unsigned32):
    """Custom type extremeBgp4V2NlriIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExtremeBgp4V2NlriIndex_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2NlriIndex_Object = MibTableColumn
extremeBgp4V2NlriIndex = _ExtremeBgp4V2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 1),
    _ExtremeBgp4V2NlriIndex_Type()
)
extremeBgp4V2NlriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriIndex.setStatus("current")
_ExtremeBgp4V2NlriAfi_Type = ExtremeBgp4V2AddressFamilyIdentifierTC
_ExtremeBgp4V2NlriAfi_Object = MibTableColumn
extremeBgp4V2NlriAfi = _ExtremeBgp4V2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 2),
    _ExtremeBgp4V2NlriAfi_Type()
)
extremeBgp4V2NlriAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAfi.setStatus("current")
_ExtremeBgp4V2NlriSafi_Type = ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC
_ExtremeBgp4V2NlriSafi_Object = MibTableColumn
extremeBgp4V2NlriSafi = _ExtremeBgp4V2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 3),
    _ExtremeBgp4V2NlriSafi_Type()
)
extremeBgp4V2NlriSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriSafi.setStatus("current")
_ExtremeBgp4V2NlriPrefixType_Type = InetAddressType
_ExtremeBgp4V2NlriPrefixType_Object = MibTableColumn
extremeBgp4V2NlriPrefixType = _ExtremeBgp4V2NlriPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 4),
    _ExtremeBgp4V2NlriPrefixType_Type()
)
extremeBgp4V2NlriPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriPrefixType.setStatus("current")
_ExtremeBgp4V2NlriPrefix_Type = InetAddress
_ExtremeBgp4V2NlriPrefix_Object = MibTableColumn
extremeBgp4V2NlriPrefix = _ExtremeBgp4V2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 5),
    _ExtremeBgp4V2NlriPrefix_Type()
)
extremeBgp4V2NlriPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriPrefix.setStatus("current")
_ExtremeBgp4V2NlriPrefixLen_Type = InetAddressPrefixLength
_ExtremeBgp4V2NlriPrefixLen_Object = MibTableColumn
extremeBgp4V2NlriPrefixLen = _ExtremeBgp4V2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 6),
    _ExtremeBgp4V2NlriPrefixLen_Type()
)
extremeBgp4V2NlriPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriPrefixLen.setStatus("current")
_ExtremeBgp4V2NlriBest_Type = TruthValue
_ExtremeBgp4V2NlriBest_Object = MibTableColumn
extremeBgp4V2NlriBest = _ExtremeBgp4V2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 7),
    _ExtremeBgp4V2NlriBest_Type()
)
extremeBgp4V2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriBest.setStatus("current")
_ExtremeBgp4V2NlriCalcLocalPref_Type = Unsigned32
_ExtremeBgp4V2NlriCalcLocalPref_Object = MibTableColumn
extremeBgp4V2NlriCalcLocalPref = _ExtremeBgp4V2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 8),
    _ExtremeBgp4V2NlriCalcLocalPref_Type()
)
extremeBgp4V2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriCalcLocalPref.setStatus("current")


class _ExtremeBgp4V2NlriOrigin_Type(Integer32):
    """Custom type extremeBgp4V2NlriOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_ExtremeBgp4V2NlriOrigin_Type.__name__ = "Integer32"
_ExtremeBgp4V2NlriOrigin_Object = MibTableColumn
extremeBgp4V2NlriOrigin = _ExtremeBgp4V2NlriOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 9),
    _ExtremeBgp4V2NlriOrigin_Type()
)
extremeBgp4V2NlriOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriOrigin.setStatus("current")
_ExtremeBgp4V2NlriNextHopAddrType_Type = InetAddressType
_ExtremeBgp4V2NlriNextHopAddrType_Object = MibTableColumn
extremeBgp4V2NlriNextHopAddrType = _ExtremeBgp4V2NlriNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 10),
    _ExtremeBgp4V2NlriNextHopAddrType_Type()
)
extremeBgp4V2NlriNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriNextHopAddrType.setStatus("current")


class _ExtremeBgp4V2NlriNextHopAddr_Type(InetAddress):
    """Custom type extremeBgp4V2NlriNextHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_ExtremeBgp4V2NlriNextHopAddr_Type.__name__ = "InetAddress"
_ExtremeBgp4V2NlriNextHopAddr_Object = MibTableColumn
extremeBgp4V2NlriNextHopAddr = _ExtremeBgp4V2NlriNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 11),
    _ExtremeBgp4V2NlriNextHopAddr_Type()
)
extremeBgp4V2NlriNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriNextHopAddr.setStatus("current")
_ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Type = InetAddressType
_ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Object = MibTableColumn
extremeBgp4V2NlriLinkLocalNextHopAddrType = _ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 12),
    _ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Type()
)
extremeBgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriLinkLocalNextHopAddrType.setStatus("current")
_ExtremeBgp4V2NlriLinkLocalNextHopAddr_Type = InetAddress
_ExtremeBgp4V2NlriLinkLocalNextHopAddr_Object = MibTableColumn
extremeBgp4V2NlriLinkLocalNextHopAddr = _ExtremeBgp4V2NlriLinkLocalNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 13),
    _ExtremeBgp4V2NlriLinkLocalNextHopAddr_Type()
)
extremeBgp4V2NlriLinkLocalNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriLinkLocalNextHopAddr.setStatus("current")
_ExtremeBgp4V2NlriLocalPrefPresent_Type = TruthValue
_ExtremeBgp4V2NlriLocalPrefPresent_Object = MibTableColumn
extremeBgp4V2NlriLocalPrefPresent = _ExtremeBgp4V2NlriLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 14),
    _ExtremeBgp4V2NlriLocalPrefPresent_Type()
)
extremeBgp4V2NlriLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriLocalPrefPresent.setStatus("current")
_ExtremeBgp4V2NlriLocalPref_Type = Unsigned32
_ExtremeBgp4V2NlriLocalPref_Object = MibTableColumn
extremeBgp4V2NlriLocalPref = _ExtremeBgp4V2NlriLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 15),
    _ExtremeBgp4V2NlriLocalPref_Type()
)
extremeBgp4V2NlriLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriLocalPref.setStatus("current")
_ExtremeBgp4V2NlriMedPresent_Type = TruthValue
_ExtremeBgp4V2NlriMedPresent_Object = MibTableColumn
extremeBgp4V2NlriMedPresent = _ExtremeBgp4V2NlriMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 16),
    _ExtremeBgp4V2NlriMedPresent_Type()
)
extremeBgp4V2NlriMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriMedPresent.setStatus("current")
_ExtremeBgp4V2NlriMed_Type = Unsigned32
_ExtremeBgp4V2NlriMed_Object = MibTableColumn
extremeBgp4V2NlriMed = _ExtremeBgp4V2NlriMed_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 17),
    _ExtremeBgp4V2NlriMed_Type()
)
extremeBgp4V2NlriMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriMed.setStatus("current")
_ExtremeBgp4V2NlriAtomicAggregate_Type = TruthValue
_ExtremeBgp4V2NlriAtomicAggregate_Object = MibTableColumn
extremeBgp4V2NlriAtomicAggregate = _ExtremeBgp4V2NlriAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 18),
    _ExtremeBgp4V2NlriAtomicAggregate_Type()
)
extremeBgp4V2NlriAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAtomicAggregate.setStatus("current")
_ExtremeBgp4V2NlriAggregatorPresent_Type = TruthValue
_ExtremeBgp4V2NlriAggregatorPresent_Object = MibTableColumn
extremeBgp4V2NlriAggregatorPresent = _ExtremeBgp4V2NlriAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 19),
    _ExtremeBgp4V2NlriAggregatorPresent_Type()
)
extremeBgp4V2NlriAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAggregatorPresent.setStatus("current")
_ExtremeBgp4V2NlriAggregatorAS_Type = InetAutonomousSystemNumber
_ExtremeBgp4V2NlriAggregatorAS_Object = MibTableColumn
extremeBgp4V2NlriAggregatorAS = _ExtremeBgp4V2NlriAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 20),
    _ExtremeBgp4V2NlriAggregatorAS_Type()
)
extremeBgp4V2NlriAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAggregatorAS.setStatus("current")
_ExtremeBgp4V2NlriAggregatorAddr_Type = ExtremeBgp4V2IdentifierTC
_ExtremeBgp4V2NlriAggregatorAddr_Object = MibTableColumn
extremeBgp4V2NlriAggregatorAddr = _ExtremeBgp4V2NlriAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 21),
    _ExtremeBgp4V2NlriAggregatorAddr_Type()
)
extremeBgp4V2NlriAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAggregatorAddr.setStatus("current")
_ExtremeBgp4V2NlriAsPathCalcLength_Type = Unsigned32
_ExtremeBgp4V2NlriAsPathCalcLength_Object = MibTableColumn
extremeBgp4V2NlriAsPathCalcLength = _ExtremeBgp4V2NlriAsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 22),
    _ExtremeBgp4V2NlriAsPathCalcLength_Type()
)
extremeBgp4V2NlriAsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAsPathCalcLength.setStatus("current")
_ExtremeBgp4V2NlriAsPathString_Type = SnmpAdminString
_ExtremeBgp4V2NlriAsPathString_Object = MibTableColumn
extremeBgp4V2NlriAsPathString = _ExtremeBgp4V2NlriAsPathString_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 23),
    _ExtremeBgp4V2NlriAsPathString_Type()
)
extremeBgp4V2NlriAsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAsPathString.setStatus("current")


class _ExtremeBgp4V2NlriAsPath_Type(OctetString):
    """Custom type extremeBgp4V2NlriAsPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4072),
    )


_ExtremeBgp4V2NlriAsPath_Type.__name__ = "OctetString"
_ExtremeBgp4V2NlriAsPath_Object = MibTableColumn
extremeBgp4V2NlriAsPath = _ExtremeBgp4V2NlriAsPath_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 24),
    _ExtremeBgp4V2NlriAsPath_Type()
)
extremeBgp4V2NlriAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriAsPath.setStatus("current")


class _ExtremeBgp4V2NlriPathAttrUnknown_Type(OctetString):
    """Custom type extremeBgp4V2NlriPathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4072),
    )


_ExtremeBgp4V2NlriPathAttrUnknown_Type.__name__ = "OctetString"
_ExtremeBgp4V2NlriPathAttrUnknown_Object = MibTableColumn
extremeBgp4V2NlriPathAttrUnknown = _ExtremeBgp4V2NlriPathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 9, 1, 25),
    _ExtremeBgp4V2NlriPathAttrUnknown_Type()
)
extremeBgp4V2NlriPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2NlriPathAttrUnknown.setStatus("current")
_ExtremeBgp4V2AdjRibsOutTable_Object = MibTable
extremeBgp4V2AdjRibsOutTable = _ExtremeBgp4V2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 10)
)
if mibBuilder.loadTexts:
    extremeBgp4V2AdjRibsOutTable.setStatus("current")
_ExtremeBgp4V2AdjRibsOutEntry_Object = MibTableRow
extremeBgp4V2AdjRibsOutEntry = _ExtremeBgp4V2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 10, 1)
)
extremeBgp4V2AdjRibsOutEntry.setIndexNames(
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInstance"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAfi"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriSafi"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPrefixType"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPrefix"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPrefixLen"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddrType"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAddr"),
    (0, "EXTREME-BGP4V2-MIB", "extremeBgp4V2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    extremeBgp4V2AdjRibsOutEntry.setStatus("current")


class _ExtremeBgp4V2AdjRibsOutIndex_Type(Unsigned32):
    """Custom type extremeBgp4V2AdjRibsOutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ExtremeBgp4V2AdjRibsOutIndex_Type.__name__ = "Unsigned32"
_ExtremeBgp4V2AdjRibsOutIndex_Object = MibTableColumn
extremeBgp4V2AdjRibsOutIndex = _ExtremeBgp4V2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 10, 1, 1),
    _ExtremeBgp4V2AdjRibsOutIndex_Type()
)
extremeBgp4V2AdjRibsOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeBgp4V2AdjRibsOutIndex.setStatus("current")
_ExtremeBgp4V2AdjRibsOutRoute_Type = RowPointer
_ExtremeBgp4V2AdjRibsOutRoute_Object = MibTableColumn
extremeBgp4V2AdjRibsOutRoute = _ExtremeBgp4V2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 1, 10, 1, 2),
    _ExtremeBgp4V2AdjRibsOutRoute_Type()
)
extremeBgp4V2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeBgp4V2AdjRibsOutRoute.setStatus("current")
_ExtremeBgp4V2Conformance_ObjectIdentity = ObjectIdentity
extremeBgp4V2Conformance = _ExtremeBgp4V2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2)
)
_ExtremeBgp4V2Compliances_ObjectIdentity = ObjectIdentity
extremeBgp4V2Compliances = _ExtremeBgp4V2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 1)
)
_ExtremeBgp4V2Groups_ObjectIdentity = ObjectIdentity
extremeBgp4V2Groups = _ExtremeBgp4V2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2)
)
extremeBgp4V2PeerEntry.registerAugmentions(
    ("EXTREME-BGP4V2-MIB",
     "extremeBgp4V2PeerErrorsEntry")
)
extremeBgp4V2PeerErrorsEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions(
    ("EXTREME-BGP4V2-MIB",
     "extremeBgp4V2PeerEventTimesEntry")
)
extremeBgp4V2PeerEventTimesEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions(
    ("EXTREME-BGP4V2-MIB",
     "extremeBgp4V2PeerConfiguredTimersEntry")
)
extremeBgp4V2PeerConfiguredTimersEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions(
    ("EXTREME-BGP4V2-MIB",
     "extremeBgp4V2PeerNegotiatedTimersEntry")
)
extremeBgp4V2PeerNegotiatedTimersEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions(
    ("EXTREME-BGP4V2-MIB",
     "extremeBgp4V2PeerCountersEntry")
)
extremeBgp4V2PeerCountersEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())

# Managed Objects groups

extremeBgp4V2GlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 1)
)
extremeBgp4V2GlobalsGroup.setObjects(
    ("EXTREME-BGP4V2-MIB", "extremeBgp4V2DiscontinuityTime")
)
if mibBuilder.loadTexts:
    extremeBgp4V2GlobalsGroup.setStatus("current")

extremeBgp4V2StdMIBTimersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 2)
)
extremeBgp4V2StdMIBTimersGroup.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerFsmEstablishedTime"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInUpdatesElapsedTime"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerConnectRetryInterval"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerHoldTimeConfigured"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerKeepAliveConfigured"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerMinASOrigInterval"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerMinRouteAdverInterval"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerHoldTime"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerKeepAlive"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2StdMIBTimersGroup.setStatus("current")

extremeBgp4V2StdMIBCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 3)
)
extremeBgp4V2StdMIBCountersGroup.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInUpdates"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerOutUpdates"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerInTotalMessages"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerOutTotalMessages"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerFsmEstablishedTransitions"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PrefixInPrefixes"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PrefixInPrefixesAccepted"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PrefixOutPrefixes"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2StdMIBCountersGroup.setStatus("current")

extremeBgp4V2StdMIBErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 5)
)
extremeBgp4V2StdMIBErrorsGroup.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorCodeReceived"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorSubCodeReceived"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorReceivedData"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorReceivedTime"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorReceivedText"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorCodeSent"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorSubCodeSent"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorSentData"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorSentTime"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorSentText"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2StdMIBErrorsGroup.setStatus("current")

extremeBgp4V2StdMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 6)
)
extremeBgp4V2StdMIBPeerGroup.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerState"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerAdminStatus"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAddrType"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalPort"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalAs"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemotePort"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteAs"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalIdentifier"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemoteIdentifier"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerDescription"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2StdMIBPeerGroup.setStatus("current")

extremeBgp4V2StdMIBNlriGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 7)
)
extremeBgp4V2StdMIBNlriGroup.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAsPathCalcLength"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAsPathString"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriBest"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriCalcLocalPref"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2AdjRibsOutRoute"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAggregatorPresent"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAggregatorAS"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAggregatorAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAtomicAggregate"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriLocalPref"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriLocalPrefPresent"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriMed"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriMedPresent"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriNextHopAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriNextHopAddrType"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriLinkLocalNextHopAddrType"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriLinkLocalNextHopAddr"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriOrigin"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriAsPath"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2NlriPathAttrUnknown"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2StdMIBNlriGroup.setStatus("current")


# Notification objects

extremeBgp4V2EstablishedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 0, 1)
)
extremeBgp4V2EstablishedNotification.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerState"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalPort"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemotePort"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2EstablishedNotification.setStatus(
        "current"
    )

extremeBgp4V2BackwardTransitionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 0, 2)
)
extremeBgp4V2BackwardTransitionNotification.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerState"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLocalPort"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerRemotePort"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorCodeReceived"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorSubCodeReceived"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2PeerLastErrorReceivedText"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2BackwardTransitionNotification.setStatus(
        "current"
    )


# Notifications groups

extremeBgp4V2StdMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 2, 8)
)
extremeBgp4V2StdMIBNotificationGroup.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2EstablishedNotification"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2BackwardTransitionNotification"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2StdMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

extremeBgp4V2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1916, 1, 51, 2, 1, 4)
)
extremeBgp4V2Compliance.setObjects(
      *(("EXTREME-BGP4V2-MIB", "extremeBgp4V2StdMIBTimersGroup"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2StdMIBCountersGroup"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2StdMIBErrorsGroup"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2StdMIBPeerGroup"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2StdMIBNlriGroup"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2GlobalsGroup"),
        ("EXTREME-BGP4V2-MIB", "extremeBgp4V2StdMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    extremeBgp4V2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-BGP4V2-MIB",
    **{"extremeBgp4V2": extremeBgp4V2,
       "extremeBgp4V2Notifications": extremeBgp4V2Notifications,
       "extremeBgp4V2EstablishedNotification": extremeBgp4V2EstablishedNotification,
       "extremeBgp4V2BackwardTransitionNotification": extremeBgp4V2BackwardTransitionNotification,
       "extremeBgp4V2Objects": extremeBgp4V2Objects,
       "extremeBgp4V2DiscontinuityTable": extremeBgp4V2DiscontinuityTable,
       "extremeBgp4V2DiscontinuityEntry": extremeBgp4V2DiscontinuityEntry,
       "extremeBgp4V2DiscontinuityTime": extremeBgp4V2DiscontinuityTime,
       "extremeBgp4V2PeerTable": extremeBgp4V2PeerTable,
       "extremeBgp4V2PeerEntry": extremeBgp4V2PeerEntry,
       "extremeBgp4V2PeerInstance": extremeBgp4V2PeerInstance,
       "extremeBgp4V2PeerLocalAddrType": extremeBgp4V2PeerLocalAddrType,
       "extremeBgp4V2PeerLocalAddr": extremeBgp4V2PeerLocalAddr,
       "extremeBgp4V2PeerRemoteAddrType": extremeBgp4V2PeerRemoteAddrType,
       "extremeBgp4V2PeerRemoteAddr": extremeBgp4V2PeerRemoteAddr,
       "extremeBgp4V2PeerLocalPort": extremeBgp4V2PeerLocalPort,
       "extremeBgp4V2PeerLocalAs": extremeBgp4V2PeerLocalAs,
       "extremeBgp4V2PeerLocalIdentifier": extremeBgp4V2PeerLocalIdentifier,
       "extremeBgp4V2PeerRemotePort": extremeBgp4V2PeerRemotePort,
       "extremeBgp4V2PeerRemoteAs": extremeBgp4V2PeerRemoteAs,
       "extremeBgp4V2PeerRemoteIdentifier": extremeBgp4V2PeerRemoteIdentifier,
       "extremeBgp4V2PeerAdminStatus": extremeBgp4V2PeerAdminStatus,
       "extremeBgp4V2PeerState": extremeBgp4V2PeerState,
       "extremeBgp4V2PeerDescription": extremeBgp4V2PeerDescription,
       "extremeBgp4V2PeerErrorsTable": extremeBgp4V2PeerErrorsTable,
       "extremeBgp4V2PeerErrorsEntry": extremeBgp4V2PeerErrorsEntry,
       "extremeBgp4V2PeerLastErrorCodeReceived": extremeBgp4V2PeerLastErrorCodeReceived,
       "extremeBgp4V2PeerLastErrorSubCodeReceived": extremeBgp4V2PeerLastErrorSubCodeReceived,
       "extremeBgp4V2PeerLastErrorReceivedTime": extremeBgp4V2PeerLastErrorReceivedTime,
       "extremeBgp4V2PeerLastErrorReceivedText": extremeBgp4V2PeerLastErrorReceivedText,
       "extremeBgp4V2PeerLastErrorReceivedData": extremeBgp4V2PeerLastErrorReceivedData,
       "extremeBgp4V2PeerLastErrorCodeSent": extremeBgp4V2PeerLastErrorCodeSent,
       "extremeBgp4V2PeerLastErrorSubCodeSent": extremeBgp4V2PeerLastErrorSubCodeSent,
       "extremeBgp4V2PeerLastErrorSentTime": extremeBgp4V2PeerLastErrorSentTime,
       "extremeBgp4V2PeerLastErrorSentText": extremeBgp4V2PeerLastErrorSentText,
       "extremeBgp4V2PeerLastErrorSentData": extremeBgp4V2PeerLastErrorSentData,
       "extremeBgp4V2PeerEventTimesTable": extremeBgp4V2PeerEventTimesTable,
       "extremeBgp4V2PeerEventTimesEntry": extremeBgp4V2PeerEventTimesEntry,
       "extremeBgp4V2PeerFsmEstablishedTime": extremeBgp4V2PeerFsmEstablishedTime,
       "extremeBgp4V2PeerInUpdatesElapsedTime": extremeBgp4V2PeerInUpdatesElapsedTime,
       "extremeBgp4V2PeerConfiguredTimersTable": extremeBgp4V2PeerConfiguredTimersTable,
       "extremeBgp4V2PeerConfiguredTimersEntry": extremeBgp4V2PeerConfiguredTimersEntry,
       "extremeBgp4V2PeerConnectRetryInterval": extremeBgp4V2PeerConnectRetryInterval,
       "extremeBgp4V2PeerHoldTimeConfigured": extremeBgp4V2PeerHoldTimeConfigured,
       "extremeBgp4V2PeerKeepAliveConfigured": extremeBgp4V2PeerKeepAliveConfigured,
       "extremeBgp4V2PeerMinASOrigInterval": extremeBgp4V2PeerMinASOrigInterval,
       "extremeBgp4V2PeerMinRouteAdverInterval": extremeBgp4V2PeerMinRouteAdverInterval,
       "extremeBgp4V2PeerNegotiatedTimersTable": extremeBgp4V2PeerNegotiatedTimersTable,
       "extremeBgp4V2PeerNegotiatedTimersEntry": extremeBgp4V2PeerNegotiatedTimersEntry,
       "extremeBgp4V2PeerHoldTime": extremeBgp4V2PeerHoldTime,
       "extremeBgp4V2PeerKeepAlive": extremeBgp4V2PeerKeepAlive,
       "extremeBgp4V2PeerCountersTable": extremeBgp4V2PeerCountersTable,
       "extremeBgp4V2PeerCountersEntry": extremeBgp4V2PeerCountersEntry,
       "extremeBgp4V2PeerInUpdates": extremeBgp4V2PeerInUpdates,
       "extremeBgp4V2PeerOutUpdates": extremeBgp4V2PeerOutUpdates,
       "extremeBgp4V2PeerInTotalMessages": extremeBgp4V2PeerInTotalMessages,
       "extremeBgp4V2PeerOutTotalMessages": extremeBgp4V2PeerOutTotalMessages,
       "extremeBgp4V2PeerFsmEstablishedTransitions": extremeBgp4V2PeerFsmEstablishedTransitions,
       "extremeBgp4V2PrefixGaugesTable": extremeBgp4V2PrefixGaugesTable,
       "extremeBgp4V2PrefixGaugesEntry": extremeBgp4V2PrefixGaugesEntry,
       "extremeBgp4V2PrefixGaugesAfi": extremeBgp4V2PrefixGaugesAfi,
       "extremeBgp4V2PrefixGaugesSafi": extremeBgp4V2PrefixGaugesSafi,
       "extremeBgp4V2PrefixInPrefixes": extremeBgp4V2PrefixInPrefixes,
       "extremeBgp4V2PrefixInPrefixesAccepted": extremeBgp4V2PrefixInPrefixesAccepted,
       "extremeBgp4V2PrefixOutPrefixes": extremeBgp4V2PrefixOutPrefixes,
       "extremeBgp4V2NlriTable": extremeBgp4V2NlriTable,
       "extremeBgp4V2NlriEntry": extremeBgp4V2NlriEntry,
       "extremeBgp4V2NlriIndex": extremeBgp4V2NlriIndex,
       "extremeBgp4V2NlriAfi": extremeBgp4V2NlriAfi,
       "extremeBgp4V2NlriSafi": extremeBgp4V2NlriSafi,
       "extremeBgp4V2NlriPrefixType": extremeBgp4V2NlriPrefixType,
       "extremeBgp4V2NlriPrefix": extremeBgp4V2NlriPrefix,
       "extremeBgp4V2NlriPrefixLen": extremeBgp4V2NlriPrefixLen,
       "extremeBgp4V2NlriBest": extremeBgp4V2NlriBest,
       "extremeBgp4V2NlriCalcLocalPref": extremeBgp4V2NlriCalcLocalPref,
       "extremeBgp4V2NlriOrigin": extremeBgp4V2NlriOrigin,
       "extremeBgp4V2NlriNextHopAddrType": extremeBgp4V2NlriNextHopAddrType,
       "extremeBgp4V2NlriNextHopAddr": extremeBgp4V2NlriNextHopAddr,
       "extremeBgp4V2NlriLinkLocalNextHopAddrType": extremeBgp4V2NlriLinkLocalNextHopAddrType,
       "extremeBgp4V2NlriLinkLocalNextHopAddr": extremeBgp4V2NlriLinkLocalNextHopAddr,
       "extremeBgp4V2NlriLocalPrefPresent": extremeBgp4V2NlriLocalPrefPresent,
       "extremeBgp4V2NlriLocalPref": extremeBgp4V2NlriLocalPref,
       "extremeBgp4V2NlriMedPresent": extremeBgp4V2NlriMedPresent,
       "extremeBgp4V2NlriMed": extremeBgp4V2NlriMed,
       "extremeBgp4V2NlriAtomicAggregate": extremeBgp4V2NlriAtomicAggregate,
       "extremeBgp4V2NlriAggregatorPresent": extremeBgp4V2NlriAggregatorPresent,
       "extremeBgp4V2NlriAggregatorAS": extremeBgp4V2NlriAggregatorAS,
       "extremeBgp4V2NlriAggregatorAddr": extremeBgp4V2NlriAggregatorAddr,
       "extremeBgp4V2NlriAsPathCalcLength": extremeBgp4V2NlriAsPathCalcLength,
       "extremeBgp4V2NlriAsPathString": extremeBgp4V2NlriAsPathString,
       "extremeBgp4V2NlriAsPath": extremeBgp4V2NlriAsPath,
       "extremeBgp4V2NlriPathAttrUnknown": extremeBgp4V2NlriPathAttrUnknown,
       "extremeBgp4V2AdjRibsOutTable": extremeBgp4V2AdjRibsOutTable,
       "extremeBgp4V2AdjRibsOutEntry": extremeBgp4V2AdjRibsOutEntry,
       "extremeBgp4V2AdjRibsOutIndex": extremeBgp4V2AdjRibsOutIndex,
       "extremeBgp4V2AdjRibsOutRoute": extremeBgp4V2AdjRibsOutRoute,
       "extremeBgp4V2Conformance": extremeBgp4V2Conformance,
       "extremeBgp4V2Compliances": extremeBgp4V2Compliances,
       "extremeBgp4V2Compliance": extremeBgp4V2Compliance,
       "extremeBgp4V2Groups": extremeBgp4V2Groups,
       "extremeBgp4V2GlobalsGroup": extremeBgp4V2GlobalsGroup,
       "extremeBgp4V2StdMIBTimersGroup": extremeBgp4V2StdMIBTimersGroup,
       "extremeBgp4V2StdMIBCountersGroup": extremeBgp4V2StdMIBCountersGroup,
       "extremeBgp4V2StdMIBErrorsGroup": extremeBgp4V2StdMIBErrorsGroup,
       "extremeBgp4V2StdMIBPeerGroup": extremeBgp4V2StdMIBPeerGroup,
       "extremeBgp4V2StdMIBNlriGroup": extremeBgp4V2StdMIBNlriGroup,
       "extremeBgp4V2StdMIBNotificationGroup": extremeBgp4V2StdMIBNotificationGroup}
)
