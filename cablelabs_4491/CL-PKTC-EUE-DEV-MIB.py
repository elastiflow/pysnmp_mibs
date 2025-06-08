# SNMP MIB module (CL-PKTC-EUE-DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PKTC-EUE-DEV-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(PktcEUETCCreds,
 PktcEUETCCredsType) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-TC-MIB",
    "PktcEUETCCreds",
    "PktcEUETCCredsType")

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

(InetAddress,
 InetAddressDNS,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressDNS",
    "InetAddressType",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEUEDevMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3)
)
if mibBuilder.loadTexts:
    pktcEUEDevMIB.setRevisions(
        ("2010-04-26 00:00",
         "2009-12-14 00:00",
         "2009-05-28 00:00",
         "2008-07-10 00:00",
         "2007-11-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcEUEDevSipProtID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("udp", 2),
          ("tcp", 3),
          ("tls", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PktcEUEDevNotification_ObjectIdentity = ObjectIdentity
pktcEUEDevNotification = _PktcEUEDevNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 0)
)
_PktcEUEDevObjects_ObjectIdentity = ObjectIdentity
pktcEUEDevObjects = _PktcEUEDevObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1)
)
_PktcEUEDevProfile_ObjectIdentity = ObjectIdentity
pktcEUEDevProfile = _PktcEUEDevProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1)
)


class _PktcEUEDevProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEUEDevProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEDevProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEDevProfileVersion_Object = MibScalar
pktcEUEDevProfileVersion = _PktcEUEDevProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 1),
    _PktcEUEDevProfileVersion_Type()
)
pktcEUEDevProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevProfileVersion.setStatus("current")
_PktcEUEDevOpTable_Object = MibTable
pktcEUEDevOpTable = _PktcEUEDevOpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUEDevOpTable.setStatus("current")
_PktcEUEDevOpEntry_Object = MibTableRow
pktcEUEDevOpEntry = _PktcEUEDevOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1)
)
pktcEUEDevOpEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevOpEntry.setStatus("current")


class _PktcEUEDevOpIndex_Type(Unsigned32):
    """Custom type pktcEUEDevOpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevOpIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevOpIndex_Object = MibTableColumn
pktcEUEDevOpIndex = _PktcEUEDevOpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 1),
    _PktcEUEDevOpIndex_Type()
)
pktcEUEDevOpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevOpIndex.setStatus("current")
_PktcEUEDevOpDomain_Type = InetAddressDNS
_PktcEUEDevOpDomain_Object = MibTableColumn
pktcEUEDevOpDomain = _PktcEUEDevOpDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 2),
    _PktcEUEDevOpDomain_Type()
)
pktcEUEDevOpDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpDomain.setStatus("current")


class _PktcEUEDevOpSTUNAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevOpSTUNAddrType based on InetAddressType"""
    defaultValue = 0


_PktcEUEDevOpSTUNAddrType_Type.__name__ = "InetAddressType"
_PktcEUEDevOpSTUNAddrType_Object = MibTableColumn
pktcEUEDevOpSTUNAddrType = _PktcEUEDevOpSTUNAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 3),
    _PktcEUEDevOpSTUNAddrType_Type()
)
pktcEUEDevOpSTUNAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNAddrType.setStatus("current")


class _PktcEUEDevOpSTUNAddr_Type(InetAddress):
    """Custom type pktcEUEDevOpSTUNAddr based on InetAddress"""
    defaultValue = OctetString("")


_PktcEUEDevOpSTUNAddr_Type.__name__ = "InetAddress"
_PktcEUEDevOpSTUNAddr_Object = MibTableColumn
pktcEUEDevOpSTUNAddr = _PktcEUEDevOpSTUNAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 4),
    _PktcEUEDevOpSTUNAddr_Type()
)
pktcEUEDevOpSTUNAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNAddr.setStatus("current")


class _PktcEUEDevOpSTUNAddrPort_Type(InetPortNumber):
    """Custom type pktcEUEDevOpSTUNAddrPort based on InetPortNumber"""
    defaultValue = 0


