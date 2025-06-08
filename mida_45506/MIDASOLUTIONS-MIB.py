# SNMP MIB module (MIDASOLUTIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/mida_45506/MIDASOLUTIONS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:32:16 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

midasolutions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45506)
)
if mibBuilder.loadTexts:
    midasolutions.setRevisions(
        ("2014-03-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MidaApplications_ObjectIdentity = ObjectIdentity
midaApplications = _MidaApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1)
)
_MidaPlatform_ObjectIdentity = ObjectIdentity
midaPlatform = _MidaPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1)
)


class _MidaApplicationServerStatus_Type(Integer32):
    """Custom type midaApplicationServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaApplicationServerStatus_Type.__name__ = "Integer32"
_MidaApplicationServerStatus_Object = MibScalar
midaApplicationServerStatus = _MidaApplicationServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 1),
    _MidaApplicationServerStatus_Type()
)
midaApplicationServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaApplicationServerStatus.setStatus("current")


class _MidaControlPanelServiceStatus_Type(Integer32):
    """Custom type midaControlPanelServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaControlPanelServiceStatus_Type.__name__ = "Integer32"
_MidaControlPanelServiceStatus_Object = MibScalar
midaControlPanelServiceStatus = _MidaControlPanelServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 2),
    _MidaControlPanelServiceStatus_Type()
)
midaControlPanelServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaControlPanelServiceStatus.setStatus("current")


class _MidaGWControlPanelServiceStatus_Type(Integer32):
    """Custom type midaGWControlPanelServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaGWControlPanelServiceStatus_Type.__name__ = "Integer32"
_MidaGWControlPanelServiceStatus_Object = MibScalar
midaGWControlPanelServiceStatus = _MidaGWControlPanelServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 3),
    _MidaGWControlPanelServiceStatus_Type()
)
midaGWControlPanelServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaGWControlPanelServiceStatus.setStatus("current")


class _MidaSIPServiceStatus_Type(Integer32):
    """Custom type midaSIPServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaSIPServiceStatus_Type.__name__ = "Integer32"
_MidaSIPServiceStatus_Object = MibScalar
midaSIPServiceStatus = _MidaSIPServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 4),
    _MidaSIPServiceStatus_Type()
)
midaSIPServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaSIPServiceStatus.setStatus("current")


class _MidaCTIManagerServiceStatus_Type(Integer32):
    """Custom type midaCTIManagerServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaCTIManagerServiceStatus_Type.__name__ = "Integer32"
_MidaCTIManagerServiceStatus_Object = MibScalar
midaCTIManagerServiceStatus = _MidaCTIManagerServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 5),
    _MidaCTIManagerServiceStatus_Type()
)
midaCTIManagerServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaCTIManagerServiceStatus.setStatus("current")


class _MidaSambaServiceStatus_Type(Integer32):
    """Custom type midaSambaServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaSambaServiceStatus_Type.__name__ = "Integer32"
_MidaSambaServiceStatus_Object = MibScalar
midaSambaServiceStatus = _MidaSambaServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 6),
    _MidaSambaServiceStatus_Type()
)
midaSambaServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaSambaServiceStatus.setStatus("current")


class _MidaGlusterServiceStatus_Type(Integer32):
    """Custom type midaGlusterServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaGlusterServiceStatus_Type.__name__ = "Integer32"
_MidaGlusterServiceStatus_Object = MibScalar
midaGlusterServiceStatus = _MidaGlusterServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 7),
    _MidaGlusterServiceStatus_Type()
)
midaGlusterServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaGlusterServiceStatus.setStatus("current")


class _MidaBucardoServiceStatus_Type(Integer32):
    """Custom type midaBucardoServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaBucardoServiceStatus_Type.__name__ = "Integer32"
_MidaBucardoServiceStatus_Object = MibScalar
midaBucardoServiceStatus = _MidaBucardoServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 8),
    _MidaBucardoServiceStatus_Type()
)
midaBucardoServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaBucardoServiceStatus.setStatus("current")


class _MidaFTPServiceStatus_Type(Integer32):
    """Custom type midaFTPServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaFTPServiceStatus_Type.__name__ = "Integer32"
_MidaFTPServiceStatus_Object = MibScalar
midaFTPServiceStatus = _MidaFTPServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 9),
    _MidaFTPServiceStatus_Type()
)
midaFTPServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFTPServiceStatus.setStatus("current")


class _MidaDatabaseConnectionStatus_Type(Integer32):
    """Custom type midaDatabaseConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaDatabaseConnectionStatus_Type.__name__ = "Integer32"
_MidaDatabaseConnectionStatus_Object = MibScalar
midaDatabaseConnectionStatus = _MidaDatabaseConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 1, 10),
    _MidaDatabaseConnectionStatus_Type()
)
midaDatabaseConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaDatabaseConnectionStatus.setStatus("current")
_MidaBilling_ObjectIdentity = ObjectIdentity
midaBilling = _MidaBilling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 2)
)


class _MidaBillingServiceStatus_Type(Integer32):
    """Custom type midaBillingServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaBillingServiceStatus_Type.__name__ = "Integer32"
_MidaBillingServiceStatus_Object = MibScalar
midaBillingServiceStatus = _MidaBillingServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 2, 1),
    _MidaBillingServiceStatus_Type()
)
midaBillingServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaBillingServiceStatus.setStatus("current")


class _MidaBillingLastCDRProcessed_Type(DisplayString):
    """Custom type midaBillingLastCDRProcessed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MidaBillingLastCDRProcessed_Type.__name__ = "DisplayString"
_MidaBillingLastCDRProcessed_Object = MibScalar
midaBillingLastCDRProcessed = _MidaBillingLastCDRProcessed_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 2, 2),
    _MidaBillingLastCDRProcessed_Type()
)
midaBillingLastCDRProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaBillingLastCDRProcessed.setStatus("current")
_MidaFaxServer_ObjectIdentity = ObjectIdentity
midaFaxServer = _MidaFaxServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3)
)


class _MidaFaxServiceStatus_Type(Integer32):
    """Custom type midaFaxServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaFaxServiceStatus_Type.__name__ = "Integer32"
_MidaFaxServiceStatus_Object = MibScalar
midaFaxServiceStatus = _MidaFaxServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 1),
    _MidaFaxServiceStatus_Type()
)
midaFaxServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxServiceStatus.setStatus("current")


class _MidaFaxNotificationServiceStatus_Type(Integer32):
    """Custom type midaFaxNotificationServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaFaxNotificationServiceStatus_Type.__name__ = "Integer32"
_MidaFaxNotificationServiceStatus_Object = MibScalar
midaFaxNotificationServiceStatus = _MidaFaxNotificationServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 2),
    _MidaFaxNotificationServiceStatus_Type()
)
midaFaxNotificationServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxNotificationServiceStatus.setStatus("current")


class _MidaFaxSendingReceiving_Type(DisplayString):
    """Custom type midaFaxSendingReceiving based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MidaFaxSendingReceiving_Type.__name__ = "DisplayString"
_MidaFaxSendingReceiving_Object = MibScalar
midaFaxSendingReceiving = _MidaFaxSendingReceiving_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 3),
    _MidaFaxSendingReceiving_Type()
)
midaFaxSendingReceiving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxSendingReceiving.setStatus("current")
_MidaFaxFaxQueued_Type = Counter32
_MidaFaxFaxQueued_Object = MibScalar
midaFaxFaxQueued = _MidaFaxFaxQueued_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 4),
    _MidaFaxFaxQueued_Type()
)
midaFaxFaxQueued.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxFaxQueued.setStatus("current")


class _MidaFaxMail2FaxStatus_Type(Integer32):
    """Custom type midaFaxMail2FaxStatus based on Integer32"""
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaFaxMail2FaxStatus_Type.__name__ = "Integer32"
_MidaFaxMail2FaxStatus_Object = MibScalar
midaFaxMail2FaxStatus = _MidaFaxMail2FaxStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 5),
    _MidaFaxMail2FaxStatus_Type()
)
midaFaxMail2FaxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxMail2FaxStatus.setStatus("current")


class _MidaFaxChannelStatus_Type(Integer32):
    """Custom type midaFaxChannelStatus based on Integer32"""
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaFaxChannelStatus_Type.__name__ = "Integer32"
_MidaFaxChannelStatus_Object = MibScalar
midaFaxChannelStatus = _MidaFaxChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 6),
    _MidaFaxChannelStatus_Type()
)
midaFaxChannelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxChannelStatus.setStatus("current")
_MidaFaxChannelTable_Object = MibTable
midaFaxChannelTable = _MidaFaxChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 7)
)
if mibBuilder.loadTexts:
    midaFaxChannelTable.setStatus("current")
_MidaFaxChannelTableEntry_Object = MibTableRow
midaFaxChannelTableEntry = _MidaFaxChannelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 7, 1)
)
midaFaxChannelTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaFaxChannelTableChannelIndex"),
)
if mibBuilder.loadTexts:
    midaFaxChannelTableEntry.setStatus("current")


class _MidaFaxChannelTableChannelIndex_Type(Integer32):
    """Custom type midaFaxChannelTableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaFaxChannelTableChannelIndex_Type.__name__ = "Integer32"
