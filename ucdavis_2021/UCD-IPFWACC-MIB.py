# SNMP MIB module (UCD-IPFWACC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ucdavis_2021/UCD-IPFWACC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:49:14 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(ucdExperimental,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental")


# MODULE-IDENTITY

ucdIpFwAccMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1)
)
if mibBuilder.loadTexts:
    ucdIpFwAccMIB.setRevisions(
        ("1999-12-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpFwAccTable_Object = MibTable
ipFwAccTable = _IpFwAccTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1)
)
if mibBuilder.loadTexts:
    ipFwAccTable.setStatus("current")
_IpFwAccEntry_Object = MibTableRow
ipFwAccEntry = _IpFwAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1)
)
ipFwAccEntry.setIndexNames(
    (0, "UCD-IPFWACC-MIB", "ipFwAccIndex"),
)
if mibBuilder.loadTexts:
    ipFwAccEntry.setStatus("current")


class _IpFwAccIndex_Type(Integer32):
    """Custom type ipFwAccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpFwAccIndex_Type.__name__ = "Integer32"
_IpFwAccIndex_Object = MibTableColumn
ipFwAccIndex = _IpFwAccIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 1),
    _IpFwAccIndex_Type()
)
ipFwAccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccIndex.setStatus("current")
_IpFwAccSrcAddr_Type = IpAddress
_IpFwAccSrcAddr_Object = MibTableColumn
ipFwAccSrcAddr = _IpFwAccSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 2),
    _IpFwAccSrcAddr_Type()
)
ipFwAccSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccSrcAddr.setStatus("current")
_IpFwAccSrcNetMask_Type = IpAddress
_IpFwAccSrcNetMask_Object = MibTableColumn
ipFwAccSrcNetMask = _IpFwAccSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 3),
    _IpFwAccSrcNetMask_Type()
)
ipFwAccSrcNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccSrcNetMask.setStatus("current")
_IpFwAccDstAddr_Type = IpAddress
_IpFwAccDstAddr_Object = MibTableColumn
ipFwAccDstAddr = _IpFwAccDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 4),
    _IpFwAccDstAddr_Type()
)
ipFwAccDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDstAddr.setStatus("current")
_IpFwAccDstNetMask_Type = IpAddress
_IpFwAccDstNetMask_Object = MibTableColumn
ipFwAccDstNetMask = _IpFwAccDstNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 5),
    _IpFwAccDstNetMask_Type()
)
ipFwAccDstNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDstNetMask.setStatus("current")


class _IpFwAccViaName_Type(DisplayString):
    """Custom type ipFwAccViaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IpFwAccViaName_Type.__name__ = "DisplayString"
_IpFwAccViaName_Object = MibTableColumn
ipFwAccViaName = _IpFwAccViaName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 6),
    _IpFwAccViaName_Type()
)
ipFwAccViaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccViaName.setStatus("current")
_IpFwAccViaAddr_Type = IpAddress
_IpFwAccViaAddr_Object = MibTableColumn
ipFwAccViaAddr = _IpFwAccViaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 7),
    _IpFwAccViaAddr_Type()
)
ipFwAccViaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccViaAddr.setStatus("current")


class _IpFwAccProto_Type(Integer32):
    """Custom type ipFwAccProto based on Integer32"""
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
        *(("other", 1),
          ("all", 2),
          ("tcp", 3),
          ("udp", 4),
          ("icmp", 5))
    )


_IpFwAccProto_Type.__name__ = "Integer32"
_IpFwAccProto_Object = MibTableColumn
ipFwAccProto = _IpFwAccProto_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 8),
    _IpFwAccProto_Type()
)
ipFwAccProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccProto.setStatus("current")


class _IpFwAccBidir_Type(Integer32):
    """Custom type ipFwAccBidir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )


_IpFwAccBidir_Type.__name__ = "Integer32"
_IpFwAccBidir_Object = MibTableColumn
ipFwAccBidir = _IpFwAccBidir_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 9),
    _IpFwAccBidir_Type()
)
ipFwAccBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccBidir.setStatus("current")


class _IpFwAccDir_Type(Integer32):
    """Custom type ipFwAccDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2),
          ("out", 3))
    )


_IpFwAccDir_Type.__name__ = "Integer32"
_IpFwAccDir_Object = MibTableColumn
ipFwAccDir = _IpFwAccDir_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 10),
    _IpFwAccDir_Type()
)
ipFwAccDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDir.setStatus("current")
_IpFwAccBytes_Type = Counter32
_IpFwAccBytes_Object = MibTableColumn
ipFwAccBytes = _IpFwAccBytes_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 11),
    _IpFwAccBytes_Type()
)
ipFwAccBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccBytes.setStatus("current")
_IpFwAccPackets_Type = Counter32
_IpFwAccPackets_Object = MibTableColumn
ipFwAccPackets = _IpFwAccPackets_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 12),
    _IpFwAccPackets_Type()
)
ipFwAccPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPackets.setStatus("current")
_IpFwAccNrSrcPorts_Type = Integer32
_IpFwAccNrSrcPorts_Object = MibTableColumn
ipFwAccNrSrcPorts = _IpFwAccNrSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 13),
    _IpFwAccNrSrcPorts_Type()
)
ipFwAccNrSrcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccNrSrcPorts.setStatus("current")
_IpFwAccNrDstPorts_Type = Integer32
_IpFwAccNrDstPorts_Object = MibTableColumn
ipFwAccNrDstPorts = _IpFwAccNrDstPorts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 14),
    _IpFwAccNrDstPorts_Type()
)
ipFwAccNrDstPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccNrDstPorts.setStatus("current")