_PktcEUEDevOpSTUNAddrPort_Type.__name__ = "InetPortNumber"
_PktcEUEDevOpSTUNAddrPort_Object = MibTableColumn
pktcEUEDevOpSTUNAddrPort = _PktcEUEDevOpSTUNAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 5),
    _PktcEUEDevOpSTUNAddrPort_Type()
)
pktcEUEDevOpSTUNAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpSTUNAddrPort.setStatus("current")


class _PktcEUEDevOpTURNAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevOpTURNAddrType based on InetAddressType"""
    defaultValue = 0


_PktcEUEDevOpTURNAddrType_Type.__name__ = "InetAddressType"
_PktcEUEDevOpTURNAddrType_Object = MibTableColumn
pktcEUEDevOpTURNAddrType = _PktcEUEDevOpTURNAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 6),
    _PktcEUEDevOpTURNAddrType_Type()
)
pktcEUEDevOpTURNAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpTURNAddrType.setStatus("current")


class _PktcEUEDevOpTURNAddr_Type(InetAddress):
    """Custom type pktcEUEDevOpTURNAddr based on InetAddress"""
    defaultValue = OctetString("")


_PktcEUEDevOpTURNAddr_Type.__name__ = "InetAddress"
_PktcEUEDevOpTURNAddr_Object = MibTableColumn
pktcEUEDevOpTURNAddr = _PktcEUEDevOpTURNAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 7),
    _PktcEUEDevOpTURNAddr_Type()
)
pktcEUEDevOpTURNAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpTURNAddr.setStatus("current")


class _PktcEUEDevOpTURNAddrPort_Type(InetPortNumber):
    """Custom type pktcEUEDevOpTURNAddrPort based on InetPortNumber"""
    defaultValue = 0


_PktcEUEDevOpTURNAddrPort_Type.__name__ = "InetPortNumber"
_PktcEUEDevOpTURNAddrPort_Object = MibTableColumn
pktcEUEDevOpTURNAddrPort = _PktcEUEDevOpTURNAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 8),
    _PktcEUEDevOpTURNAddrPort_Type()
)
pktcEUEDevOpTURNAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpTURNAddrPort.setStatus("current")


class _PktcEUEDevOpTURNCredsType_Type(PktcEUETCCredsType):
    """Custom type pktcEUEDevOpTURNCredsType based on PktcEUETCCredsType"""
    defaultValue = 2


_PktcEUEDevOpTURNCredsType_Type.__name__ = "PktcEUETCCredsType"
_PktcEUEDevOpTURNCredsType_Object = MibTableColumn
pktcEUEDevOpTURNCredsType = _PktcEUEDevOpTURNCredsType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 9),
    _PktcEUEDevOpTURNCredsType_Type()
)
pktcEUEDevOpTURNCredsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpTURNCredsType.setStatus("current")


class _PktcEUEDevOpTURNCreds_Type(PktcEUETCCreds):
    """Custom type pktcEUEDevOpTURNCreds based on PktcEUETCCreds"""
    defaultValue = OctetString("")


_PktcEUEDevOpTURNCreds_Type.__name__ = "PktcEUETCCreds"
_PktcEUEDevOpTURNCreds_Object = MibTableColumn
pktcEUEDevOpTURNCreds = _PktcEUEDevOpTURNCreds_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 10),
    _PktcEUEDevOpTURNCreds_Type()
)
pktcEUEDevOpTURNCreds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpTURNCreds.setStatus("current")
_PktcEUEDevOpRowStatus_Type = RowStatus
_PktcEUEDevOpRowStatus_Object = MibTableColumn
pktcEUEDevOpRowStatus = _PktcEUEDevOpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 2, 1, 11),
    _PktcEUEDevOpRowStatus_Type()
)
pktcEUEDevOpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevOpRowStatus.setStatus("current")
_PktcEUEDevDnsTable_Object = MibTable
pktcEUEDevDnsTable = _PktcEUEDevDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pktcEUEDevDnsTable.setStatus("current")
_PktcEUEDevDnsEntry_Object = MibTableRow
pktcEUEDevDnsEntry = _PktcEUEDevDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1)
)
pktcEUEDevDnsEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevDnsEntry.setStatus("current")


class _PktcEUEDevDnsIndex_Type(Unsigned32):
    """Custom type pktcEUEDevDnsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevDnsIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevDnsIndex_Object = MibTableColumn