_MidaFaxChannelTableChannelIndex_Object = MibTableColumn
midaFaxChannelTableChannelIndex = _MidaFaxChannelTableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 7, 1, 1),
    _MidaFaxChannelTableChannelIndex_Type()
)
midaFaxChannelTableChannelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaFaxChannelTableChannelIndex.setStatus("current")
_MidaFaxChannelTableChannelStatus_Type = DisplayString
_MidaFaxChannelTableChannelStatus_Object = MibTableColumn
midaFaxChannelTableChannelStatus = _MidaFaxChannelTableChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 7, 1, 2),
    _MidaFaxChannelTableChannelStatus_Type()
)
midaFaxChannelTableChannelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaFaxChannelTableChannelStatus.setStatus("current")
_MidaFaxChannelTableRowStatus_Type = RowStatus
_MidaFaxChannelTableRowStatus_Object = MibTableColumn
midaFaxChannelTableRowStatus = _MidaFaxChannelTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 7, 1, 3),
    _MidaFaxChannelTableRowStatus_Type()
)
midaFaxChannelTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaFaxChannelTableRowStatus.setStatus("current")
_MidaFaxLastReceivedTs_Type = Integer32
_MidaFaxLastReceivedTs_Object = MibScalar
midaFaxLastReceivedTs = _MidaFaxLastReceivedTs_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 8),
    _MidaFaxLastReceivedTs_Type()
)
midaFaxLastReceivedTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxLastReceivedTs.setStatus("current")
_MidaFaxLastSentTs_Type = Integer32
_MidaFaxLastSentTs_Object = MibScalar
midaFaxLastSentTs = _MidaFaxLastSentTs_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 9),
    _MidaFaxLastSentTs_Type()
)
midaFaxLastSentTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxLastSentTs.setStatus("current")
_MidaFaxLastConversionTs_Type = Integer32
_MidaFaxLastConversionTs_Object = MibScalar
midaFaxLastConversionTs = _MidaFaxLastConversionTs_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 10),
    _MidaFaxLastConversionTs_Type()
)
midaFaxLastConversionTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxLastConversionTs.setStatus("current")
_MidaFaxLastArchivedTs_Type = Integer32
_MidaFaxLastArchivedTs_Object = MibScalar
midaFaxLastArchivedTs = _MidaFaxLastArchivedTs_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 11),
    _MidaFaxLastArchivedTs_Type()
)
midaFaxLastArchivedTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxLastArchivedTs.setStatus("current")
_MidaFaxProcessingTime_Type = Integer32
_MidaFaxProcessingTime_Object = MibScalar
midaFaxProcessingTime = _MidaFaxProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 12),
    _MidaFaxProcessingTime_Type()
)
midaFaxProcessingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxProcessingTime.setStatus("current")
_MidaFaxLastMissingAcquisitionReportTs_Type = Integer32
_MidaFaxLastMissingAcquisitionReportTs_Object = MibScalar
midaFaxLastMissingAcquisitionReportTs = _MidaFaxLastMissingAcquisitionReportTs_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 3, 13),
    _MidaFaxLastMissingAcquisitionReportTs_Type()
)
midaFaxLastMissingAcquisitionReportTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaFaxLastMissingAcquisitionReportTs.setStatus("current")
_MidaImportManager_ObjectIdentity = ObjectIdentity
midaImportManager = _MidaImportManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4)
)


class _MidaImportManagerServiceStatus_Type(Integer32):
    """Custom type midaImportManagerServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaImportManagerServiceStatus_Type.__name__ = "Integer32"
_MidaImportManagerServiceStatus_Object = MibScalar
midaImportManagerServiceStatus = _MidaImportManagerServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4, 1),
    _MidaImportManagerServiceStatus_Type()
)
midaImportManagerServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaImportManagerServiceStatus.setStatus("current")
_MidaImportManagerTable_Object = MibTable
midaImportManagerTable = _MidaImportManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4, 2)
)
if mibBuilder.loadTexts:
    midaImportManagerTable.setStatus("current")
_MidaImportManagerTableEntry_Object = MibTableRow
midaImportManagerTableEntry = _MidaImportManagerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4, 2, 1)
)
midaImportManagerTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaImportManagerTableType"),
)
if mibBuilder.loadTexts:
    midaImportManagerTableEntry.setStatus("current")


class _MidaImportManagerTableType_Type(Integer32):
    """Custom type midaImportManagerTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("web", 1),
          ("csv", 2),
          ("axl", 4),
          ("odbc", 8),
          ("ldap", 16),
          ("custom", 32),
          ("ucxsi", 64))
    )


_MidaImportManagerTableType_Type.__name__ = "Integer32"
_MidaImportManagerTableType_Object = MibTableColumn
midaImportManagerTableType = _MidaImportManagerTableType_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4, 2, 1, 1),
    _MidaImportManagerTableType_Type()
)
midaImportManagerTableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaImportManagerTableType.setStatus("current")
_MidaImportManagerTableLastImport_Type = DisplayString
_MidaImportManagerTableLastImport_Object = MibTableColumn
midaImportManagerTableLastImport = _MidaImportManagerTableLastImport_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4, 2, 1, 2),
    _MidaImportManagerTableLastImport_Type()
)
midaImportManagerTableLastImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaImportManagerTableLastImport.setStatus("current")
_MidaImportManagerTableRowStatus_Type = RowStatus
_MidaImportManagerTableRowStatus_Object = MibTableColumn
midaImportManagerTableRowStatus = _MidaImportManagerTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 4, 2, 1, 3),
    _MidaImportManagerTableRowStatus_Type()
)
midaImportManagerTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaImportManagerTableRowStatus.setStatus("current")
_MidaRecorder_ObjectIdentity = ObjectIdentity
midaRecorder = _MidaRecorder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5)
)


class _MidaRecorderSnifferServiceStatus_Type(Integer32):
    """Custom type midaRecorderSnifferServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaRecorderSnifferServiceStatus_Type.__name__ = "Integer32"
_MidaRecorderSnifferServiceStatus_Object = MibScalar
midaRecorderSnifferServiceStatus = _MidaRecorderSnifferServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 1),
    _MidaRecorderSnifferServiceStatus_Type()
)
midaRecorderSnifferServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderSnifferServiceStatus.setStatus("current")


class _MidaVoipRecorderServiceStatus_Type(Integer32):
    """Custom type midaVoipRecorderServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaVoipRecorderServiceStatus_Type.__name__ = "Integer32"
_MidaVoipRecorderServiceStatus_Object = MibScalar
midaVoipRecorderServiceStatus = _MidaVoipRecorderServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 2),
    _MidaVoipRecorderServiceStatus_Type()
)
midaVoipRecorderServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderServiceStatus.setStatus("current")
_MidaRecorderCollectorsTable_Object = MibTable
midaRecorderCollectorsTable = _MidaRecorderCollectorsTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3)
)
if mibBuilder.loadTexts:
    midaRecorderCollectorsTable.setStatus("current")
_MidaRecorderCollectorsTableEntry_Object = MibTableRow
midaRecorderCollectorsTableEntry = _MidaRecorderCollectorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1)
)
midaRecorderCollectorsTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaRecorderCollectorsTableIndex"),
)
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableEntry.setStatus("current")


class _MidaRecorderCollectorsTableIndex_Type(Integer32):
    """Custom type midaRecorderCollectorsTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaRecorderCollectorsTableIndex_Type.__name__ = "Integer32"
_MidaRecorderCollectorsTableIndex_Object = MibTableColumn
midaRecorderCollectorsTableIndex = _MidaRecorderCollectorsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 1),
    _MidaRecorderCollectorsTableIndex_Type()
)
midaRecorderCollectorsTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableIndex.setStatus("current")
_MidaRecorderCollectorsTableChannelSource_Type = DisplayString
_MidaRecorderCollectorsTableChannelSource_Object = MibTableColumn
midaRecorderCollectorsTableChannelSource = _MidaRecorderCollectorsTableChannelSource_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 2),
    _MidaRecorderCollectorsTableChannelSource_Type()
)
midaRecorderCollectorsTableChannelSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableChannelSource.setStatus("current")
_MidaRecorderCollectorsTableIPAddress_Type = DisplayString
_MidaRecorderCollectorsTableIPAddress_Object = MibTableColumn
midaRecorderCollectorsTableIPAddress = _MidaRecorderCollectorsTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 3),
    _MidaRecorderCollectorsTableIPAddress_Type()
)
midaRecorderCollectorsTableIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableIPAddress.setStatus("current")
_MidaRecorderCollectorsTableDownloaded_Type = Integer32
_MidaRecorderCollectorsTableDownloaded_Object = MibTableColumn
midaRecorderCollectorsTableDownloaded = _MidaRecorderCollectorsTableDownloaded_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 4),
    _MidaRecorderCollectorsTableDownloaded_Type()
)
midaRecorderCollectorsTableDownloaded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableDownloaded.setStatus("current")


class _MidaRecorderCollectorsTableStatus_Type(Integer32):
    """Custom type midaRecorderCollectorsTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              20,
              21,
              22,
              23,
              24,
              2000,
              2001,
              4020,
              4055,
              5024)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("success", 0),
          ("failureexceptionoccurred", 1),
          ("failurelicense", 2),
          ("failuregeneralerror", 3),
          ("failureinvalidipaddress", 4),
          ("failureduringcdrdbwriting", 5),
          ("failureduringfilescompression", 6),
          ("failureduringfilesencryption", 7),
          ("failuretimeoutexception", 8),
          ("mgfailurenotmountedshare", 10),
          ("mgfailurebeforefilescopying", 11),
          ("mgfailureduringfilescopying", 12),
          ("mgfailurebeforecdranalyzing", 13),
          ("mgfailureduringcdranalyzing", 14),
          ("mgfailureduringaudiofilesanalyzing", 15),
          ("mgfailurelogin", 20),
          ("mgfailureservertime", 21),
          ("mgfailuresessionsprocesscode", 22),
          ("mgfailuresessionsprocess", 23),
          ("mgfailurelogout", 24),
          ("mgsuccessreqcompleted", 2000),
          ("mgsuccessnoresultfound", 2001),
          ("mgfailurecredentialsareinvalid", 4020),
          ("mgfailurerequestparametermissing", 4055),
          ("mgfailureunknownaxlservice", 5024))
    )


