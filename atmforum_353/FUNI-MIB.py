# SNMP MIB module (FUNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/atmforum_353/FUNI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:04:44 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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



class FuniValidVpi(Integer32):
    """Custom type FuniValidVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class FuniValidVci(Integer32):
    """Custom type FuniValidVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfFuni_ObjectIdentity = ObjectIdentity
atmfFuni = _AtmfFuni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 6)
)
_FuniMIB_ObjectIdentity = ObjectIdentity
funiMIB = _FuniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1)
)
_FuniMIBObjects_ObjectIdentity = ObjectIdentity
funiMIBObjects = _FuniMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1)
)
_FuniIfConfTable_Object = MibTable
funiIfConfTable = _FuniIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    funiIfConfTable.setStatus("mandatory")
_FuniIfConfEntry_Object = MibTableRow
funiIfConfEntry = _FuniIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1)
)
funiIfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    funiIfConfEntry.setStatus("mandatory")


class _FuniIfConfMode_Type(Integer32):
    """Custom type funiIfConfMode based on Integer32"""
    defaultValue = 1

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
        *(("mode1a", 1),
          ("mode1b", 2),
          ("mode3", 3),
          ("mode4", 4))
    )


_FuniIfConfMode_Type.__name__ = "Integer32"
_FuniIfConfMode_Object = MibTableColumn
funiIfConfMode = _FuniIfConfMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 1),
    _FuniIfConfMode_Type()
)
funiIfConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfMode.setStatus("mandatory")


class _FuniIfConfFcsBits_Type(Integer32):
    """Custom type funiIfConfFcsBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcsBits16", 1),
          ("fcsBits32", 2))
    )


_FuniIfConfFcsBits_Type.__name__ = "Integer32"
_FuniIfConfFcsBits_Object = MibTableColumn
funiIfConfFcsBits = _FuniIfConfFcsBits_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 2),
    _FuniIfConfFcsBits_Type()
)
funiIfConfFcsBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfFcsBits.setStatus("mandatory")


class _FuniIfConfSigSupport_Type(Integer32):
    """Custom type funiIfConfSigSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FuniIfConfSigSupport_Type.__name__ = "Integer32"
_FuniIfConfSigSupport_Object = MibTableColumn
funiIfConfSigSupport = _FuniIfConfSigSupport_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 3),
    _FuniIfConfSigSupport_Type()
)
funiIfConfSigSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfSigSupport.setStatus("mandatory")


class _FuniIfConfSigVpi_Type(FuniValidVpi):
    """Custom type funiIfConfSigVpi based on FuniValidVpi"""
    defaultValue = 0


_FuniIfConfSigVpi_Type.__name__ = "FuniValidVpi"
_FuniIfConfSigVpi_Object = MibTableColumn
funiIfConfSigVpi = _FuniIfConfSigVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 4),
    _FuniIfConfSigVpi_Type()
)
funiIfConfSigVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfSigVpi.setStatus("mandatory")


class _FuniIfConfSigVci_Type(FuniValidVci):
    """Custom type funiIfConfSigVci based on FuniValidVci"""
    defaultValue = 5


_FuniIfConfSigVci_Type.__name__ = "FuniValidVci"
_FuniIfConfSigVci_Object = MibTableColumn
funiIfConfSigVci = _FuniIfConfSigVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 5),
    _FuniIfConfSigVci_Type()
)
funiIfConfSigVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfSigVci.setStatus("mandatory")


class _FuniIfConfIlmiSupport_Type(Integer32):
    """Custom type funiIfConfIlmiSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FuniIfConfIlmiSupport_Type.__name__ = "Integer32"
_FuniIfConfIlmiSupport_Object = MibTableColumn
funiIfConfIlmiSupport = _FuniIfConfIlmiSupport_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 6),
    _FuniIfConfIlmiSupport_Type()
)
funiIfConfIlmiSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfIlmiSupport.setStatus("mandatory")


class _FuniIfConfIlmiVpi_Type(FuniValidVpi):
    """Custom type funiIfConfIlmiVpi based on FuniValidVpi"""
    defaultValue = 0


_FuniIfConfIlmiVpi_Type.__name__ = "FuniValidVpi"
_FuniIfConfIlmiVpi_Object = MibTableColumn
funiIfConfIlmiVpi = _FuniIfConfIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 7),
    _FuniIfConfIlmiVpi_Type()
)
funiIfConfIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfIlmiVpi.setStatus("mandatory")


class _FuniIfConfIlmiVci_Type(FuniValidVci):
    """Custom type funiIfConfIlmiVci based on FuniValidVci"""
    defaultValue = 16


_FuniIfConfIlmiVci_Type.__name__ = "FuniValidVci"
_FuniIfConfIlmiVci_Object = MibTableColumn
funiIfConfIlmiVci = _FuniIfConfIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 8),
    _FuniIfConfIlmiVci_Type()
)
funiIfConfIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfIlmiVci.setStatus("mandatory")


class _FuniIfConfOamSupport_Type(Integer32):
    """Custom type funiIfConfOamSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FuniIfConfOamSupport_Type.__name__ = "Integer32"