pktcEUEDevDnsIndex = _PktcEUEDevDnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 1),
    _PktcEUEDevDnsIndex_Type()
)
pktcEUEDevDnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevDnsIndex.setStatus("current")


class _PktcEUEDevDnsAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevDnsAddrType based on InetAddressType"""
    defaultValue = 0


_PktcEUEDevDnsAddrType_Type.__name__ = "InetAddressType"
_PktcEUEDevDnsAddrType_Object = MibTableColumn
pktcEUEDevDnsAddrType = _PktcEUEDevDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 2),
    _PktcEUEDevDnsAddrType_Type()
)
pktcEUEDevDnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevDnsAddrType.setStatus("current")


class _PktcEUEDevDnsAddr_Type(InetAddress):
    """Custom type pktcEUEDevDnsAddr based on InetAddress"""
    defaultValue = OctetString("")


_PktcEUEDevDnsAddr_Type.__name__ = "InetAddress"
_PktcEUEDevDnsAddr_Object = MibTableColumn
pktcEUEDevDnsAddr = _PktcEUEDevDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 3),
    _PktcEUEDevDnsAddr_Type()
)
pktcEUEDevDnsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevDnsAddr.setStatus("current")
_PktcEUEDevDnsRowStatus_Type = RowStatus
_PktcEUEDevDnsRowStatus_Object = MibTableColumn
pktcEUEDevDnsRowStatus = _PktcEUEDevDnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 3, 1, 4),
    _PktcEUEDevDnsRowStatus_Type()
)
pktcEUEDevDnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevDnsRowStatus.setStatus("current")
_PktcEUEDevPCSCFTable_Object = MibTable
pktcEUEDevPCSCFTable = _PktcEUEDevPCSCFTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTable.setStatus("current")
_PktcEUEDevPCSCFEntry_Object = MibTableRow
pktcEUEDevPCSCFEntry = _PktcEUEDevPCSCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1)
)
pktcEUEDevPCSCFEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFEntry.setStatus("current")


class _PktcEUEDevPCSCFIndex_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevPCSCFIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFIndex_Object = MibTableColumn
pktcEUEDevPCSCFIndex = _PktcEUEDevPCSCFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 1),
    _PktcEUEDevPCSCFIndex_Type()
)
pktcEUEDevPCSCFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFIndex.setStatus("current")


class _PktcEUEDevPCSCFAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevPCSCFAddrType based on InetAddressType"""
    defaultValue = 0


_PktcEUEDevPCSCFAddrType_Type.__name__ = "InetAddressType"
_PktcEUEDevPCSCFAddrType_Object = MibTableColumn
pktcEUEDevPCSCFAddrType = _PktcEUEDevPCSCFAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 2),
    _PktcEUEDevPCSCFAddrType_Type()
)
pktcEUEDevPCSCFAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFAddrType.setStatus("current")


class _PktcEUEDevPCSCFAddr_Type(InetAddress):
    """Custom type pktcEUEDevPCSCFAddr based on InetAddress"""
    defaultValue = OctetString("")