_MidaRecorderCollectorsTableStatus_Type.__name__ = "Integer32"
_MidaRecorderCollectorsTableStatus_Object = MibTableColumn
midaRecorderCollectorsTableStatus = _MidaRecorderCollectorsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 5),
    _MidaRecorderCollectorsTableStatus_Type()
)
midaRecorderCollectorsTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableStatus.setStatus("current")
_MidaRecorderCollectorsTableLastRun_Type = DisplayString
_MidaRecorderCollectorsTableLastRun_Object = MibTableColumn
midaRecorderCollectorsTableLastRun = _MidaRecorderCollectorsTableLastRun_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 6),
    _MidaRecorderCollectorsTableLastRun_Type()
)
midaRecorderCollectorsTableLastRun.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableLastRun.setStatus("current")
_MidaRecorderCollectorsTableRowStatus_Type = RowStatus
_MidaRecorderCollectorsTableRowStatus_Object = MibTableColumn
midaRecorderCollectorsTableRowStatus = _MidaRecorderCollectorsTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 3, 1, 7),
    _MidaRecorderCollectorsTableRowStatus_Type()
)
midaRecorderCollectorsTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderCollectorsTableRowStatus.setStatus("current")
_MidaTDMPortTable_Object = MibTable
midaTDMPortTable = _MidaTDMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4)
)
if mibBuilder.loadTexts:
    midaTDMPortTable.setStatus("current")
_MidaTDMPortTableEntry_Object = MibTableRow
midaTDMPortTableEntry = _MidaTDMPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1)
)
midaTDMPortTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaTDMPortTableIndex"),
)
if mibBuilder.loadTexts:
    midaTDMPortTableEntry.setStatus("current")


class _MidaTDMPortTableIndex_Type(Integer32):
    """Custom type midaTDMPortTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaTDMPortTableIndex_Type.__name__ = "Integer32"
_MidaTDMPortTableIndex_Object = MibTableColumn
midaTDMPortTableIndex = _MidaTDMPortTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 1),
    _MidaTDMPortTableIndex_Type()
)
midaTDMPortTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMPortTableIndex.setStatus("current")
_MidaTDMBoardName_Type = DisplayString
_MidaTDMBoardName_Object = MibTableColumn
midaTDMBoardName = _MidaTDMBoardName_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 2),
    _MidaTDMBoardName_Type()
)
midaTDMBoardName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMBoardName.setStatus("current")
_MidaTDMBoardLogicalIndex_Type = Integer32
_MidaTDMBoardLogicalIndex_Object = MibTableColumn
midaTDMBoardLogicalIndex = _MidaTDMBoardLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 3),
    _MidaTDMBoardLogicalIndex_Type()
)
midaTDMBoardLogicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMBoardLogicalIndex.setStatus("current")
_MidaTDMSpanIndex_Type = Integer32
_MidaTDMSpanIndex_Object = MibTableColumn
midaTDMSpanIndex = _MidaTDMSpanIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 4),
    _MidaTDMSpanIndex_Type()
)
midaTDMSpanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMSpanIndex.setStatus("current")


class _MidaTDMSpanStatus_Type(Integer32):
    """Custom type midaTDMSpanStatus based on Integer32"""
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
        *(("green", 1),
          ("yellow", 2),
          ("red", 3),
          ("blue", 4),
          ("other", 5),
          ("na", 6))
    )


_MidaTDMSpanStatus_Type.__name__ = "Integer32"
_MidaTDMSpanStatus_Object = MibTableColumn
midaTDMSpanStatus = _MidaTDMSpanStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 5),
    _MidaTDMSpanStatus_Type()
)
midaTDMSpanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMSpanStatus.setStatus("current")


class _MidaTDMSpanClockSource_Type(Integer32):
    """Custom type midaTDMSpanClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nt", 1),
          ("te", 2))
    )


_MidaTDMSpanClockSource_Type.__name__ = "Integer32"
_MidaTDMSpanClockSource_Object = MibTableColumn
midaTDMSpanClockSource = _MidaTDMSpanClockSource_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 6),
    _MidaTDMSpanClockSource_Type()
)
midaTDMSpanClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMSpanClockSource.setStatus("current")


class _MidaTDMSpanTapMode_Type(Integer32):
    """Custom type midaTDMSpanTapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hiz", 1),
          ("extz", 2),
          ("none", 3))
    )


_MidaTDMSpanTapMode_Type.__name__ = "Integer32"
_MidaTDMSpanTapMode_Object = MibTableColumn
midaTDMSpanTapMode = _MidaTDMSpanTapMode_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 7),
    _MidaTDMSpanTapMode_Type()
)
midaTDMSpanTapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMSpanTapMode.setStatus("current")
_MidaTDMPortTableRowStatus_Type = RowStatus
_MidaTDMPortTableRowStatus_Object = MibTableColumn
midaTDMPortTableRowStatus = _MidaTDMPortTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 4, 1, 8),
    _MidaTDMPortTableRowStatus_Type()
)
midaTDMPortTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaTDMPortTableRowStatus.setStatus("current")
_MidaEMBoardPortTable_Object = MibTable
midaEMBoardPortTable = _MidaEMBoardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5)
)
if mibBuilder.loadTexts:
    midaEMBoardPortTable.setStatus("current")
_MidaEMBoardPortTableEntry_Object = MibTableRow
midaEMBoardPortTableEntry = _MidaEMBoardPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1)
)
midaEMBoardPortTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaEMBoardTableIndex"),
)
if mibBuilder.loadTexts:
    midaEMBoardPortTableEntry.setStatus("current")


class _MidaEMBoardTableIndex_Type(Integer32):
    """Custom type midaEMBoardTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaEMBoardTableIndex_Type.__name__ = "Integer32"
_MidaEMBoardTableIndex_Object = MibTableColumn
midaEMBoardTableIndex = _MidaEMBoardTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 1),
    _MidaEMBoardTableIndex_Type()
)
midaEMBoardTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMBoardTableIndex.setStatus("current")
_MidaEMBoardName_Type = DisplayString
_MidaEMBoardName_Object = MibTableColumn
midaEMBoardName = _MidaEMBoardName_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 2),
    _MidaEMBoardName_Type()
)
midaEMBoardName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMBoardName.setStatus("current")
_MidaEMLogicalBoardIndex_Type = Integer32
_MidaEMLogicalBoardIndex_Object = MibTableColumn
midaEMLogicalBoardIndex = _MidaEMLogicalBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 3),
    _MidaEMLogicalBoardIndex_Type()
)
midaEMLogicalBoardIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMLogicalBoardIndex.setStatus("current")
_MidaEMSpanIndex_Type = Integer32
_MidaEMSpanIndex_Object = MibTableColumn
midaEMSpanIndex = _MidaEMSpanIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 4),
    _MidaEMSpanIndex_Type()
)
midaEMSpanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMSpanIndex.setStatus("current")
_MidaEMChannelIndex_Type = Integer32
_MidaEMChannelIndex_Object = MibTableColumn
midaEMChannelIndex = _MidaEMChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 5),
    _MidaEMChannelIndex_Type()
)
midaEMChannelIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMChannelIndex.setStatus("current")


class _MidaEMBoardState_Type(Integer32):
    """Custom type midaEMBoardState based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("onhook", 1),
          ("onhookbusy", 2),
          ("ring", 3),
          ("fault", 4),
          ("initreserved", 5),
          ("reserved", 6),
          ("setupinitiated", 7),
          ("setup", 8),
          ("proceedinginitiated", 9),
          ("proceeding", 10),
          ("progressinitiated", 11),
          ("progress", 12),
          ("alertinitiated", 13),
          ("alert", 14),
          ("connectinitiated", 15),
          ("connect", 16),
          ("disconnectinitiated", 17),
          ("disconnect", 18),
          ("releaseinitiated", 19))
    )


_MidaEMBoardState_Type.__name__ = "Integer32"
_MidaEMBoardState_Object = MibTableColumn
midaEMBoardState = _MidaEMBoardState_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 6),
    _MidaEMBoardState_Type()
)
midaEMBoardState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMBoardState.setStatus("current")
_MidaEMBoardRowStatusTable_Type = RowStatus
_MidaEMBoardRowStatusTable_Object = MibTableColumn
midaEMBoardRowStatusTable = _MidaEMBoardRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 5, 1, 7),
    _MidaEMBoardRowStatusTable_Type()
)
midaEMBoardRowStatusTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaEMBoardRowStatusTable.setStatus("current")


class _MidaRecorderDiskStatus_Type(Integer32):
    """Custom type midaRecorderDiskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaRecorderDiskStatus_Type.__name__ = "Integer32"