_FuniIfConfOamSupport_Object = MibTableColumn
funiIfConfOamSupport = _FuniIfConfOamSupport_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 1, 1, 9),
    _FuniIfConfOamSupport_Type()
)
funiIfConfOamSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfConfOamSupport.setStatus("mandatory")
_FuniIfStatsTable_Object = MibTable
funiIfStatsTable = _FuniIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    funiIfStatsTable.setStatus("mandatory")
_FuniIfStatsEntry_Object = MibTableRow
funiIfStatsEntry = _FuniIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1)
)
funiIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    funiIfStatsEntry.setStatus("mandatory")
_FuniIfEstablishedPvccs_Type = Gauge32
_FuniIfEstablishedPvccs_Object = MibTableColumn
funiIfEstablishedPvccs = _FuniIfEstablishedPvccs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 1),
    _FuniIfEstablishedPvccs_Type()
)
funiIfEstablishedPvccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfEstablishedPvccs.setStatus("mandatory")
_FuniIfEstablishedSvccs_Type = Gauge32
_FuniIfEstablishedSvccs_Object = MibTableColumn
funiIfEstablishedSvccs = _FuniIfEstablishedSvccs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 2),
    _FuniIfEstablishedSvccs_Type()
)
funiIfEstablishedSvccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfEstablishedSvccs.setStatus("mandatory")
_FuniIfRxAbortedFrames_Type = Counter32
_FuniIfRxAbortedFrames_Object = MibTableColumn
funiIfRxAbortedFrames = _FuniIfRxAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 3),
    _FuniIfRxAbortedFrames_Type()
)
funiIfRxAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfRxAbortedFrames.setStatus("mandatory")
_FuniIfRxTooShortFrames_Type = Counter32
_FuniIfRxTooShortFrames_Object = MibTableColumn
funiIfRxTooShortFrames = _FuniIfRxTooShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 4),
    _FuniIfRxTooShortFrames_Type()
)
funiIfRxTooShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfRxTooShortFrames.setStatus("mandatory")
_FuniIfRxTooLongFrames_Type = Counter32
_FuniIfRxTooLongFrames_Object = MibTableColumn
funiIfRxTooLongFrames = _FuniIfRxTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 5),
    _FuniIfRxTooLongFrames_Type()
)
funiIfRxTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfRxTooLongFrames.setStatus("mandatory")
_FuniIfRxFcsErrFrames_Type = Counter32
_FuniIfRxFcsErrFrames_Object = MibTableColumn
funiIfRxFcsErrFrames = _FuniIfRxFcsErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 6),
    _FuniIfRxFcsErrFrames_Type()
)
funiIfRxFcsErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfRxFcsErrFrames.setStatus("mandatory")
_FuniIfRxUnknownFaFrames_Type = Counter32
_FuniIfRxUnknownFaFrames_Object = MibTableColumn
funiIfRxUnknownFaFrames = _FuniIfRxUnknownFaFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 7),
    _FuniIfRxUnknownFaFrames_Type()
)
funiIfRxUnknownFaFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfRxUnknownFaFrames.setStatus("mandatory")
_FuniIfRxDiscardedFrames_Type = Counter32
_FuniIfRxDiscardedFrames_Object = MibTableColumn
funiIfRxDiscardedFrames = _FuniIfRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 8),
    _FuniIfRxDiscardedFrames_Type()
)
funiIfRxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfRxDiscardedFrames.setStatus("mandatory")
_FuniIfTxTooLongFrames_Type = Counter32
_FuniIfTxTooLongFrames_Object = MibTableColumn
funiIfTxTooLongFrames = _FuniIfTxTooLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 9),
    _FuniIfTxTooLongFrames_Type()
)
funiIfTxTooLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfTxTooLongFrames.setStatus("mandatory")
_FuniIfTxLenErrFrames_Type = Counter32
_FuniIfTxLenErrFrames_Object = MibTableColumn
funiIfTxLenErrFrames = _FuniIfTxLenErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 10),
    _FuniIfTxLenErrFrames_Type()
)
funiIfTxLenErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfTxLenErrFrames.setStatus("mandatory")
_FuniIfTxCrcErrFrames_Type = Counter32
_FuniIfTxCrcErrFrames_Object = MibTableColumn
funiIfTxCrcErrFrames = _FuniIfTxCrcErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 11),
    _FuniIfTxCrcErrFrames_Type()
)
funiIfTxCrcErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfTxCrcErrFrames.setStatus("mandatory")
_FuniIfTxPartialFrames_Type = Counter32
_FuniIfTxPartialFrames_Object = MibTableColumn
funiIfTxPartialFrames = _FuniIfTxPartialFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 12),
    _FuniIfTxPartialFrames_Type()
)
funiIfTxPartialFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfTxPartialFrames.setStatus("mandatory")
_FuniIfTxTimeOutFrames_Type = Counter32
_FuniIfTxTimeOutFrames_Object = MibTableColumn
funiIfTxTimeOutFrames = _FuniIfTxTimeOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 13),
    _FuniIfTxTimeOutFrames_Type()
)
funiIfTxTimeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfTxTimeOutFrames.setStatus("mandatory")
_FuniIfTxDiscardedFrames_Type = Counter32
_FuniIfTxDiscardedFrames_Object = MibTableColumn
funiIfTxDiscardedFrames = _FuniIfTxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 2, 1, 14),
    _FuniIfTxDiscardedFrames_Type()
)
funiIfTxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfTxDiscardedFrames.setStatus("mandatory")
_FuniVclStatsTable_Object = MibTable
funiVclStatsTable = _FuniVclStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3)
)
if mibBuilder.loadTexts:
    funiVclStatsTable.setStatus("mandatory")