_PktcEUEDevPCSCFAddr_Type.__name__ = "InetAddress"
_PktcEUEDevPCSCFAddr_Object = MibTableColumn
pktcEUEDevPCSCFAddr = _PktcEUEDevPCSCFAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 3),
    _PktcEUEDevPCSCFAddr_Type()
)
pktcEUEDevPCSCFAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFAddr.setStatus("current")
_PktcEUEDevPCSCFSipPort_Type = InetPortNumber
_PktcEUEDevPCSCFSipPort_Object = MibTableColumn
pktcEUEDevPCSCFSipPort = _PktcEUEDevPCSCFSipPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 4),
    _PktcEUEDevPCSCFSipPort_Type()
)
pktcEUEDevPCSCFSipPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFSipPort.setStatus("current")
_PktcEUEDevPCSCFUsedProtocol_Type = PktcEUEDevSipProtID
_PktcEUEDevPCSCFUsedProtocol_Object = MibTableColumn
pktcEUEDevPCSCFUsedProtocol = _PktcEUEDevPCSCFUsedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 5),
    _PktcEUEDevPCSCFUsedProtocol_Type()
)
pktcEUEDevPCSCFUsedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFUsedProtocol.setStatus("current")
_PktcEUEDevPCSCFUsedInetAddressType_Type = InetAddressType
_PktcEUEDevPCSCFUsedInetAddressType_Object = MibTableColumn
pktcEUEDevPCSCFUsedInetAddressType = _PktcEUEDevPCSCFUsedInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 6),
    _PktcEUEDevPCSCFUsedInetAddressType_Type()
)
pktcEUEDevPCSCFUsedInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFUsedInetAddressType.setStatus("current")
_PktcEUEDevPCSCFUsedInetAddress_Type = InetAddress
_PktcEUEDevPCSCFUsedInetAddress_Object = MibTableColumn
pktcEUEDevPCSCFUsedInetAddress = _PktcEUEDevPCSCFUsedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 7),
    _PktcEUEDevPCSCFUsedInetAddress_Type()
)
pktcEUEDevPCSCFUsedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFUsedInetAddress.setStatus("current")


class _PktcEUEDevPCSCFTimerT1_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFTimerT1 based on Unsigned32"""
    defaultValue = 500


_PktcEUEDevPCSCFTimerT1_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFTimerT1_Object = MibTableColumn
pktcEUEDevPCSCFTimerT1 = _PktcEUEDevPCSCFTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 8),
    _PktcEUEDevPCSCFTimerT1_Type()
)
pktcEUEDevPCSCFTimerT1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerT1.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerT1.setUnits("milliseconds")


class _PktcEUEDevPCSCFTimerT2_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFTimerT2 based on Unsigned32"""
    defaultValue = 4000


_PktcEUEDevPCSCFTimerT2_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFTimerT2_Object = MibTableColumn
pktcEUEDevPCSCFTimerT2 = _PktcEUEDevPCSCFTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 9),
    _PktcEUEDevPCSCFTimerT2_Type()
)
pktcEUEDevPCSCFTimerT2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerT2.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerT2.setUnits("milliseconds")


class _PktcEUEDevPCSCFTimerT4_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFTimerT4 based on Unsigned32"""
    defaultValue = 5000


_PktcEUEDevPCSCFTimerT4_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFTimerT4_Object = MibTableColumn
pktcEUEDevPCSCFTimerT4 = _PktcEUEDevPCSCFTimerT4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 10),
    _PktcEUEDevPCSCFTimerT4_Type()
)
pktcEUEDevPCSCFTimerT4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerT4.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerT4.setUnits("milliseconds")


class _PktcEUEDevPCSCFTimerTD_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFTimerTD based on Unsigned32"""
    defaultValue = 32000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32000, 4294967295),
    )


_PktcEUEDevPCSCFTimerTD_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFTimerTD_Object = MibTableColumn
pktcEUEDevPCSCFTimerTD = _PktcEUEDevPCSCFTimerTD_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 11),
    _PktcEUEDevPCSCFTimerTD_Type()
)
pktcEUEDevPCSCFTimerTD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerTD.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFTimerTD.setUnits("milliseconds")
_PktcEUEDevPCSCFRowStatus_Type = RowStatus
_PktcEUEDevPCSCFRowStatus_Object = MibTableColumn
pktcEUEDevPCSCFRowStatus = _PktcEUEDevPCSCFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 12),
    _PktcEUEDevPCSCFRowStatus_Type()
)
pktcEUEDevPCSCFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFRowStatus.setStatus("current")