_MidaRecorderDiskStatus_Object = MibScalar
midaRecorderDiskStatus = _MidaRecorderDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 6),
    _MidaRecorderDiskStatus_Type()
)
midaRecorderDiskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderDiskStatus.setStatus("current")


class _MidaRecorderBackupStatus_Type(Integer32):
    """Custom type midaRecorderBackupStatus based on Integer32"""
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaRecorderBackupStatus_Type.__name__ = "Integer32"
_MidaRecorderBackupStatus_Object = MibScalar
midaRecorderBackupStatus = _MidaRecorderBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 7),
    _MidaRecorderBackupStatus_Type()
)
midaRecorderBackupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderBackupStatus.setStatus("current")


class _MidaRecorderShareStatus_Type(Integer32):
    """Custom type midaRecorderShareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaRecorderShareStatus_Type.__name__ = "Integer32"
_MidaRecorderShareStatus_Object = MibScalar
midaRecorderShareStatus = _MidaRecorderShareStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 8),
    _MidaRecorderShareStatus_Type()
)
midaRecorderShareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderShareStatus.setStatus("current")
_MidaRecorderSnifferChannelTable_Object = MibTable
midaRecorderSnifferChannelTable = _MidaRecorderSnifferChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9)
)
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTable.setStatus("current")
_MidaRecorderSnifferChannelTableEntry_Object = MibTableRow
midaRecorderSnifferChannelTableEntry = _MidaRecorderSnifferChannelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9, 1)
)
midaRecorderSnifferChannelTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaRecorderSnifferChannelTableIndex"),
)
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTableEntry.setStatus("current")


class _MidaRecorderSnifferChannelTableIndex_Type(Integer32):
    """Custom type midaRecorderSnifferChannelTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaRecorderSnifferChannelTableIndex_Type.__name__ = "Integer32"
_MidaRecorderSnifferChannelTableIndex_Object = MibTableColumn
midaRecorderSnifferChannelTableIndex = _MidaRecorderSnifferChannelTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9, 1, 1),
    _MidaRecorderSnifferChannelTableIndex_Type()
)
midaRecorderSnifferChannelTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTableIndex.setStatus("current")
_MidaRecorderSnifferChannelTableCallParty1_Type = DisplayString
_MidaRecorderSnifferChannelTableCallParty1_Object = MibTableColumn
midaRecorderSnifferChannelTableCallParty1 = _MidaRecorderSnifferChannelTableCallParty1_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9, 1, 2),
    _MidaRecorderSnifferChannelTableCallParty1_Type()
)
midaRecorderSnifferChannelTableCallParty1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTableCallParty1.setStatus("current")
_MidaRecorderSnifferChannelTableCallParty2_Type = DisplayString
_MidaRecorderSnifferChannelTableCallParty2_Object = MibTableColumn
midaRecorderSnifferChannelTableCallParty2 = _MidaRecorderSnifferChannelTableCallParty2_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9, 1, 3),
    _MidaRecorderSnifferChannelTableCallParty2_Type()
)
midaRecorderSnifferChannelTableCallParty2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTableCallParty2.setStatus("current")


class _MidaRecorderSnifferChannelTableStatus_Type(Integer32):
    """Custom type midaRecorderSnifferChannelTableStatus based on Integer32"""
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
        *(("inactive", 1),
          ("active", 2),
          ("warning", 3),
          ("critical", 4),
          ("removed", 5))
    )


_MidaRecorderSnifferChannelTableStatus_Type.__name__ = "Integer32"
_MidaRecorderSnifferChannelTableStatus_Object = MibTableColumn
midaRecorderSnifferChannelTableStatus = _MidaRecorderSnifferChannelTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9, 1, 4),
    _MidaRecorderSnifferChannelTableStatus_Type()
)
midaRecorderSnifferChannelTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTableStatus.setStatus("current")
_MidaRecorderSnifferChannelTableRowStatus_Type = RowStatus
_MidaRecorderSnifferChannelTableRowStatus_Object = MibTableColumn
midaRecorderSnifferChannelTableRowStatus = _MidaRecorderSnifferChannelTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 9, 1, 5),
    _MidaRecorderSnifferChannelTableRowStatus_Type()
)
midaRecorderSnifferChannelTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaRecorderSnifferChannelTableRowStatus.setStatus("current")
_MidaRecorderSnifferActiveRecordings_Type = Integer32
_MidaRecorderSnifferActiveRecordings_Object = MibScalar
midaRecorderSnifferActiveRecordings = _MidaRecorderSnifferActiveRecordings_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 10),
    _MidaRecorderSnifferActiveRecordings_Type()
)
midaRecorderSnifferActiveRecordings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderSnifferActiveRecordings.setStatus("current")
_MidaRecorderSnifferMetadataActiveRecordings_Type = Integer32
_MidaRecorderSnifferMetadataActiveRecordings_Object = MibScalar
midaRecorderSnifferMetadataActiveRecordings = _MidaRecorderSnifferMetadataActiveRecordings_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 11),
    _MidaRecorderSnifferMetadataActiveRecordings_Type()
)
midaRecorderSnifferMetadataActiveRecordings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderSnifferMetadataActiveRecordings.setStatus("current")
_MidaRecorderSnifferConfiguredChannels_Type = Integer32
_MidaRecorderSnifferConfiguredChannels_Object = MibScalar
midaRecorderSnifferConfiguredChannels = _MidaRecorderSnifferConfiguredChannels_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 12),
    _MidaRecorderSnifferConfiguredChannels_Type()
)
midaRecorderSnifferConfiguredChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderSnifferConfiguredChannels.setStatus("current")


class _MidaVoipRecorderProxyServiceStatus_Type(Integer32):
    """Custom type midaVoipRecorderProxyServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaVoipRecorderProxyServiceStatus_Type.__name__ = "Integer32"
_MidaVoipRecorderProxyServiceStatus_Object = MibScalar
midaVoipRecorderProxyServiceStatus = _MidaVoipRecorderProxyServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 13),
    _MidaVoipRecorderProxyServiceStatus_Type()
)
midaVoipRecorderProxyServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderProxyServiceStatus.setStatus("current")
_MidaVoipRecorderProxySessions_Type = Integer32
_MidaVoipRecorderProxySessions_Object = MibScalar
midaVoipRecorderProxySessions = _MidaVoipRecorderProxySessions_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 14),
    _MidaVoipRecorderProxySessions_Type()
)
midaVoipRecorderProxySessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderProxySessions.setStatus("current")
_MidaVoipRecorderProxyActiveCalls_Type = Integer32
_MidaVoipRecorderProxyActiveCalls_Object = MibScalar
midaVoipRecorderProxyActiveCalls = _MidaVoipRecorderProxyActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 15),
    _MidaVoipRecorderProxyActiveCalls_Type()
)
midaVoipRecorderProxyActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderProxyActiveCalls.setStatus("current")
_MidaVoipRecorderProxyTotalCalls_Type = Integer32
_MidaVoipRecorderProxyTotalCalls_Object = MibScalar
midaVoipRecorderProxyTotalCalls = _MidaVoipRecorderProxyTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 16),
    _MidaVoipRecorderProxyTotalCalls_Type()
)
midaVoipRecorderProxyTotalCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderProxyTotalCalls.setStatus("current")
_MidaVoipRecorderActvityTable_Object = MibTable
midaVoipRecorderActvityTable = _MidaVoipRecorderActvityTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17)
)
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTable.setStatus("current")
_MidaVoipRecorderActvityTableEntry_Object = MibTableRow
midaVoipRecorderActvityTableEntry = _MidaVoipRecorderActvityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1)
)
midaVoipRecorderActvityTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaVoipRecorderActvityTableIndex"),
)
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableEntry.setStatus("current")


class _MidaVoipRecorderActvityTableIndex_Type(Integer32):
    """Custom type midaVoipRecorderActvityTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaVoipRecorderActvityTableIndex_Type.__name__ = "Integer32"
_MidaVoipRecorderActvityTableIndex_Object = MibTableColumn
midaVoipRecorderActvityTableIndex = _MidaVoipRecorderActvityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 1),
    _MidaVoipRecorderActvityTableIndex_Type()
)
midaVoipRecorderActvityTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableIndex.setStatus("current")
_MidaVoipRecorderActvityTableInstanceNumber_Type = Integer32
_MidaVoipRecorderActvityTableInstanceNumber_Object = MibTableColumn
midaVoipRecorderActvityTableInstanceNumber = _MidaVoipRecorderActvityTableInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 2),
    _MidaVoipRecorderActvityTableInstanceNumber_Type()
)
midaVoipRecorderActvityTableInstanceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableInstanceNumber.setStatus("current")
_MidaVoipRecorderActvityTableActiveSessions_Type = Integer32
_MidaVoipRecorderActvityTableActiveSessions_Object = MibTableColumn
midaVoipRecorderActvityTableActiveSessions = _MidaVoipRecorderActvityTableActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 3),
    _MidaVoipRecorderActvityTableActiveSessions_Type()
)
midaVoipRecorderActvityTableActiveSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableActiveSessions.setStatus("current")
_MidaVoipRecorderActvityTableRefusedSessions_Type = Integer32
_MidaVoipRecorderActvityTableRefusedSessions_Object = MibTableColumn
midaVoipRecorderActvityTableRefusedSessions = _MidaVoipRecorderActvityTableRefusedSessions_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 4),
    _MidaVoipRecorderActvityTableRefusedSessions_Type()
)
midaVoipRecorderActvityTableRefusedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableRefusedSessions.setStatus("current")
_MidaVoipRecorderActvityTableActiveCalls_Type = Integer32
_MidaVoipRecorderActvityTableActiveCalls_Object = MibTableColumn
midaVoipRecorderActvityTableActiveCalls = _MidaVoipRecorderActvityTableActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 5),
    _MidaVoipRecorderActvityTableActiveCalls_Type()
)
midaVoipRecorderActvityTableActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableActiveCalls.setStatus("current")
_MidaVoipRecorderActvityTableTotalCalls_Type = Integer32
_MidaVoipRecorderActvityTableTotalCalls_Object = MibTableColumn
midaVoipRecorderActvityTableTotalCalls = _MidaVoipRecorderActvityTableTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 6),
    _MidaVoipRecorderActvityTableTotalCalls_Type()
)
midaVoipRecorderActvityTableTotalCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableTotalCalls.setStatus("current")
_MidaVoipRecorderActvityTableRowStatus_Type = RowStatus
_MidaVoipRecorderActvityTableRowStatus_Object = MibTableColumn
midaVoipRecorderActvityTableRowStatus = _MidaVoipRecorderActvityTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 17, 1, 7),
    _MidaVoipRecorderActvityTableRowStatus_Type()
)
midaVoipRecorderActvityTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoipRecorderActvityTableRowStatus.setStatus("current")