_FuniVclStatsEntry_Object = MibTableRow
funiVclStatsEntry = _FuniVclStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1)
)
funiVclStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FUNI-MIB", "funiVclFaVpi"),
    (0, "FUNI-MIB", "funiVclFaVci"),
)
if mibBuilder.loadTexts:
    funiVclStatsEntry.setStatus("mandatory")
_FuniVclFaVpi_Type = FuniValidVpi
_FuniVclFaVpi_Object = MibTableColumn
funiVclFaVpi = _FuniVclFaVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 1),
    _FuniVclFaVpi_Type()
)
funiVclFaVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funiVclFaVpi.setStatus("mandatory")
_FuniVclFaVci_Type = FuniValidVci
_FuniVclFaVci_Object = MibTableColumn
funiVclFaVci = _FuniVclFaVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 2),
    _FuniVclFaVci_Type()
)
funiVclFaVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    funiVclFaVci.setStatus("mandatory")
_FuniVclRxClp0Frames_Type = Counter32
_FuniVclRxClp0Frames_Object = MibTableColumn
funiVclRxClp0Frames = _FuniVclRxClp0Frames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 3),
    _FuniVclRxClp0Frames_Type()
)
funiVclRxClp0Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclRxClp0Frames.setStatus("mandatory")
_FuniVclRxTotalFrames_Type = Counter32
_FuniVclRxTotalFrames_Object = MibTableColumn
funiVclRxTotalFrames = _FuniVclRxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 4),
    _FuniVclRxTotalFrames_Type()
)
funiVclRxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclRxTotalFrames.setStatus("mandatory")
_FuniVclTxClp0Frames_Type = Counter32
_FuniVclTxClp0Frames_Object = MibTableColumn
funiVclTxClp0Frames = _FuniVclTxClp0Frames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 5),
    _FuniVclTxClp0Frames_Type()
)
funiVclTxClp0Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclTxClp0Frames.setStatus("mandatory")
_FuniVclTxTotalFrames_Type = Counter32
_FuniVclTxTotalFrames_Object = MibTableColumn
funiVclTxTotalFrames = _FuniVclTxTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 6),
    _FuniVclTxTotalFrames_Type()
)
funiVclTxTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclTxTotalFrames.setStatus("mandatory")
_FuniVclRxClp0Octets_Type = Counter32
_FuniVclRxClp0Octets_Object = MibTableColumn
funiVclRxClp0Octets = _FuniVclRxClp0Octets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 7),
    _FuniVclRxClp0Octets_Type()
)
funiVclRxClp0Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclRxClp0Octets.setStatus("mandatory")
_FuniVclRxTotalOctets_Type = Counter32
_FuniVclRxTotalOctets_Object = MibTableColumn
funiVclRxTotalOctets = _FuniVclRxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 8),
    _FuniVclRxTotalOctets_Type()
)
funiVclRxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclRxTotalOctets.setStatus("mandatory")
_FuniVclTxClp0Octets_Type = Counter32
_FuniVclTxClp0Octets_Object = MibTableColumn
funiVclTxClp0Octets = _FuniVclTxClp0Octets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 9),
    _FuniVclTxClp0Octets_Type()
)
funiVclTxClp0Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclTxClp0Octets.setStatus("mandatory")
_FuniVclTxTotalOctets_Type = Counter32
_FuniVclTxTotalOctets_Object = MibTableColumn
funiVclTxTotalOctets = _FuniVclTxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 10),
    _FuniVclTxTotalOctets_Type()
)
funiVclTxTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclTxTotalOctets.setStatus("mandatory")
_FuniVclRxErrors_Type = Counter32
_FuniVclRxErrors_Object = MibTableColumn
funiVclRxErrors = _FuniVclRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 11),
    _FuniVclRxErrors_Type()
)
funiVclRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclRxErrors.setStatus("mandatory")
_FuniVclTxErrors_Type = Counter32
_FuniVclTxErrors_Object = MibTableColumn
funiVclTxErrors = _FuniVclTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 12),
    _FuniVclTxErrors_Type()
)
funiVclTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclTxErrors.setStatus("mandatory")
_FuniVclRxOamFrames_Type = Counter32
_FuniVclRxOamFrames_Object = MibTableColumn
funiVclRxOamFrames = _FuniVclRxOamFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 13),
    _FuniVclRxOamFrames_Type()
)
funiVclRxOamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclRxOamFrames.setStatus("mandatory")
_FuniVclTxOamFrames_Type = Counter32
_FuniVclTxOamFrames_Object = MibTableColumn
funiVclTxOamFrames = _FuniVclTxOamFrames_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 6, 1, 3, 1, 14),
    _FuniVclTxOamFrames_Type()
)
funiVclTxOamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiVclTxOamFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUNI-MIB",
    **{"FuniValidVpi": FuniValidVpi,
       "FuniValidVci": FuniValidVci,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfFuni": atmfFuni,
       "funiMIB": funiMIB,
       "funiMIBObjects": funiMIBObjects,
       "funiIfConfTable": funiIfConfTable,
       "funiIfConfEntry": funiIfConfEntry,
       "funiIfConfMode": funiIfConfMode,
       "funiIfConfFcsBits": funiIfConfFcsBits,
       "funiIfConfSigSupport": funiIfConfSigSupport,
       "funiIfConfSigVpi": funiIfConfSigVpi,
       "funiIfConfSigVci": funiIfConfSigVci,
       "funiIfConfIlmiSupport": funiIfConfIlmiSupport,
       "funiIfConfIlmiVpi": funiIfConfIlmiVpi,
       "funiIfConfIlmiVci": funiIfConfIlmiVci,
       "funiIfConfOamSupport": funiIfConfOamSupport,
       "funiIfStatsTable": funiIfStatsTable,
       "funiIfStatsEntry": funiIfStatsEntry,
       "funiIfEstablishedPvccs": funiIfEstablishedPvccs,
       "funiIfEstablishedSvccs": funiIfEstablishedSvccs,
       "funiIfRxAbortedFrames": funiIfRxAbortedFrames,
       "funiIfRxTooShortFrames": funiIfRxTooShortFrames,
       "funiIfRxTooLongFrames": funiIfRxTooLongFrames,
       "funiIfRxFcsErrFrames": funiIfRxFcsErrFrames,
       "funiIfRxUnknownFaFrames": funiIfRxUnknownFaFrames,
       "funiIfRxDiscardedFrames": funiIfRxDiscardedFrames,
       "funiIfTxTooLongFrames": funiIfTxTooLongFrames,
       "funiIfTxLenErrFrames": funiIfTxLenErrFrames,
       "funiIfTxCrcErrFrames": funiIfTxCrcErrFrames,
       "funiIfTxPartialFrames": funiIfTxPartialFrames,
       "funiIfTxTimeOutFrames": funiIfTxTimeOutFrames,
       "funiIfTxDiscardedFrames": funiIfTxDiscardedFrames,
       "funiVclStatsTable": funiVclStatsTable,
       "funiVclStatsEntry": funiVclStatsEntry,
       "funiVclFaVpi": funiVclFaVpi,
       "funiVclFaVci": funiVclFaVci,
       "funiVclRxClp0Frames": funiVclRxClp0Frames,
       "funiVclRxTotalFrames": funiVclRxTotalFrames,
       "funiVclTxClp0Frames": funiVclTxClp0Frames,
       "funiVclTxTotalFrames": funiVclTxTotalFrames,
       "funiVclRxClp0Octets": funiVclRxClp0Octets,
       "funiVclRxTotalOctets": funiVclRxTotalOctets,
       "funiVclTxClp0Octets": funiVclTxClp0Octets,
       "funiVclTxTotalOctets": funiVclTxTotalOctets,
       "funiVclRxErrors": funiVclRxErrors,
       "funiVclTxErrors": funiVclTxErrors,
       "funiVclRxOamFrames": funiVclRxOamFrames,
       "funiVclTxOamFrames": funiVclTxOamFrames}
)