class _PktcEUEDevPCSCFInviteAttempts_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFInviteAttempts based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PktcEUEDevPCSCFInviteAttempts_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFInviteAttempts_Object = MibTableColumn
pktcEUEDevPCSCFInviteAttempts = _PktcEUEDevPCSCFInviteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 13),
    _PktcEUEDevPCSCFInviteAttempts_Type()
)
pktcEUEDevPCSCFInviteAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFInviteAttempts.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFInviteAttempts.setUnits("attempts")


class _PktcEUEDevPCSCFMaxTime_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFMaxTime based on Unsigned32"""
    defaultValue = 1800


_PktcEUEDevPCSCFMaxTime_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFMaxTime_Object = MibTableColumn
pktcEUEDevPCSCFMaxTime = _PktcEUEDevPCSCFMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 14),
    _PktcEUEDevPCSCFMaxTime_Type()
)
pktcEUEDevPCSCFMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFMaxTime.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFMaxTime.setUnits("seconds")


class _PktcEUEDevPCSCFBaseTimeAllFailed_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFBaseTimeAllFailed based on Unsigned32"""
    defaultValue = 30


_PktcEUEDevPCSCFBaseTimeAllFailed_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFBaseTimeAllFailed_Object = MibTableColumn
pktcEUEDevPCSCFBaseTimeAllFailed = _PktcEUEDevPCSCFBaseTimeAllFailed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 15),
    _PktcEUEDevPCSCFBaseTimeAllFailed_Type()
)
pktcEUEDevPCSCFBaseTimeAllFailed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFBaseTimeAllFailed.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFBaseTimeAllFailed.setUnits("seconds")


class _PktcEUEDevPCSCFBaseTimeAllNotFailed_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFBaseTimeAllNotFailed based on Unsigned32"""
    defaultValue = 90


_PktcEUEDevPCSCFBaseTimeAllNotFailed_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFBaseTimeAllNotFailed_Object = MibTableColumn
pktcEUEDevPCSCFBaseTimeAllNotFailed = _PktcEUEDevPCSCFBaseTimeAllNotFailed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 16),
    _PktcEUEDevPCSCFBaseTimeAllNotFailed_Type()
)
pktcEUEDevPCSCFBaseTimeAllNotFailed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFBaseTimeAllNotFailed.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFBaseTimeAllNotFailed.setUnits("seconds")


class _PktcEUEDevPCSCFSubscribeRetry_Type(Unsigned32):
    """Custom type pktcEUEDevPCSCFSubscribeRetry based on Unsigned32"""
    defaultValue = 900


_PktcEUEDevPCSCFSubscribeRetry_Type.__name__ = "Unsigned32"
_PktcEUEDevPCSCFSubscribeRetry_Object = MibTableColumn
pktcEUEDevPCSCFSubscribeRetry = _PktcEUEDevPCSCFSubscribeRetry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 4, 1, 17),
    _PktcEUEDevPCSCFSubscribeRetry_Type()
)
pktcEUEDevPCSCFSubscribeRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFSubscribeRetry.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFSubscribeRetry.setUnits("seconds")
_PktcEUEDevBSFTable_Object = MibTable
pktcEUEDevBSFTable = _PktcEUEDevBSFTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pktcEUEDevBSFTable.setStatus("current")
_PktcEUEDevBSFEntry_Object = MibTableRow
pktcEUEDevBSFEntry = _PktcEUEDevBSFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5, 1)
)
pktcEUEDevBSFEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFASType"),
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEDevBSFEntry.setStatus("current")


class _PktcEUEDevBSFASType_Type(SnmpAdminString):
    """Custom type pktcEUEDevBSFASType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUEDevBSFASType_Type.__name__ = "SnmpAdminString"
_PktcEUEDevBSFASType_Object = MibTableColumn
pktcEUEDevBSFASType = _PktcEUEDevBSFASType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5, 1, 1),
    _PktcEUEDevBSFASType_Type()
)
pktcEUEDevBSFASType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevBSFASType.setStatus("current")