class _MidaDRLinkServiceStatus_Type(Integer32):
    """Custom type midaDRLinkServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaDRLinkServiceStatus_Type.__name__ = "Integer32"
_MidaDRLinkServiceStatus_Object = MibScalar
midaDRLinkServiceStatus = _MidaDRLinkServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 18),
    _MidaDRLinkServiceStatus_Type()
)
midaDRLinkServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaDRLinkServiceStatus.setStatus("current")


class _MidaDRLinkRTPEngineServiceStatus_Type(Integer32):
    """Custom type midaDRLinkRTPEngineServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaDRLinkRTPEngineServiceStatus_Type.__name__ = "Integer32"
_MidaDRLinkRTPEngineServiceStatus_Object = MibScalar
midaDRLinkRTPEngineServiceStatus = _MidaDRLinkRTPEngineServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 19),
    _MidaDRLinkRTPEngineServiceStatus_Type()
)
midaDRLinkRTPEngineServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaDRLinkRTPEngineServiceStatus.setStatus("current")


class _MidaDRLinkSlowEvents_Type(Integer32):
    """Custom type midaDRLinkSlowEvents based on Integer32"""
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaDRLinkSlowEvents_Type.__name__ = "Integer32"
_MidaDRLinkSlowEvents_Object = MibScalar
midaDRLinkSlowEvents = _MidaDRLinkSlowEvents_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 20),
    _MidaDRLinkSlowEvents_Type()
)
midaDRLinkSlowEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaDRLinkSlowEvents.setStatus("current")


class _MidaDRLinkNoChannelAvailable_Type(Integer32):
    """Custom type midaDRLinkNoChannelAvailable based on Integer32"""
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
        *(("normal", 1),
          ("warning", 2),
          ("critical", 3),
          ("disabled", 4))
    )


_MidaDRLinkNoChannelAvailable_Type.__name__ = "Integer32"
_MidaDRLinkNoChannelAvailable_Object = MibScalar
midaDRLinkNoChannelAvailable = _MidaDRLinkNoChannelAvailable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 21),
    _MidaDRLinkNoChannelAvailable_Type()
)
midaDRLinkNoChannelAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaDRLinkNoChannelAvailable.setStatus("current")
_MidaDRLinkTSAPIServerTable_Object = MibTable
midaDRLinkTSAPIServerTable = _MidaDRLinkTSAPIServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22)
)
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTable.setStatus("current")
_MidaDRLinkTSAPIServerTableEntry_Object = MibTableRow
midaDRLinkTSAPIServerTableEntry = _MidaDRLinkTSAPIServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1)
)
midaDRLinkTSAPIServerTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaDRLinkTSAPIServerTableIndex"),
)
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTableEntry.setStatus("current")


class _MidaDRLinkTSAPIServerTableIndex_Type(Integer32):
    """Custom type midaDRLinkTSAPIServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaDRLinkTSAPIServerTableIndex_Type.__name__ = "Integer32"
_MidaDRLinkTSAPIServerTableIndex_Object = MibTableColumn
midaDRLinkTSAPIServerTableIndex = _MidaDRLinkTSAPIServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1, 1),
    _MidaDRLinkTSAPIServerTableIndex_Type()
)
midaDRLinkTSAPIServerTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTableIndex.setStatus("current")
_MidaDRLinkTSAPIServerTableServer_Type = DisplayString
_MidaDRLinkTSAPIServerTableServer_Object = MibTableColumn
midaDRLinkTSAPIServerTableServer = _MidaDRLinkTSAPIServerTableServer_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1, 2),
    _MidaDRLinkTSAPIServerTableServer_Type()
)
midaDRLinkTSAPIServerTableServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTableServer.setStatus("current")


class _MidaDRLinkTSAPIServerTablePort_Type(Integer32):
    """Custom type midaDRLinkTSAPIServerTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaDRLinkTSAPIServerTablePort_Type.__name__ = "Integer32"
_MidaDRLinkTSAPIServerTablePort_Object = MibTableColumn
midaDRLinkTSAPIServerTablePort = _MidaDRLinkTSAPIServerTablePort_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1, 3),
    _MidaDRLinkTSAPIServerTablePort_Type()
)
midaDRLinkTSAPIServerTablePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTablePort.setStatus("current")
_MidaDRLinkTSAPIServerTableLink_Type = DisplayString
_MidaDRLinkTSAPIServerTableLink_Object = MibTableColumn
midaDRLinkTSAPIServerTableLink = _MidaDRLinkTSAPIServerTableLink_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1, 4),
    _MidaDRLinkTSAPIServerTableLink_Type()
)
midaDRLinkTSAPIServerTableLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTableLink.setStatus("current")


class _MidaDRLinkTSAPIServerTableStatus_Type(Integer32):
    """Custom type midaDRLinkTSAPIServerTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("connected", 1),
          ("escaped", 2),
          ("monitored", 3),
          ("tsapiFailed", 4),
          ("oxeFailed", 5))
    )


_MidaDRLinkTSAPIServerTableStatus_Type.__name__ = "Integer32"
_MidaDRLinkTSAPIServerTableStatus_Object = MibTableColumn
midaDRLinkTSAPIServerTableStatus = _MidaDRLinkTSAPIServerTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1, 5),
    _MidaDRLinkTSAPIServerTableStatus_Type()
)
midaDRLinkTSAPIServerTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTableStatus.setStatus("current")
_MidaDRLinkTSAPIServerTableRowStatus_Type = RowStatus
_MidaDRLinkTSAPIServerTableRowStatus_Object = MibTableColumn
midaDRLinkTSAPIServerTableRowStatus = _MidaDRLinkTSAPIServerTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 22, 1, 6),
    _MidaDRLinkTSAPIServerTableRowStatus_Type()
)
midaDRLinkTSAPIServerTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTSAPIServerTableRowStatus.setStatus("current")
_MidaDRLinkDevicesTable_Object = MibTable
midaDRLinkDevicesTable = _MidaDRLinkDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23)
)
if mibBuilder.loadTexts:
    midaDRLinkDevicesTable.setStatus("current")
_MidaDRLinkDevicesTableEntry_Object = MibTableRow
midaDRLinkDevicesTableEntry = _MidaDRLinkDevicesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1)
)
midaDRLinkDevicesTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaDRLinkDevicesTableIndex"),
)
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableEntry.setStatus("current")


class _MidaDRLinkDevicesTableIndex_Type(Integer32):
    """Custom type midaDRLinkDevicesTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaDRLinkDevicesTableIndex_Type.__name__ = "Integer32"
_MidaDRLinkDevicesTableIndex_Object = MibTableColumn
midaDRLinkDevicesTableIndex = _MidaDRLinkDevicesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 1),
    _MidaDRLinkDevicesTableIndex_Type()
)
midaDRLinkDevicesTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableIndex.setStatus("current")
_MidaDRLinkDevicesTableTSAPIServerIndex_Type = Integer32
_MidaDRLinkDevicesTableTSAPIServerIndex_Object = MibTableColumn
midaDRLinkDevicesTableTSAPIServerIndex = _MidaDRLinkDevicesTableTSAPIServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 2),
    _MidaDRLinkDevicesTableTSAPIServerIndex_Type()
)
midaDRLinkDevicesTableTSAPIServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableTSAPIServerIndex.setStatus("current")
_MidaDRLinkDevicesTableDevice_Type = DisplayString
_MidaDRLinkDevicesTableDevice_Object = MibTableColumn
midaDRLinkDevicesTableDevice = _MidaDRLinkDevicesTableDevice_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 3),
    _MidaDRLinkDevicesTableDevice_Type()
)
midaDRLinkDevicesTableDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableDevice.setStatus("current")
_MidaDRLinkDevicesTableParty2_Type = DisplayString
_MidaDRLinkDevicesTableParty2_Object = MibTableColumn
midaDRLinkDevicesTableParty2 = _MidaDRLinkDevicesTableParty2_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 4),
    _MidaDRLinkDevicesTableParty2_Type()
)
midaDRLinkDevicesTableParty2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableParty2.setStatus("current")
_MidaDRLinkDevicesTableParticipants_Type = DisplayString
_MidaDRLinkDevicesTableParticipants_Object = MibTableColumn
midaDRLinkDevicesTableParticipants = _MidaDRLinkDevicesTableParticipants_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 5),
    _MidaDRLinkDevicesTableParticipants_Type()
)
midaDRLinkDevicesTableParticipants.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableParticipants.setStatus("current")
_MidaDRLinkDevicesTableCallId_Type = DisplayString
_MidaDRLinkDevicesTableCallId_Object = MibTableColumn
midaDRLinkDevicesTableCallId = _MidaDRLinkDevicesTableCallId_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 6),
    _MidaDRLinkDevicesTableCallId_Type()
)
midaDRLinkDevicesTableCallId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableCallId.setStatus("current")