class _IpFwAccSrcIsRange_Type(Integer32):
    """Custom type ipFwAccSrcIsRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srchasrange", 1),
          ("srchasnorange", 2))
    )


_IpFwAccSrcIsRange_Type.__name__ = "Integer32"
_IpFwAccSrcIsRange_Object = MibTableColumn
ipFwAccSrcIsRange = _IpFwAccSrcIsRange_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 15),
    _IpFwAccSrcIsRange_Type()
)
ipFwAccSrcIsRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccSrcIsRange.setStatus("current")


class _IpFwAccDstIsRange_Type(Integer32):
    """Custom type ipFwAccDstIsRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsthasrange", 1),
          ("dsthasnorange", 2))
    )


_IpFwAccDstIsRange_Type.__name__ = "Integer32"
_IpFwAccDstIsRange_Object = MibTableColumn
ipFwAccDstIsRange = _IpFwAccDstIsRange_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 16),
    _IpFwAccDstIsRange_Type()
)
ipFwAccDstIsRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDstIsRange.setStatus("current")
_IpFwAccPort1_Type = Integer32
_IpFwAccPort1_Object = MibTableColumn
ipFwAccPort1 = _IpFwAccPort1_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 17),
    _IpFwAccPort1_Type()
)
ipFwAccPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort1.setStatus("current")
_IpFwAccPort2_Type = Integer32
_IpFwAccPort2_Object = MibTableColumn
ipFwAccPort2 = _IpFwAccPort2_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 18),
    _IpFwAccPort2_Type()
)
ipFwAccPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort2.setStatus("current")
_IpFwAccPort3_Type = Integer32
_IpFwAccPort3_Object = MibTableColumn
ipFwAccPort3 = _IpFwAccPort3_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 19),
    _IpFwAccPort3_Type()
)
ipFwAccPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort3.setStatus("current")
_IpFwAccPort4_Type = Integer32
_IpFwAccPort4_Object = MibTableColumn
ipFwAccPort4 = _IpFwAccPort4_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 20),
    _IpFwAccPort4_Type()
)
ipFwAccPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort4.setStatus("current")
_IpFwAccPort5_Type = Integer32
_IpFwAccPort5_Object = MibTableColumn
ipFwAccPort5 = _IpFwAccPort5_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 21),
    _IpFwAccPort5_Type()
)
ipFwAccPort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort5.setStatus("current")
_IpFwAccPort6_Type = Integer32
_IpFwAccPort6_Object = MibTableColumn
ipFwAccPort6 = _IpFwAccPort6_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 22),
    _IpFwAccPort6_Type()
)
ipFwAccPort6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort6.setStatus("current")
_IpFwAccPort7_Type = Integer32
_IpFwAccPort7_Object = MibTableColumn
ipFwAccPort7 = _IpFwAccPort7_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 23),
    _IpFwAccPort7_Type()
)
ipFwAccPort7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort7.setStatus("current")
_IpFwAccPort8_Type = Integer32
_IpFwAccPort8_Object = MibTableColumn
ipFwAccPort8 = _IpFwAccPort8_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 24),
    _IpFwAccPort8_Type()
)
ipFwAccPort8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort8.setStatus("current")
_IpFwAccPort9_Type = Integer32
_IpFwAccPort9_Object = MibTableColumn
ipFwAccPort9 = _IpFwAccPort9_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 25),
    _IpFwAccPort9_Type()
)
ipFwAccPort9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort9.setStatus("current")
_IpFwAccPort10_Type = Integer32
_IpFwAccPort10_Object = MibTableColumn
ipFwAccPort10 = _IpFwAccPort10_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 26),
    _IpFwAccPort10_Type()
)
ipFwAccPort10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort10.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UCD-IPFWACC-MIB",
    **{"ucdIpFwAccMIB": ucdIpFwAccMIB,
       "ipFwAccTable": ipFwAccTable,
       "ipFwAccEntry": ipFwAccEntry,
       "ipFwAccIndex": ipFwAccIndex,
       "ipFwAccSrcAddr": ipFwAccSrcAddr,
       "ipFwAccSrcNetMask": ipFwAccSrcNetMask,
       "ipFwAccDstAddr": ipFwAccDstAddr,
       "ipFwAccDstNetMask": ipFwAccDstNetMask,
       "ipFwAccViaName": ipFwAccViaName,
       "ipFwAccViaAddr": ipFwAccViaAddr,
       "ipFwAccProto": ipFwAccProto,
       "ipFwAccBidir": ipFwAccBidir,
       "ipFwAccDir": ipFwAccDir,
       "ipFwAccBytes": ipFwAccBytes,
       "ipFwAccPackets": ipFwAccPackets,
       "ipFwAccNrSrcPorts": ipFwAccNrSrcPorts,
       "ipFwAccNrDstPorts": ipFwAccNrDstPorts,
       "ipFwAccSrcIsRange": ipFwAccSrcIsRange,
       "ipFwAccDstIsRange": ipFwAccDstIsRange,
       "ipFwAccPort1": ipFwAccPort1,
       "ipFwAccPort2": ipFwAccPort2,
       "ipFwAccPort3": ipFwAccPort3,
       "ipFwAccPort4": ipFwAccPort4,
       "ipFwAccPort5": ipFwAccPort5,
       "ipFwAccPort6": ipFwAccPort6,
       "ipFwAccPort7": ipFwAccPort7,
       "ipFwAccPort8": ipFwAccPort8,
       "ipFwAccPort9": ipFwAccPort9,
       "ipFwAccPort10": ipFwAccPort10}
)