class _PktcEUEDevBSFIndex_Type(Unsigned32):
    """Custom type pktcEUEDevBSFIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PktcEUEDevBSFIndex_Type.__name__ = "Unsigned32"
_PktcEUEDevBSFIndex_Object = MibTableColumn
pktcEUEDevBSFIndex = _PktcEUEDevBSFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5, 1, 2),
    _PktcEUEDevBSFIndex_Type()
)
pktcEUEDevBSFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEDevBSFIndex.setStatus("current")


class _PktcEUEDevBSFAddrType_Type(InetAddressType):
    """Custom type pktcEUEDevBSFAddrType based on InetAddressType"""
    defaultValue = 0


_PktcEUEDevBSFAddrType_Type.__name__ = "InetAddressType"
_PktcEUEDevBSFAddrType_Object = MibTableColumn
pktcEUEDevBSFAddrType = _PktcEUEDevBSFAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5, 1, 3),
    _PktcEUEDevBSFAddrType_Type()
)
pktcEUEDevBSFAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevBSFAddrType.setStatus("current")


class _PktcEUEDevBSFAddr_Type(InetAddress):
    """Custom type pktcEUEDevBSFAddr based on InetAddress"""
    defaultValue = OctetString("")


_PktcEUEDevBSFAddr_Type.__name__ = "InetAddress"
_PktcEUEDevBSFAddr_Object = MibTableColumn
pktcEUEDevBSFAddr = _PktcEUEDevBSFAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5, 1, 4),
    _PktcEUEDevBSFAddr_Type()
)
pktcEUEDevBSFAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEDevBSFAddr.setStatus("current")
_PktcEUEDevBSFRowStatus_Type = RowStatus
_PktcEUEDevBSFRowStatus_Object = MibTableColumn
pktcEUEDevBSFRowStatus = _PktcEUEDevBSFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 5, 1, 5),
    _PktcEUEDevBSFRowStatus_Type()
)
pktcEUEDevBSFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEDevBSFRowStatus.setStatus("current")
_PktcEUECBSupport_Type = TruthValue
_PktcEUECBSupport_Object = MibScalar
pktcEUECBSupport = _PktcEUECBSupport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 6),
    _PktcEUECBSupport_Type()
)
pktcEUECBSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUECBSupport.setStatus("current")


class _PktcEUECBEnable_Type(TruthValue):
    """Custom type pktcEUECBEnable based on TruthValue"""
    defaultValue = 2


_PktcEUECBEnable_Type.__name__ = "TruthValue"
_PktcEUECBEnable_Object = MibScalar
pktcEUECBEnable = _PktcEUECBEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 7),
    _PktcEUECBEnable_Type()
)
pktcEUECBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUECBEnable.setStatus("current")


class _PktcEUECBData_Type(OctetString):
    """Custom type pktcEUECBData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_PktcEUECBData_Type.__name__ = "OctetString"
_PktcEUECBData_Object = MibScalar
pktcEUECBData = _PktcEUECBData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 8),
    _PktcEUECBData_Type()
)
pktcEUECBData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUECBData.setStatus("current")


class _PktcEUEDevSipPort_Type(InetPortNumber):
    """Custom type pktcEUEDevSipPort based on InetPortNumber"""
    defaultValue = 5060


_PktcEUEDevSipPort_Type.__name__ = "InetPortNumber"
_PktcEUEDevSipPort_Object = MibScalar
pktcEUEDevSipPort = _PktcEUEDevSipPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 1, 1, 9),
    _PktcEUEDevSipPort_Type()
)
pktcEUEDevSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUEDevSipPort.setStatus("current")
_PktcEUEDevConformance_ObjectIdentity = ObjectIdentity
pktcEUEDevConformance = _PktcEUEDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2)
)
_PktcEUEDevCompliances_ObjectIdentity = ObjectIdentity
pktcEUEDevCompliances = _PktcEUEDevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1)
)
_PktcEUEDevGroups_ObjectIdentity = ObjectIdentity
pktcEUEDevGroups = _PktcEUEDevGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2)
)