class _MidaDRLinkDevicesTableType_Type(Integer32):
    """Custom type midaDRLinkDevicesTableType based on Integer32"""
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
        *(("none", 0),
          ("incoming", 1),
          ("outgoing", 2),
          ("conference", 3))
    )


_MidaDRLinkDevicesTableType_Type.__name__ = "Integer32"
_MidaDRLinkDevicesTableType_Object = MibTableColumn
midaDRLinkDevicesTableType = _MidaDRLinkDevicesTableType_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 7),
    _MidaDRLinkDevicesTableType_Type()
)
midaDRLinkDevicesTableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableType.setStatus("current")


class _MidaDRLinkDevicesTableStatus_Type(Integer32):
    """Custom type midaDRLinkDevicesTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("monitoredFailed", 1),
          ("monitored", 2),
          ("inCalling", 3),
          ("recording", 4))
    )


_MidaDRLinkDevicesTableStatus_Type.__name__ = "Integer32"
_MidaDRLinkDevicesTableStatus_Object = MibTableColumn
midaDRLinkDevicesTableStatus = _MidaDRLinkDevicesTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 8),
    _MidaDRLinkDevicesTableStatus_Type()
)
midaDRLinkDevicesTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableStatus.setStatus("current")
_MidaDRLinkDevicesTableRowStatus_Type = RowStatus
_MidaDRLinkDevicesTableRowStatus_Object = MibTableColumn
midaDRLinkDevicesTableRowStatus = _MidaDRLinkDevicesTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 23, 1, 9),
    _MidaDRLinkDevicesTableRowStatus_Type()
)
midaDRLinkDevicesTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkDevicesTableRowStatus.setStatus("current")
_MidaDRLinkTDMServerTable_Object = MibTable
midaDRLinkTDMServerTable = _MidaDRLinkTDMServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 24)
)
if mibBuilder.loadTexts:
    midaDRLinkTDMServerTable.setStatus("current")
_MidaDRLinkTDMServerTableEntry_Object = MibTableRow
midaDRLinkTDMServerTableEntry = _MidaDRLinkTDMServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 24, 1)
)
midaDRLinkTDMServerTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaDRLinkTDMServerTableIndex"),
)
if mibBuilder.loadTexts:
    midaDRLinkTDMServerTableEntry.setStatus("current")


class _MidaDRLinkTDMServerTableIndex_Type(Integer32):
    """Custom type midaDRLinkTDMServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaDRLinkTDMServerTableIndex_Type.__name__ = "Integer32"
_MidaDRLinkTDMServerTableIndex_Object = MibTableColumn
midaDRLinkTDMServerTableIndex = _MidaDRLinkTDMServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 24, 1, 1),
    _MidaDRLinkTDMServerTableIndex_Type()
)
midaDRLinkTDMServerTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMServerTableIndex.setStatus("current")
_MidaDRLinkTDMServerTableServer_Type = DisplayString
_MidaDRLinkTDMServerTableServer_Object = MibTableColumn
midaDRLinkTDMServerTableServer = _MidaDRLinkTDMServerTableServer_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 24, 1, 2),
    _MidaDRLinkTDMServerTableServer_Type()
)
midaDRLinkTDMServerTableServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMServerTableServer.setStatus("current")


class _MidaDRLinkTDMServerTableStatus_Type(Integer32):
    """Custom type midaDRLinkTDMServerTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1),
          ("authenticated", 2))
    )


_MidaDRLinkTDMServerTableStatus_Type.__name__ = "Integer32"
_MidaDRLinkTDMServerTableStatus_Object = MibTableColumn
midaDRLinkTDMServerTableStatus = _MidaDRLinkTDMServerTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 24, 1, 3),
    _MidaDRLinkTDMServerTableStatus_Type()
)
midaDRLinkTDMServerTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMServerTableStatus.setStatus("current")
_MidaDRLinkTDMServerTableRowStatus_Type = RowStatus
_MidaDRLinkTDMServerTableRowStatus_Object = MibTableColumn
midaDRLinkTDMServerTableRowStatus = _MidaDRLinkTDMServerTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 24, 1, 4),
    _MidaDRLinkTDMServerTableRowStatus_Type()
)
midaDRLinkTDMServerTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMServerTableRowStatus.setStatus("current")
_MidaDRLinkTDMConnectionTable_Object = MibTable
midaDRLinkTDMConnectionTable = _MidaDRLinkTDMConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25)
)
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTable.setStatus("current")
_MidaDRLinkTDMConnectionTableEntry_Object = MibTableRow
midaDRLinkTDMConnectionTableEntry = _MidaDRLinkTDMConnectionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1)
)
midaDRLinkTDMConnectionTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaDRLinkTDMConnectionTableIndex"),
)
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableEntry.setStatus("current")


class _MidaDRLinkTDMConnectionTableIndex_Type(Integer32):
    """Custom type midaDRLinkTDMConnectionTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaDRLinkTDMConnectionTableIndex_Type.__name__ = "Integer32"
_MidaDRLinkTDMConnectionTableIndex_Object = MibTableColumn
midaDRLinkTDMConnectionTableIndex = _MidaDRLinkTDMConnectionTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 1),
    _MidaDRLinkTDMConnectionTableIndex_Type()
)
midaDRLinkTDMConnectionTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableIndex.setStatus("current")
_MidaDRLinkTDMConnectionTableTSAPIServerIndex_Type = Integer32
_MidaDRLinkTDMConnectionTableTSAPIServerIndex_Object = MibTableColumn
midaDRLinkTDMConnectionTableTSAPIServerIndex = _MidaDRLinkTDMConnectionTableTSAPIServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 2),
    _MidaDRLinkTDMConnectionTableTSAPIServerIndex_Type()
)
midaDRLinkTDMConnectionTableTSAPIServerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableTSAPIServerIndex.setStatus("current")
_MidaDRLinkTDMConnectionTablePcmCrystal_Type = Integer32
_MidaDRLinkTDMConnectionTablePcmCrystal_Object = MibTableColumn
midaDRLinkTDMConnectionTablePcmCrystal = _MidaDRLinkTDMConnectionTablePcmCrystal_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 3),
    _MidaDRLinkTDMConnectionTablePcmCrystal_Type()
)
midaDRLinkTDMConnectionTablePcmCrystal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTablePcmCrystal.setStatus("current")
_MidaDRLinkTDMConnectionTablePcmCoupler_Type = Integer32
_MidaDRLinkTDMConnectionTablePcmCoupler_Object = MibTableColumn
midaDRLinkTDMConnectionTablePcmCoupler = _MidaDRLinkTDMConnectionTablePcmCoupler_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 4),
    _MidaDRLinkTDMConnectionTablePcmCoupler_Type()
)
midaDRLinkTDMConnectionTablePcmCoupler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTablePcmCoupler.setStatus("current")
_MidaDRLinkTDMConnectionTablePCMTimeslot_Type = Integer32
_MidaDRLinkTDMConnectionTablePCMTimeslot_Object = MibTableColumn
midaDRLinkTDMConnectionTablePCMTimeslot = _MidaDRLinkTDMConnectionTablePCMTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 5),
    _MidaDRLinkTDMConnectionTablePCMTimeslot_Type()
)
midaDRLinkTDMConnectionTablePCMTimeslot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTablePCMTimeslot.setStatus("current")
_MidaDRLinkTDMConnectionTableBoard_Type = Integer32
_MidaDRLinkTDMConnectionTableBoard_Object = MibTableColumn
midaDRLinkTDMConnectionTableBoard = _MidaDRLinkTDMConnectionTableBoard_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 6),
    _MidaDRLinkTDMConnectionTableBoard_Type()
)
midaDRLinkTDMConnectionTableBoard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableBoard.setStatus("current")
_MidaDRLinkTDMConnectionTableSpan_Type = Integer32
_MidaDRLinkTDMConnectionTableSpan_Object = MibTableColumn
midaDRLinkTDMConnectionTableSpan = _MidaDRLinkTDMConnectionTableSpan_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 7),
    _MidaDRLinkTDMConnectionTableSpan_Type()
)
midaDRLinkTDMConnectionTableSpan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableSpan.setStatus("current")
_MidaDRLinkTDMConnectionTableChannel_Type = Integer32
_MidaDRLinkTDMConnectionTableChannel_Object = MibTableColumn
midaDRLinkTDMConnectionTableChannel = _MidaDRLinkTDMConnectionTableChannel_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 8),
    _MidaDRLinkTDMConnectionTableChannel_Type()
)
midaDRLinkTDMConnectionTableChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableChannel.setStatus("current")


class _MidaDRLinkTDMConnectionTableStatus_Type(Integer32):
    """Custom type midaDRLinkTDMConnectionTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("free", 0),
          ("busy", 1))
    )


_MidaDRLinkTDMConnectionTableStatus_Type.__name__ = "Integer32"
_MidaDRLinkTDMConnectionTableStatus_Object = MibTableColumn
midaDRLinkTDMConnectionTableStatus = _MidaDRLinkTDMConnectionTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 9),
    _MidaDRLinkTDMConnectionTableStatus_Type()
)
midaDRLinkTDMConnectionTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableStatus.setStatus("current")
_MidaDRLinkTDMConnectionTableRowStatus_Type = RowStatus
_MidaDRLinkTDMConnectionTableRowStatus_Object = MibTableColumn
midaDRLinkTDMConnectionTableRowStatus = _MidaDRLinkTDMConnectionTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 25, 1, 10),
    _MidaDRLinkTDMConnectionTableRowStatus_Type()
)
midaDRLinkTDMConnectionTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaDRLinkTDMConnectionTableRowStatus.setStatus("current")


class _MidaRecorderErlangUsage_Type(DisplayString):
    """Custom type midaRecorderErlangUsage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MidaRecorderErlangUsage_Type.__name__ = "DisplayString"
_MidaRecorderErlangUsage_Object = MibScalar
midaRecorderErlangUsage = _MidaRecorderErlangUsage_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 5, 26),
    _MidaRecorderErlangUsage_Type()
)
midaRecorderErlangUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaRecorderErlangUsage.setStatus("current")
_MidaScheduler_ObjectIdentity = ObjectIdentity
midaScheduler = _MidaScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 6)
)


class _MidaSchedulerServiceStatus_Type(Integer32):
    """Custom type midaSchedulerServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("notrunning", 2),
          ("disabled", 3))
    )


_MidaSchedulerServiceStatus_Type.__name__ = "Integer32"
_MidaSchedulerServiceStatus_Object = MibScalar
midaSchedulerServiceStatus = _MidaSchedulerServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 6, 1),
    _MidaSchedulerServiceStatus_Type()
)
midaSchedulerServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaSchedulerServiceStatus.setStatus("current")
_MidaVoiceServices_ObjectIdentity = ObjectIdentity
midaVoiceServices = _MidaVoiceServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7)
)
_MidaVoiceServicesActiveCalls_Type = Integer32
_MidaVoiceServicesActiveCalls_Object = MibScalar
midaVoiceServicesActiveCalls = _MidaVoiceServicesActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 1),
    _MidaVoiceServicesActiveCalls_Type()
)
midaVoiceServicesActiveCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    midaVoiceServicesActiveCalls.setStatus("current")
_MidaQMTable_Object = MibTable
midaQMTable = _MidaQMTable_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2)
)
if mibBuilder.loadTexts:
    midaQMTable.setStatus("current")
_MidaQMTableEntry_Object = MibTableRow
midaQMTableEntry = _MidaQMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1)
)
midaQMTableEntry.setIndexNames(
    (0, "MIDASOLUTIONS-MIB", "midaQMTableIndex"),
)
if mibBuilder.loadTexts:
    midaQMTableEntry.setStatus("current")


class _MidaQMTableIndex_Type(Integer32):
    """Custom type midaQMTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MidaQMTableIndex_Type.__name__ = "Integer32"
_MidaQMTableIndex_Object = MibTableColumn
midaQMTableIndex = _MidaQMTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 1),
    _MidaQMTableIndex_Type()
)
midaQMTableIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMTableIndex.setStatus("current")