# Managed Objects groups

pktcEUEDevProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 1)
)
pktcEUEDevProfileGroup.setObjects(
    ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevProfileVersion")
)
if mibBuilder.loadTexts:
    pktcEUEDevProfileGroup.setStatus("current")

pktcEUEDevOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 2)
)
pktcEUEDevOpGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpDomain"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpSTUNAddrPort"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTURNAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTURNAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTURNAddrPort"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTURNCredsType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpTURNCreds"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevOpGroup.setStatus("current")

pktcEUEDevDnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 3)
)
pktcEUEDevDnsGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevDnsGroup.setStatus("current")

pktcEUEDevPCSCFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 4)
)
pktcEUEDevPCSCFGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFSipPort"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFUsedProtocol"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFUsedInetAddressType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFUsedInetAddress"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFTimerT1"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFTimerT2"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFTimerT4"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFTimerTD"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFRowStatus"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFInviteAttempts"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFMaxTime"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFBaseTimeAllFailed"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFBaseTimeAllNotFailed"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFSubscribeRetry"))
)
if mibBuilder.loadTexts:
    pktcEUEDevPCSCFGroup.setStatus("current")

pktcEUEDevBSFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 5)
)
pktcEUEDevBSFGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFAddrType"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFAddr"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEDevBSFGroup.setStatus("current")

pktcEUEDevPerDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 2, 6)
)
pktcEUEDevPerDeviceGroup.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUECBSupport"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUECBEnable"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUECBData"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevSipPort"))
)
if mibBuilder.loadTexts:
    pktcEUEDevPerDeviceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUEDevMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 3, 2, 1, 1)
)
pktcEUEDevMIBCompliance.setObjects(
      *(("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevProfileGroup"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpGroup"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevDnsGroup"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPCSCFGroup"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevBSFGroup"),
        ("CL-PKTC-EUE-DEV-MIB", "pktcEUEDevPerDeviceGroup"))
)
if mibBuilder.loadTexts:
    pktcEUEDevMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-DEV-MIB",
    **{"PktcEUEDevSipProtID": PktcEUEDevSipProtID,
       "pktcEUEDevMIB": pktcEUEDevMIB,
       "pktcEUEDevNotification": pktcEUEDevNotification,
       "pktcEUEDevObjects": pktcEUEDevObjects,
       "pktcEUEDevProfile": pktcEUEDevProfile,
       "pktcEUEDevProfileVersion": pktcEUEDevProfileVersion,
       "pktcEUEDevOpTable": pktcEUEDevOpTable,
       "pktcEUEDevOpEntry": pktcEUEDevOpEntry,
       "pktcEUEDevOpIndex": pktcEUEDevOpIndex,
       "pktcEUEDevOpDomain": pktcEUEDevOpDomain,
       "pktcEUEDevOpSTUNAddrType": pktcEUEDevOpSTUNAddrType,
       "pktcEUEDevOpSTUNAddr": pktcEUEDevOpSTUNAddr,
       "pktcEUEDevOpSTUNAddrPort": pktcEUEDevOpSTUNAddrPort,
       "pktcEUEDevOpTURNAddrType": pktcEUEDevOpTURNAddrType,
       "pktcEUEDevOpTURNAddr": pktcEUEDevOpTURNAddr,
       "pktcEUEDevOpTURNAddrPort": pktcEUEDevOpTURNAddrPort,
       "pktcEUEDevOpTURNCredsType": pktcEUEDevOpTURNCredsType,
       "pktcEUEDevOpTURNCreds": pktcEUEDevOpTURNCreds,
       "pktcEUEDevOpRowStatus": pktcEUEDevOpRowStatus,
       "pktcEUEDevDnsTable": pktcEUEDevDnsTable,
       "pktcEUEDevDnsEntry": pktcEUEDevDnsEntry,
       "pktcEUEDevDnsIndex": pktcEUEDevDnsIndex,
       "pktcEUEDevDnsAddrType": pktcEUEDevDnsAddrType,
       "pktcEUEDevDnsAddr": pktcEUEDevDnsAddr,
       "pktcEUEDevDnsRowStatus": pktcEUEDevDnsRowStatus,
       "pktcEUEDevPCSCFTable": pktcEUEDevPCSCFTable,
       "pktcEUEDevPCSCFEntry": pktcEUEDevPCSCFEntry,
       "pktcEUEDevPCSCFIndex": pktcEUEDevPCSCFIndex,
       "pktcEUEDevPCSCFAddrType": pktcEUEDevPCSCFAddrType,
       "pktcEUEDevPCSCFAddr": pktcEUEDevPCSCFAddr,
       "pktcEUEDevPCSCFSipPort": pktcEUEDevPCSCFSipPort,
       "pktcEUEDevPCSCFUsedProtocol": pktcEUEDevPCSCFUsedProtocol,
       "pktcEUEDevPCSCFUsedInetAddressType": pktcEUEDevPCSCFUsedInetAddressType,
       "pktcEUEDevPCSCFUsedInetAddress": pktcEUEDevPCSCFUsedInetAddress,
       "pktcEUEDevPCSCFTimerT1": pktcEUEDevPCSCFTimerT1,
       "pktcEUEDevPCSCFTimerT2": pktcEUEDevPCSCFTimerT2,
       "pktcEUEDevPCSCFTimerT4": pktcEUEDevPCSCFTimerT4,
       "pktcEUEDevPCSCFTimerTD": pktcEUEDevPCSCFTimerTD,
       "pktcEUEDevPCSCFRowStatus": pktcEUEDevPCSCFRowStatus,
       "pktcEUEDevPCSCFInviteAttempts": pktcEUEDevPCSCFInviteAttempts,
       "pktcEUEDevPCSCFMaxTime": pktcEUEDevPCSCFMaxTime,
       "pktcEUEDevPCSCFBaseTimeAllFailed": pktcEUEDevPCSCFBaseTimeAllFailed,
       "pktcEUEDevPCSCFBaseTimeAllNotFailed": pktcEUEDevPCSCFBaseTimeAllNotFailed,
       "pktcEUEDevPCSCFSubscribeRetry": pktcEUEDevPCSCFSubscribeRetry,
       "pktcEUEDevBSFTable": pktcEUEDevBSFTable,
       "pktcEUEDevBSFEntry": pktcEUEDevBSFEntry,
       "pktcEUEDevBSFASType": pktcEUEDevBSFASType,
       "pktcEUEDevBSFIndex": pktcEUEDevBSFIndex,
       "pktcEUEDevBSFAddrType": pktcEUEDevBSFAddrType,
       "pktcEUEDevBSFAddr": pktcEUEDevBSFAddr,
       "pktcEUEDevBSFRowStatus": pktcEUEDevBSFRowStatus,
       "pktcEUECBSupport": pktcEUECBSupport,
       "pktcEUECBEnable": pktcEUECBEnable,
       "pktcEUECBData": pktcEUECBData,
       "pktcEUEDevSipPort": pktcEUEDevSipPort,
       "pktcEUEDevConformance": pktcEUEDevConformance,
       "pktcEUEDevCompliances": pktcEUEDevCompliances,
       "pktcEUEDevMIBCompliance": pktcEUEDevMIBCompliance,
       "pktcEUEDevGroups": pktcEUEDevGroups,
       "pktcEUEDevProfileGroup": pktcEUEDevProfileGroup,
       "pktcEUEDevOpGroup": pktcEUEDevOpGroup,
       "pktcEUEDevDnsGroup": pktcEUEDevDnsGroup,
       "pktcEUEDevPCSCFGroup": pktcEUEDevPCSCFGroup,
       "pktcEUEDevBSFGroup": pktcEUEDevBSFGroup,
       "pktcEUEDevPerDeviceGroup": pktcEUEDevPerDeviceGroup}
)