class _MidaQMServiceStatus_Type(Integer32):
    """Custom type midaQMServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_MidaQMServiceStatus_Type.__name__ = "Integer32"
_MidaQMServiceStatus_Object = MibTableColumn
midaQMServiceStatus = _MidaQMServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 2),
    _MidaQMServiceStatus_Type()
)
midaQMServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMServiceStatus.setStatus("current")
_MidaQMServiceName_Type = DisplayString
_MidaQMServiceName_Object = MibTableColumn
midaQMServiceName = _MidaQMServiceName_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 3),
    _MidaQMServiceName_Type()
)
midaQMServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMServiceName.setStatus("current")
_MidaQMServiceNumber_Type = DisplayString
_MidaQMServiceNumber_Object = MibTableColumn
midaQMServiceNumber = _MidaQMServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 4),
    _MidaQMServiceNumber_Type()
)
midaQMServiceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMServiceNumber.setStatus("current")
_MidaQMServiceSupervisors_Type = Integer32
_MidaQMServiceSupervisors_Object = MibTableColumn
midaQMServiceSupervisors = _MidaQMServiceSupervisors_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 5),
    _MidaQMServiceSupervisors_Type()
)
midaQMServiceSupervisors.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMServiceSupervisors.setStatus("current")
_MidaQMServiceAgents_Type = Integer32
_MidaQMServiceAgents_Object = MibTableColumn
midaQMServiceAgents = _MidaQMServiceAgents_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 6),
    _MidaQMServiceAgents_Type()
)
midaQMServiceAgents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMServiceAgents.setStatus("current")
_MidaQMServiceLoggedAgents_Type = Integer32
_MidaQMServiceLoggedAgents_Object = MibTableColumn
midaQMServiceLoggedAgents = _MidaQMServiceLoggedAgents_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 7),
    _MidaQMServiceLoggedAgents_Type()
)
midaQMServiceLoggedAgents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMServiceLoggedAgents.setStatus("current")
_MidaQMTableRowStatus_Type = RowStatus
_MidaQMTableRowStatus_Object = MibTableColumn
midaQMTableRowStatus = _MidaQMTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45506, 1, 7, 2, 1, 8),
    _MidaQMTableRowStatus_Type()
)
midaQMTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    midaQMTableRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIDASOLUTIONS-MIB",
    **{"midasolutions": midasolutions,
       "midaApplications": midaApplications,
       "midaPlatform": midaPlatform,
       "midaApplicationServerStatus": midaApplicationServerStatus,
       "midaControlPanelServiceStatus": midaControlPanelServiceStatus,
       "midaGWControlPanelServiceStatus": midaGWControlPanelServiceStatus,
       "midaSIPServiceStatus": midaSIPServiceStatus,
       "midaCTIManagerServiceStatus": midaCTIManagerServiceStatus,
       "midaSambaServiceStatus": midaSambaServiceStatus,
       "midaGlusterServiceStatus": midaGlusterServiceStatus,
       "midaBucardoServiceStatus": midaBucardoServiceStatus,
       "midaFTPServiceStatus": midaFTPServiceStatus,
       "midaDatabaseConnectionStatus": midaDatabaseConnectionStatus,
       "midaBilling": midaBilling,
       "midaBillingServiceStatus": midaBillingServiceStatus,
       "midaBillingLastCDRProcessed": midaBillingLastCDRProcessed,
       "midaFaxServer": midaFaxServer,
       "midaFaxServiceStatus": midaFaxServiceStatus,
       "midaFaxNotificationServiceStatus": midaFaxNotificationServiceStatus,
       "midaFaxSendingReceiving": midaFaxSendingReceiving,
       "midaFaxFaxQueued": midaFaxFaxQueued,
       "midaFaxMail2FaxStatus": midaFaxMail2FaxStatus,
       "midaFaxChannelStatus": midaFaxChannelStatus,
       "midaFaxChannelTable": midaFaxChannelTable,
       "midaFaxChannelTableEntry": midaFaxChannelTableEntry,
       "midaFaxChannelTableChannelIndex": midaFaxChannelTableChannelIndex,
       "midaFaxChannelTableChannelStatus": midaFaxChannelTableChannelStatus,
       "midaFaxChannelTableRowStatus": midaFaxChannelTableRowStatus,
       "midaFaxLastReceivedTs": midaFaxLastReceivedTs,
       "midaFaxLastSentTs": midaFaxLastSentTs,
       "midaFaxLastConversionTs": midaFaxLastConversionTs,
       "midaFaxLastArchivedTs": midaFaxLastArchivedTs,
       "midaFaxProcessingTime": midaFaxProcessingTime,
       "midaFaxLastMissingAcquisitionReportTs": midaFaxLastMissingAcquisitionReportTs,
       "midaImportManager": midaImportManager,
       "midaImportManagerServiceStatus": midaImportManagerServiceStatus,
       "midaImportManagerTable": midaImportManagerTable,
       "midaImportManagerTableEntry": midaImportManagerTableEntry,
       "midaImportManagerTableType": midaImportManagerTableType,
       "midaImportManagerTableLastImport": midaImportManagerTableLastImport,
       "midaImportManagerTableRowStatus": midaImportManagerTableRowStatus,
       "midaRecorder": midaRecorder,
       "midaRecorderSnifferServiceStatus": midaRecorderSnifferServiceStatus,
       "midaVoipRecorderServiceStatus": midaVoipRecorderServiceStatus,
       "midaRecorderCollectorsTable": midaRecorderCollectorsTable,
       "midaRecorderCollectorsTableEntry": midaRecorderCollectorsTableEntry,
       "midaRecorderCollectorsTableIndex": midaRecorderCollectorsTableIndex,
       "midaRecorderCollectorsTableChannelSource": midaRecorderCollectorsTableChannelSource,
       "midaRecorderCollectorsTableIPAddress": midaRecorderCollectorsTableIPAddress,
       "midaRecorderCollectorsTableDownloaded": midaRecorderCollectorsTableDownloaded,
       "midaRecorderCollectorsTableStatus": midaRecorderCollectorsTableStatus,
       "midaRecorderCollectorsTableLastRun": midaRecorderCollectorsTableLastRun,
       "midaRecorderCollectorsTableRowStatus": midaRecorderCollectorsTableRowStatus,
       "midaTDMPortTable": midaTDMPortTable,
       "midaTDMPortTableEntry": midaTDMPortTableEntry,
       "midaTDMPortTableIndex": midaTDMPortTableIndex,
       "midaTDMBoardName": midaTDMBoardName,
       "midaTDMBoardLogicalIndex": midaTDMBoardLogicalIndex,
       "midaTDMSpanIndex": midaTDMSpanIndex,
       "midaTDMSpanStatus": midaTDMSpanStatus,
       "midaTDMSpanClockSource": midaTDMSpanClockSource,
       "midaTDMSpanTapMode": midaTDMSpanTapMode,
       "midaTDMPortTableRowStatus": midaTDMPortTableRowStatus,
       "midaEMBoardPortTable": midaEMBoardPortTable,
       "midaEMBoardPortTableEntry": midaEMBoardPortTableEntry,
       "midaEMBoardTableIndex": midaEMBoardTableIndex,
       "midaEMBoardName": midaEMBoardName,
       "midaEMLogicalBoardIndex": midaEMLogicalBoardIndex,
       "midaEMSpanIndex": midaEMSpanIndex,
       "midaEMChannelIndex": midaEMChannelIndex,
       "midaEMBoardState": midaEMBoardState,
       "midaEMBoardRowStatusTable": midaEMBoardRowStatusTable,
       "midaRecorderDiskStatus": midaRecorderDiskStatus,
       "midaRecorderBackupStatus": midaRecorderBackupStatus,
       "midaRecorderShareStatus": midaRecorderShareStatus,
       "midaRecorderSnifferChannelTable": midaRecorderSnifferChannelTable,
       "midaRecorderSnifferChannelTableEntry": midaRecorderSnifferChannelTableEntry,
       "midaRecorderSnifferChannelTableIndex": midaRecorderSnifferChannelTableIndex,
       "midaRecorderSnifferChannelTableCallParty1": midaRecorderSnifferChannelTableCallParty1,
       "midaRecorderSnifferChannelTableCallParty2": midaRecorderSnifferChannelTableCallParty2,
       "midaRecorderSnifferChannelTableStatus": midaRecorderSnifferChannelTableStatus,
       "midaRecorderSnifferChannelTableRowStatus": midaRecorderSnifferChannelTableRowStatus,
       "midaRecorderSnifferActiveRecordings": midaRecorderSnifferActiveRecordings,
       "midaRecorderSnifferMetadataActiveRecordings": midaRecorderSnifferMetadataActiveRecordings,
       "midaRecorderSnifferConfiguredChannels": midaRecorderSnifferConfiguredChannels,
       "midaVoipRecorderProxyServiceStatus": midaVoipRecorderProxyServiceStatus,
       "midaVoipRecorderProxySessions": midaVoipRecorderProxySessions,
       "midaVoipRecorderProxyActiveCalls": midaVoipRecorderProxyActiveCalls,
       "midaVoipRecorderProxyTotalCalls": midaVoipRecorderProxyTotalCalls,
       "midaVoipRecorderActvityTable": midaVoipRecorderActvityTable,
       "midaVoipRecorderActvityTableEntry": midaVoipRecorderActvityTableEntry,
       "midaVoipRecorderActvityTableIndex": midaVoipRecorderActvityTableIndex,
       "midaVoipRecorderActvityTableInstanceNumber": midaVoipRecorderActvityTableInstanceNumber,
       "midaVoipRecorderActvityTableActiveSessions": midaVoipRecorderActvityTableActiveSessions,
       "midaVoipRecorderActvityTableRefusedSessions": midaVoipRecorderActvityTableRefusedSessions,
       "midaVoipRecorderActvityTableActiveCalls": midaVoipRecorderActvityTableActiveCalls,
       "midaVoipRecorderActvityTableTotalCalls": midaVoipRecorderActvityTableTotalCalls,
       "midaVoipRecorderActvityTableRowStatus": midaVoipRecorderActvityTableRowStatus,
       "midaDRLinkServiceStatus": midaDRLinkServiceStatus,
       "midaDRLinkRTPEngineServiceStatus": midaDRLinkRTPEngineServiceStatus,
       "midaDRLinkSlowEvents": midaDRLinkSlowEvents,
       "midaDRLinkNoChannelAvailable": midaDRLinkNoChannelAvailable,
       "midaDRLinkTSAPIServerTable": midaDRLinkTSAPIServerTable,
       "midaDRLinkTSAPIServerTableEntry": midaDRLinkTSAPIServerTableEntry,
       "midaDRLinkTSAPIServerTableIndex": midaDRLinkTSAPIServerTableIndex,
       "midaDRLinkTSAPIServerTableServer": midaDRLinkTSAPIServerTableServer,
       "midaDRLinkTSAPIServerTablePort": midaDRLinkTSAPIServerTablePort,
       "midaDRLinkTSAPIServerTableLink": midaDRLinkTSAPIServerTableLink,
       "midaDRLinkTSAPIServerTableStatus": midaDRLinkTSAPIServerTableStatus,
       "midaDRLinkTSAPIServerTableRowStatus": midaDRLinkTSAPIServerTableRowStatus,
       "midaDRLinkDevicesTable": midaDRLinkDevicesTable,
       "midaDRLinkDevicesTableEntry": midaDRLinkDevicesTableEntry,
       "midaDRLinkDevicesTableIndex": midaDRLinkDevicesTableIndex,
       "midaDRLinkDevicesTableTSAPIServerIndex": midaDRLinkDevicesTableTSAPIServerIndex,
       "midaDRLinkDevicesTableDevice": midaDRLinkDevicesTableDevice,
       "midaDRLinkDevicesTableParty2": midaDRLinkDevicesTableParty2,
       "midaDRLinkDevicesTableParticipants": midaDRLinkDevicesTableParticipants,
       "midaDRLinkDevicesTableCallId": midaDRLinkDevicesTableCallId,
       "midaDRLinkDevicesTableType": midaDRLinkDevicesTableType,
       "midaDRLinkDevicesTableStatus": midaDRLinkDevicesTableStatus,
       "midaDRLinkDevicesTableRowStatus": midaDRLinkDevicesTableRowStatus,
       "midaDRLinkTDMServerTable": midaDRLinkTDMServerTable,
       "midaDRLinkTDMServerTableEntry": midaDRLinkTDMServerTableEntry,
       "midaDRLinkTDMServerTableIndex": midaDRLinkTDMServerTableIndex,
       "midaDRLinkTDMServerTableServer": midaDRLinkTDMServerTableServer,
       "midaDRLinkTDMServerTableStatus": midaDRLinkTDMServerTableStatus,
       "midaDRLinkTDMServerTableRowStatus": midaDRLinkTDMServerTableRowStatus,
       "midaDRLinkTDMConnectionTable": midaDRLinkTDMConnectionTable,
       "midaDRLinkTDMConnectionTableEntry": midaDRLinkTDMConnectionTableEntry,
       "midaDRLinkTDMConnectionTableIndex": midaDRLinkTDMConnectionTableIndex,
       "midaDRLinkTDMConnectionTableTSAPIServerIndex": midaDRLinkTDMConnectionTableTSAPIServerIndex,
       "midaDRLinkTDMConnectionTablePcmCrystal": midaDRLinkTDMConnectionTablePcmCrystal,
       "midaDRLinkTDMConnectionTablePcmCoupler": midaDRLinkTDMConnectionTablePcmCoupler,
       "midaDRLinkTDMConnectionTablePCMTimeslot": midaDRLinkTDMConnectionTablePCMTimeslot,
       "midaDRLinkTDMConnectionTableBoard": midaDRLinkTDMConnectionTableBoard,
       "midaDRLinkTDMConnectionTableSpan": midaDRLinkTDMConnectionTableSpan,
       "midaDRLinkTDMConnectionTableChannel": midaDRLinkTDMConnectionTableChannel,
       "midaDRLinkTDMConnectionTableStatus": midaDRLinkTDMConnectionTableStatus,
       "midaDRLinkTDMConnectionTableRowStatus": midaDRLinkTDMConnectionTableRowStatus,
       "midaRecorderErlangUsage": midaRecorderErlangUsage,
       "midaScheduler": midaScheduler,
       "midaSchedulerServiceStatus": midaSchedulerServiceStatus,
       "midaVoiceServices": midaVoiceServices,
       "midaVoiceServicesActiveCalls": midaVoiceServicesActiveCalls,
       "midaQMTable": midaQMTable,
       "midaQMTableEntry": midaQMTableEntry,
       "midaQMTableIndex": midaQMTableIndex,
       "midaQMServiceStatus": midaQMServiceStatus,
       "midaQMServiceName": midaQMServiceName,
       "midaQMServiceNumber": midaQMServiceNumber,
       "midaQMServiceSupervisors": midaQMServiceSupervisors,
       "midaQMServiceAgents": midaQMServiceAgents,
       "midaQMServiceLoggedAgents": midaQMServiceLoggedAgents,
       "midaQMTableRowStatus": midaQMTableRowStatus}
)
